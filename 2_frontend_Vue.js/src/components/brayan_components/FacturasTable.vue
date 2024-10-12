<script setup>
import { computed, ref, onMounted, watch } from 'vue'
import { useMainStore } from '@/stores/main'
import { mdiEye, mdiTrashCan, mdiPencilBoxMultiple, mdiFoodForkDrink, mdiCartPlus, mdiPencilPlus, mdiEyeCheckOutline } from '@mdi/js'
import CardModalBrayan from '@/components/brayan_components/CardModalBrayan.vue'
import CardLista from '@/components/brayan_components/CardLista.vue'
import TableCheckboxCell from '@/components/TableCheckboxCell.vue'
import BaseLevel from '@/components/BaseLevel.vue'
import BaseButtons from '@/components/BaseButtons.vue'
import BaseButton from '@/components/BaseButton.vue'
import UserAvatar from '@/components/UserAvatar.vue'
import NotificationBar from '@/components/alejo_components/NotificationBar.vue'

defineProps({
  checkable: Boolean
})

import jsPDF from "jspdf";
import html2canvas from "html2canvas";

import { getProductosFacturaById, deleteProductoFactura, updateProductoFactura, addProductoToFactura,getAllProductosPrueba } from "@/services/brayan_service/FacturaProductoService";
import { getAllFacturas, updateFacturaService, deleteFactura, getFacturaByPage, getFacturaByid } from "@/services/brayan_service/FacturacionService";


//ESTO ES PARA OBTENER LOS PRODUCTOS Y PONERLOS EN EL INPUT DE AGREGAR PRODUCTO, te odio  NICOLAS
const productosDisponibles = ref([]);

const fetchAllProductos = async () => {
  try {
    const response = await getAllProductosPrueba();
    console.log('Respuesta de la API:', response);  // Asume que la lista de productos está correctamente en response
    productosDisponibles.value = response; // Asume que la lista de productos está correctamente en response
  } catch (error) {
    console.error("Error al obtener productos:", error);
  }
};

onMounted(() => {
  fetchAllProductos(); // Cargar la lista de productos cuando el componente se monte
});

//variables de facturas
const facturas = ref([]);
const selectedFactura = ref({});
const showEditModal = ref(false);
const showDeleteModal = ref(false);
const showDetalles = ref(false);
const facturasOriginales = ref([]);
const TotalPages = ref(0);
const currentPage = ref(1);

const buscarFactura = ref('');



const metodosDePago = ['EFECTIVO', 'TARJETA', 'TRANSFERENCIA'];

 // Lista de estados
const estados = ['PAGADA', 'PENDIENTE', 'CANCELADA'];


const isAlertVisible = ref(false);
const modalMessage = ref('');
const colorAlert = ref('');

async function buscar_Factura() {
  // Si el campo de búsqueda está vacío, se obtienen todas las facturas
  if (buscarFactura.value.trim() === '') {
    fetchFacturas();
  } else {

    try {
      const response = await getFacturaByid(buscarFactura.value);
      console.log('Respuesta de la API:', response);
      if (response && response.data) {
        // Actualiza selectedFactura y facturas
        selectedFactura.value = response.data;
        facturas.value = [selectedFactura.value]; // Mostrar  factura encontrada
      } else {
        // Si no se encuentra la factura, limpiar selectedFactura pero no facturas
        selectedFactura.value = null;
      }
    } catch (error) {
      console.error('Error al encontrar la factura:', error);

      // Mantener las facturas existentes en caso de error
      selectedFactura.value = null;
    }
  }
}


const filtrarFacturasPorEstado = () => {
  const estadoSeleccionado = selectedFactura.value.estado;

  if (estadoSeleccionado === "") {
    // Si el estado es "Ninguna", mostrar todas las facturas
    facturas.value = [...facturasOriginales.value];
  } else {
    // Filtrar facturas basadas en el estado seleccionado
    facturas.value = facturasOriginales.value.filter(factura => factura.estado === estadoSeleccionado);
  }
  if (facturas.value.length === 0) {
    modalMessage.value = 'No se encontraron facturas con el estado seleccionado';
    isAlertVisible.value = true;
    colorAlert.value = 'danger';

    // Cerrar la alerta automáticamente después de 3 segundos
    setTimeout(() => {
      isAlertVisible.value = false;
    }, 5000);
  }
};



//ver facturas
const fetchFacturas = async () => {
  try {
    const response = await getFacturaByPage(currentPage.value);
    facturas.value = response.data.facturaciones;
    facturasOriginales.value = [...facturas.value]; // Guardamos todas las facturas sin filtrar
    TotalPages.value = response.data.total_pages;
  } catch (error) {
    console.error('Error al obtener facturas:', error.message);
  }
};


onMounted(() => {
  fetchFacturas();
});

const emit = defineEmits(['update', 'close']);



//actualizar facturas
const updateFactura = async () => {
  try {
    await updateFacturaService(
      selectedFactura.value.id_facturacion,
      selectedFactura.value.subtotal,
      selectedFactura.value.impuestos,
      selectedFactura.value.total,
      selectedFactura.value.total_precio_productos,
      selectedFactura.value.metodo_pago,
      selectedFactura.value.estado,
      selectedFactura.value.fecha_salida
    );
    fetchFacturas();
    closeEditModal();
    modalMessage.value = 'La factura se actualizo exitosamente';
    isAlertVisible.value = true;
    colorAlert.value = 'success';
    setTimeout(() => {
      isAlertVisible.value = false;
    }, 3000);
    
    emit('update');
    emit('close');
  } catch (error) {
    fetchFacturas();
    closeEditModal();
    modalMessage.value = 'Hubo un error al actualizar la factura';
    isAlertVisible.value = true;
    colorAlert.value = 'danger';
    setTimeout(() => {
      isAlertVisible.value = false;
    }, 3000);
  }
};



//Eliminar factura
const confirmDelete = async () => {
  try {
    await deleteFactura(selectedFactura.value.id_facturacion);
    fetchFacturas();
    closeDeleteModal();
    modalMessage.value = 'La factura se elimino exitosamente';
    isAlertVisible.value = true;
    colorAlert.value = 'success';
    setTimeout(() => {
      isAlertVisible.value = false;
    }, 3000);
   
    emit('delete');  // Emite el evento correcto para que lo maneje el componente padre
    emit('close');   // Cierra el modal
  } catch (error) {
    if (error.response?.status === 400) {
      fetchFacturas();
      closeDeleteModal();
      modalMessage.value = 'Hubo un error al eliminar la factura';
      isAlertVisible.value = true;
      colorAlert.value = 'danger';
      setTimeout(() => {
      isAlertVisible.value = false;
    }, 3000);
    } 
  }
};


//ABRIR MODAL DE EDITAR Y ELIMINAR FACTURA
function openEditModal(factura) {
  selectedFactura.value = { ...factura, fecha_salida: factura.fecha_salida ? factura.fecha_salida.replace(' ', 'T').split('.')[0] : '' }; // Clona la factura seleccionada
  showEditModal.value = true;
}

function openDeleteModal(factura) {
  selectedFactura.value = { ...factura };
  showDeleteModal.value = true;
}

function openDetallesmodal(factura) {
  selectedFactura.value = { ...factura };
  showDetalles.value = true;
  console.log("Factura seleccionada:", selectedFactura.value);
  
}




//CERRAR MODAL DE EDITAR Y ELIMINAR FACTURA
function closeEditModal() {
  showEditModal.value = false;
}

function closeDeleteModal() {
  showDeleteModal.value = false;
}

function closeDetallesModal() {
  showDetalles.value = false;
}


function cerrarEditarFactura() {
  closeEditModal();
}

function cerrarEliminarFactura() {
  closeDeleteModal();
}


function cerrarDetallesFactura() {
  closeDetallesModal();
}


//

//PRODUCTOS DE FACTURAS |||||||||||||||||||


//variables de productos de facturas
const productos = ref([]);
const selectedProduct = ref({
  factura_producto: {
    id_facturacion: null,
    id_producto: null,
    cantidad: null,
    fecha: null,
    precio_unitario: null,

  },

});
const showListaProductosModal = ref(false);
const showAgregarProductosModal = ref(false);
const showDeleteProductosModal = ref(false);
const showEditProductosModal = ref(false);


//LISTA DE PRODCUTOS DE FACTURA
const fetchProductos = async () => {
  try {
    if (selectedFactura.value && selectedFactura.value.id_facturacion) {
      const response = await getProductosFacturaById(selectedFactura.value.id_facturacion);
      console.log(response); // Verifica la estructura de la respuesta
      if (response && response.productos) {
        productos.value = response.productos; // Asegúrate de asignar la lista de productos
      } else {
        console.error('No se encontraron productos en la respuesta:', response);
      }
    }
  } catch (error) {
    console.error('Error al obtener productos de la factura:', error);
  }
};

watch(() => selectedFactura.value, fetchProductos, { immediate: true });


const addProducto = async () => {
  try {
    console.log('Datos del producto a agregar:', selectedProduct.value);
    await addProductoToFactura(
      selectedFactura.value.id_facturacion,
      selectedProduct.value.id_producto,
      selectedProduct.value.cantidad,
      selectedProduct.value.fecha,
      selectedProduct.value.precio_unitario
    );
    fetchProductos();
    closeAgregarProductosModal();
    resetSelectedProduct();
    modalMessage.value = 'El Producto se agrego exitosamente';
    isAlertVisible.value = true;
    colorAlert.value = 'info';
    setTimeout(() => {
      isAlertVisible.value = false;
    }, 3000);
   
  } catch (error) {
    closeAgregarProductosModal();
    modalMessage.value = 'Hubo un error al agregar el producto';
    isAlertVisible.value = true;
    colorAlert.value = 'danger';
    setTimeout(() => {
      isAlertVisible.value = false;
    }, 3000);
  }
};

function resetSelectedProduct() {
  selectedProduct.value = {
    id_producto: null,
    cantidad: null,
    fecha: null,
    precio_unitario: null
  };
}






//ELIMINAR PRODUCTO DE FACTURA
const confirmDeleteProducto = async () => {
  try {
    console.log('Confirmar eliminación del producto:', selectedProduct.value); // Verifica que se muestra la información del producto
    await deleteProductoFactura(selectedProduct.value.factura_producto.id_factura_producto);
    fetchProductos();
    closeDeleteProductosModal();
    closeListaProductosModal();
    modalMessage.value = 'el producto se elimino exitosamente de la factura';
    isAlertVisible.value = true;
    colorAlert.value = 'info';
    setTimeout(() => {
      isAlertVisible.value = false;
    }, 3000);
   
  } catch (error) {
    closeDeleteProductosModal();
    closeListaProductosModal();
    modalMessage.value = 'Hubo un error al eliminar el producto de la factura';
    isAlertVisible.value = true;
    colorAlert.value = 'danger';
    setTimeout(() => {
      isAlertVisible.value = false;
    }, 3000);
  }
};


//ACTUALIZAR PRODUCTO DE FACTURA
const updateProducto = async () => {
  try {
    console.log('Datos del producto en el modal:', selectedProduct.value);
    await updateProductoFactura(
      selectedProduct.value.factura_producto.id_factura_producto,
      selectedProduct.value.factura_producto.cantidad,
      selectedProduct.value.fecha,
      selectedProduct.value.factura_producto.precio_unitario
    );
    closeEditProductosModal();
    closeListaProductosModal();
    modalMessage.value = 'el producto se actualizo exitosamente en la factura';
    isAlertVisible.value = true;
    colorAlert.value = 'info';
    setTimeout(() => {
      isAlertVisible.value = false;
    }, 3000);
   
    
  } catch (error) {
    closeEditProductosModal();
    closeListaProductosModal();
    modalMessage.value = 'Hubo un error al eliminar el producto de la factura';
    isAlertVisible.value = true;
    colorAlert.value = 'danger';
    setTimeout(() => {
      isAlertVisible.value = false;
    }, 3000);
  }
};





//ABRIR MODAL DE LISTA DE PRODUCTOS DE LA FACTURA

function openListaProductosModal(factura) {
  selectedFactura.value = factura;
  showListaProductosModal.value = true;
}



//ABRIR MODAL DE AGREGAR PRODUCTOS A LA FACTURA
function openAgregarProductosModal(factura) {
  selectedFactura.value = factura;
  showAgregarProductosModal.value = true;
}



const openEditProductoModal = (producto) => {
  if (producto && producto.factura_producto && producto.factura_producto.id_factura_producto) {
    console.log('Producto seleccionado para editar:', producto);
    selectedProduct.value = { ...producto };
    showEditProductosModal.value = true;
  } else {
    console.error('Producto no válido:', producto);
  }
};



const openDeleteProductoModal = (producto) => {
  if (producto && producto.factura_producto && producto.factura_producto.id_factura_producto) {
    console.log('Producto seleccionado:', producto.factura_producto.id_factura_producto);
    selectedProduct.value = { ...producto };
    showDeleteProductosModal.value = true;
  } else {
    console.error('Producto no válido:', producto);
  }
};



//CERRAR MODAL DE LISTA DE PRODUCTOS DE LA FACTURA
function closeListaProductosModal() {
  showListaProductosModal.value = false;
}


function closeAgregarProductosModal() {
  showAgregarProductosModal.value = false;
}


const closeEditProductosModal = () => {
  showEditProductosModal.value = false;
};

const closeDeleteProductosModal = () => {
  showDeleteProductosModal.value = false;
};




//CERRAR MODALES DE AGREGAR Y ELIMINAR PRODUCTOS DE LA FACTURA
function cerrarlistaProductoFactura() {
  closeListaProductosModal();
}


function cerrarEditarProductoFactura() {
  closeEditProductosModal();
}

function cerrarEliminarProductoFactura() {
  closeDeleteProductosModal();
}

function cerrarAgregarProductoFactura() {
  closeAgregarProductosModal();
}

const downloadPDF = () => {
  const facturaDetalles = document.getElementById('facturaDetalles');

  // Almacenar el estilo original
  const originalBackgroundColor = facturaDetalles.style.backgroundColor;
  const originalColor = facturaDetalles.style.color;

  // Cambiar temporalmente a un tema claro
  facturaDetalles.style.backgroundColor = 'white';
  facturaDetalles.style.color = 'black';

  // Elimina el límite de altura para la captura completa del contenido
  const originalMaxHeight = facturaDetalles.style.maxHeight;
  facturaDetalles.style.maxHeight = 'none'; 

  // Captura el contenido del modal con html2canvas
  html2canvas(facturaDetalles, { scale: 1, width: facturaDetalles.offsetWidth, height: facturaDetalles.scrollHeight })
    .then((canvas) => {
      const imgData = canvas.toDataURL('image/png', 1);
      const pdf = new jsPDF();

      const imgWidth = 190; // Ancho del PDF
      const pageHeight = pdf.internal.pageSize.height;
      const imgHeight = (canvas.height * imgWidth) / canvas.width;
      let heightLeft = imgHeight;

      let position = 0;

      // Agregar la primera imagen
      pdf.addImage(imgData, 'PNG', 10, position, imgWidth, imgHeight);
      heightLeft -= pageHeight;

      // Manejar el contenido que excede la altura de la página
      while (heightLeft >= 0) {
        position = heightLeft - imgHeight;
        pdf.addPage();
        pdf.addImage(imgData, 'PNG', 10, position, imgWidth, imgHeight);
        heightLeft -= pageHeight;
      }

      // Guardar el PDF
      pdf.save('factura.pdf');

      // Restaurar el estilo original
      facturaDetalles.style.backgroundColor = originalBackgroundColor;
      facturaDetalles.style.color = originalColor;
      facturaDetalles.style.maxHeight = originalMaxHeight;
    })
    .catch((error) => {
      console.error('Error al generar el PDF:', error);
      
      // Restaurar el estilo original en caso de error
      facturaDetalles.style.backgroundColor = originalBackgroundColor;
      facturaDetalles.style.color = originalColor;
      facturaDetalles.style.maxHeight = originalMaxHeight;
    });
};




function fechaActual() {
  const hoy = new Date();

  return hoy.toLocaleDateString('es-ES'); // Cambia el idioma según sea necesario
}

</script>


<template>

<NotificationBar
  v-if="isAlertVisible"
  :color="colorAlert" 
  :description="modalMessage"
  :visible="isModalVisible"
/>

  <!-- CARDBOX PARA EDITAR FACTURA-->
  <div id="cardEditar">
    <CardModalBrayan v-model="showEditModal" title="Editar Factura">
      <form @submit.prevent="updateFactura">
        <div class="grid grid-cols-2 sm:grid-cols-2  gap-4">
          <!-- Primer par de campos -->
         
          <!-- Tercer par de campos -->
          <div class="mb-4">
            <label for="facturaMetodoPago" class="block text-gray-700">Método de Pago</label>
            <select id="facturaMetodoPago" v-model="selectedFactura.metodo_pago"
                    class="w-full border border-gray-300 rounded px-3 py-2 text-gray-800 focus:outline-none focus:border-blue-500">
              <!-- Lista de métodos de pago predefinidos -->
              <option v-for="metodo in metodosDePago" :key="metodo" :value="metodo">
                {{ metodo }}
              </option>
            </select>
          </div>

          <div class="mb-4">
            <label for="facturaEstado" class="block text-gray-700">Estado</label>
            <select id="facturaEstado" v-model="selectedFactura.estado"
                    class="w-full border border-gray-300 rounded px-3 py-2 text-gray-800 focus:outline-none focus:border-blue-500">
              <!-- Lista de estados predefinidos -->
              <option v-for="estado in estados" :key="estado" :value="estado">
                {{ estado }}
              </option>
            </select>
          </div>
          <!-- Último par de campos -->
          <div class="mb-4">
            <label for="facturaFechaSalida" class="block text-gray-700 dark:text-gray-300 font-medium">Fecha
              Salida</label>
            <input type="datetime-local" id="facturaFechaSalida"
              class="mt-1 block w-full border-gray-300 dark:border-gray-600 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:text-gray-300 sm:text-sm"
              v-model="selectedFactura.fecha_salida" required />
          </div>
        </div>

        <!-- Botón de enviar (guardar cambios) -->
        <div class="mt-3flex justify-start">
          <BaseButton class="mx-3" type="button" label="Cerrar" color="info" medium @click="cerrarEditarFactura" />
          <BaseButton type="submit" label="Editar" color="success" medium />

        </div>
      </form>
    </CardModalBrayan>
  </div>




  <!-- CARDBOX PARA ELIMINAR FACTURA -->
  <CardModalBrayan v-model="showDeleteModal" title="Eliminar Factura">
    <div class="mb-4">
      <p id="texto_">
        ¿Está seguro que desea eliminar la factura con el ID {{ selectedFactura.id_facturacion }}?
      </p>
    </div>

    <div class="flex justify-end mt-5">
      <BaseButton class="mx-3" type="button" label="Cancelar" color="info" medium @click="cerrarEliminarFactura" />
      <BaseButton type="button" label="Eliminar" color="danger" small @click="confirmDelete" />

    </div>
  </CardModalBrayan>






  <!-- SECCION DE PRODUCTOOOOOS
//
//

//

-->

  <!-- CARDBOX PARA VER LA LISTA DE PRODUCTOS DE UNA FACTURA-->
  <CardLista v-model="showListaProductosModal" title="Historial de Productos de la Factura">
    <div class="relative overflow-x-auto ">

      <div class="max-h-96 overflow-y-auto ">
        <table id="tabla_productos">
          <thead class="text-xs text-gray-700 uppercase bg-blue-100 ">
            <tr>
              <th>ID Facturación</th>
             <!-- <th>ID Factura Producto</th> -->
              <th>ID Producto</th>
              <th>Cantidad</th>
              <th>Fecha</th>
              <th>Precio U</th>
              <th>Nombre</th>
              <th>Descripción</th>
              <th>Precio Actual</th>
              <th>Acciones</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="producto in productos" :key="producto.factura_producto.id_factura_producto">
              <td :data-label="'ID Facturación'">{{ selectedFactura.id_facturacion }}</td>
                <!--<td :data-label="'ID Factura Producto'">{{ producto.factura_producto.id_factura_producto }}</td> -->
              <td :data-label="'ID Producto'">{{ producto.factura_producto?.id_producto || 'N/A' }}</td>
              <td :data-label="'Cantidad'">{{ producto.factura_producto?.cantidad || 'N/A' }}</td>
              <td :data-label="'Cantidad'">{{ producto.factura_producto?.fecha || 'N/A' }}</td>
              <td :data-label="'Precio U'">{{ producto.factura_producto?.precio_unitario || 'N/A' }}</td>
              <td :data-label="'Nombre'">{{ producto.productos?.nombre_producto || 'N/A' }}</td>
              <td :data-label="'Descripción'">{{ producto.productos?.descripcion || 'N/A' }}</td>
              <td :data-label="'Precio Actual'">{{ producto.productos?.precio_actual || 'N/A' }}</td>
              <td :data-label="'Acciones'">
                <div class="flex justify-center space-x-2">
                  <BaseButton color="info" :icon="mdiPencilPlus" small @click="openEditProductoModal(producto)">
                  </BaseButton>
                  <BaseButton color="danger" :icon="mdiTrashCan" small @click="openDeleteProductoModal(producto)">
                  </BaseButton>

                </div>
              </td>
            </tr>
          </tbody>
        </table>

      </div>
    </div>
    <div class="flex justify-end ">

      <button type="button" @click="cerrarlistaProductoFactura"
        class="bg-gray-500 text-white mt-4 px-4 py-2 rounded mr-2 ">
        Salir
      </button>
    </div>
  </CardLista>


  <!-- CARDBOX PARA ELIMINAR PRODUCTO DE UNA FACTURA -->
  <CardModalBrayan v-model="showDeleteProductosModal" title="Eliminar Producto">
    <p id="texto_" class="mb-4">
      ¿Está seguro que desea eliminar el Producto de la factura?
    </p>

    <div class="flex justify-end">
      <button type="button" @click="cerrarEliminarProductoFactura"
        class="bg-gray-500 text-white px-4 py-2 rounded mr-2">
        Cancelar
      </button>
      <button type="button" @click="confirmDeleteProducto" class="bg-red-500 text-white px-4 py-2 rounded">
        Eliminar
      </button>
    </div>
  </CardModalBrayan>


  <!-- CARDBOX PARA EDITAR PRODUCTO DE UNA FACTURA -->
  <CardModalBrayan v-model="showEditProductosModal" title="Editar Producto">
    <form @submit.prevent="updateProducto">
      <div class="mb-4">
        <label for="cantidad" class="block text-gray-700">Cantidad</label>
        <input type="number" id="cantidad" v-model="selectedProduct.factura_producto.cantidad"
          class="w-full border border-gray-300 rounded px-3 py-2 text-gray-800 focus:outline-none focus:border-blue-500"
          required />
      </div>
      <div class="mb-4">
        <label for="fecha" class="block text-gray-700">Fecha</label>
        <input type="date" id="fecha" v-model="selectedProduct.fecha"
          class="w-full border border-gray-300 rounded px-3 py-2 text-gray-800 focus:outline-none focus:border-blue-500" required/>
      </div>
      <div class="mb-4">
        <label for="precio_unitario" class="block text-gray-700">Precio Unitario</label>
        <input type="number" id="precio_unitario" v-model="selectedProduct.factura_producto.precio_unitario"
          class="w-full border border-gray-300 rounded px-3 py-2 text-gray-800 focus:outline-none focus:border-blue-500"
          required />
      </div>

      <div class="flex justify-end">
        <button @click="cerrarEditarProductoFactura" type="button"
          class="bg-gray-500 text-white px-4 py-2 rounded mr-2 hover:bg-gray-600 transition">
          Cancelar
        </button>
        <button type="submit" class="bg-blue-800 text-white px-4 py-2 rounded hover:bg-blue-700 transition">
          Editar
        </button>
      </div>
    </form>
  </CardModalBrayan>


  <!-- CARDBOX PARA AGREGAR PRODUCTO DE UNA FACTURA -->
  <CardModalBrayan v-model="showAgregarProductosModal" title="Agregar Producto a la Factura">
    <form @submit.prevent="addProducto">
      <div class="mb-4">
        <label for="id_facturacion" class="block text-gray-700">ID facturación</label>
        <input id="id_facturacion" v-model="selectedFactura.id_facturacion" type="number" disabled
          class="w-full border border-gray-300 rounded px-3 py-2 text-gray-800 bg-gray-100 focus:outline-none focus:border-blue-500"  required/>
      </div>
      <div class="mb-4">
        <label for="id_producto" class="block text-gray-700"> Producto</label>
        <select id="id_producto" v-model="selectedProduct.id_producto" required
                class="w-full border border-gray-300 rounded px-3 py-2 text-gray-800 focus:outline-none focus:border-blue-500">
          <option v-for="producto in productosDisponibles" :key="producto.id_producto" :value="producto.id_producto">
            {{ producto.nombre_producto}} / $: {{ producto.precio_actual }}
          </option>
        </select>
      </div>
      <div class="mb-4">
        <label for="cantidad" class="block text-gray-700">Cantidad</label>
        <input id="cantidad" v-model="selectedProduct.cantidad" type="number"
          class="w-full border border-gray-300 rounded px-3 py-2 text-gray-800 focus:outline-none focus:border-blue-500" required />
      </div>
      <div class="mb-4">
        <label for="fecha" class="block text-gray-700">Fecha</label>
        <input id="fecha" v-model="selectedProduct.fecha" type="date"
          class="w-full border border-gray-300 rounded px-3 py-2 text-gray-800 focus:outline-none focus:border-blue-500" required />
      </div>
      <div class="mb-4">
        <label for="precio_unitario" class="block text-gray-700">Precio Unitario</label>
        <input id="precio_unitario" v-model="selectedProduct.precio_unitario" type="number"
          class="w-full border border-gray-300 rounded px-3 py-2 text-gray-800 focus:outline-none focus:border-blue-500"  required/>
      </div>
      <div class="flex justify-end">
        <button type="button" @click="cerrarAgregarProductoFactura"
          class="bg-gray-500 text-white px-4 py-2 rounded mr-2 hover:bg-gray-600 transition">
          Cancelar
        </button>
        <button type="submit" class="bg-blue-800 text-white px-4 py-2 rounded hover:bg-blue-700 transition">
          Agregar
        </button>
      </div>
    </form>
  </CardModalBrayan>



  <div class="mb-6 max-w-md mx-left">
    <h1 class="text-black dark:text-white text-3xl font-bold mb-3">Seccion de Facturas</h1>
    <div class="flex items-center space-x-4">
    <!-- Input de búsqueda -->
    <div class="flex items-center border rounded-lg shadow-sm flex-grow">
      <input
        type="search"
        id="buscarFactura"
        placeholder="Buscar factura por ID"
        class="w-full px-4 py-2 border-gray-300 rounded-lg focus:ring-blue-500 focus:border-blue-500 sm:text-sm"
        v-model="buscarFactura"
        @input="buscar_Factura"
      />
    </div>
    
    <!-- Filtro de estado -->
    <div class="flex items-center" style="width: 200px;">
      <h2 class="mr-3 text-sm">Filtrar por:</h2>
      <select id="facturaEstado" v-model="selectedFactura.estado" class="w-full border border-gray-300 rounded px-3 py-2 text-gray-800 focus:outline-none focus:border-blue-500 text-sm" @change="filtrarFacturasPorEstado">
        <option value="">Ninguna</option> 
        <option v-for="estado in estados" :key="estado" :value="estado">
          {{ estado }}
        </option>
      </select>
    </div>
  </div>
  </div>


  <!-- SECCION  DE HISTORIAL DE FACTURAS-->
  <div class="relative overflow-x-auto">




    <div class="grid grid-cols-1 md:grid-cols-5 gap-4 py-4">

    </div>
    <table>
      <thead>
        <tr>
          <th v-if="checkable" />

          <th class="">ID Facturación</th>
           <!--<th class="">ID Check-in</th>-->
          <th class="">Nombre</th>
          <th class="">N° Documento</th>
          <th class="">Email</th>
          <th class="">Telefono</th>
          <th class="">Subtotal</th>
          <th class="">Impuestos</th>
          <th class="">ID descuento</th>
          <th class="">% descuento</th>       
          <th class="">Total Precio Productos</th>
          <th class="">Total a pagar</th>
          <th class="">Método de Pago Factura</th>
          <th class="">Estado</th>
          <th class="">Fecha Salida</th>
          <!-- <th class="">ID Reserva</th>
          <th class="">Medio Llegada</th>
          <th class="">Llegada Situación</th>
          <th class="">Equipaje</th>
          <th class="">Fecha Reserva</th>
          <th class="">Empresa</th>
          <th class="">Valor Depósito</th>
          <th class="">Forma de Pago Reserva</th>-->

          <th class="">Acciones</th>

        </tr>
      </thead>
      <tbody>
        <tr v-for="factura in facturas" :key="factura.id_facturacion">

          <td data-label="ID Facturación">{{ factura.id_facturacion }}</td>
            <!--<td data-label="ID Check-In">{{ factura.check_in.id_check_in }}</td>-->
          <td data-label="Nombre Completo">{{ factura.huesped.nombre_completo }}</td>
          <td data-label="Número de Documento">{{ factura.huesped.numero_documento }}</td>
          <td data-label="Email">{{ factura.huesped.email }}</td>
          <td data-label="Telefono">{{ factura.huesped.telefono }}</td>
          <td data-label="Subtotal">{{ factura.subtotal }}</td>
          <td data-label="Impuestos">{{ factura.impuestos }}</td>
          <td data-label="id descuento">{{ factura.descuento.id_descuento }}</td>
          <td data-label="id descuento">{{ factura.descuento.porcentaje_descuento + '%'}} </td>
      
          <td data-label="Total Precio Productos">{{ factura.total_precio_productos }}</td>
          <td data-label="Total a pagar">{{ factura.total }}</td>
          <td data-label="Método de Pago Factura">{{ factura.metodo_pago }}</td>
          <td data-label="Estado">{{ factura.estado }}</td>
          <td data-label="Fecha de Salida">{{ factura.fecha_salida }}</td>
         <!-- <td data-label="ID Reserva">{{ factura.reserva.id_reserva }}</td>
          <td data-label="Medio de Llegada">{{ factura.check_in.medio_llegada }}</td>
          <td data-label="Llegada Situación">{{ factura.check_in.llegada_situacion }}</td>
          <td data-label="Equipaje">{{ factura.check_in.equipaje }}</td>
          <td data-label="Fecha Reserva">{{ factura.reserva.fecha_reserva }}</td>
          <td data-label="Empresa">{{ factura.reserva.empresa }}</td>
          <td data-label="Valor Depósito">{{ factura.reserva.valor_deposito }}</td>
          <td data-label="Forma de Pago Reserva">{{ factura.reserva.forma_pago }}</td>-->

          <td class="before:hidden lg:w-1 whitespace-nowrap">
            <BaseButtons type="justify-start lg:justify-end" no-wrap>
              <BaseButton color="primary" :icon="mdiEyeCheckOutline" small @click="openDetallesmodal(factura)">
              </BaseButton>
              <BaseButton color="warning" :icon="mdiCartPlus" small @click="openAgregarProductosModal(factura)">
              </BaseButton>
              <BaseButton color="success" :icon="mdiFoodForkDrink" small @click="openListaProductosModal(factura)">
              </BaseButton>
              <BaseButton color="info" :icon="mdiPencilBoxMultiple" small @click="openEditModal(factura)" />
              <BaseButton color="danger" :icon="mdiTrashCan" small @click="openDeleteModal(factura)" />

            </BaseButtons>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
  <div class="p-3 lg:px-6 border-t border-gray-100 dark:border-slate-800 w-96">
    <BaseLevel>
        <BaseButtons style="display: inline-flex; overflow-x: auto; flex-wrap: nowrap;">
            <BaseButton
            v-for="page in TotalPages"
            :key="page"
            :active="page === currentPage"
            :label="page"
            :color="page === currentPage ? 'lightDark' : 'whiteDark'"
            small
            @click="currentPage = page; fetchFacturas()"
            />
        </BaseButtons>
        <small>Página {{ currentPage }} de {{ TotalPages }}</small>
    </BaseLevel>
    </div>



  <!-- VER INFO DE LA FACTURA-->
  <!-- CardBox para mostrar información de la factura y productos asociados -->
  <CardLista v-model="showDetalles" >
    <!-- Sección de Información de la Factura -->
    <div class="mb-2 overflow-y-auto max-h-96 " id="facturaDetalles" >
    <div >
      <div class="flex justify-between items-center mb-1" >
        <h1 class="font-bold text-lg" style="font-size: 26px; color: darkgreen;">DETALLES DE LA FACTURA</h1>

        <div class="flex items-center">

          <img src="@/assets/img/sena-agro.png" alt="" style="width: 70px; margin-right: 5px;">
        </div>

      </div>
      <div>
        <h2 class="font-bold">Fecha: {{ fechaActual() }}</h2>
      </div>
      <div class="mb-4 mt-4 mr-5 flex flex-wrap justify-between">
        <div class="w-full md:w-1/2 mb-2">

          <h2 class="font-bold mb-3">Cliente: {{ selectedFactura?.huesped?.nombre_completo }}</h2>
          <h2 class="font-bold">Documento: {{ selectedFactura?.huesped?.numero_documento }}</h2>
        </div>
        <div class="w-full md:w-1/2 mb-2">
          <h2 class="font-bold mb-3">Email: {{ selectedFactura?.huesped?.email }}</h2>
          <h2 class="font-bold">Teléfono: {{ selectedFactura?.huesped?.telefono }}</h2>
        </div>
      </div>
        <table>
          <thead>
            <tr>
              <th>Campo</th>
              <th>Valor</th>
            </tr>
          </thead>
          <tbody class="text-sm">
            <tr>
              <td data-label="Campo">ID Facturación</td>
              <td data-label="Valor">{{ selectedFactura?.id_facturacion }}</td>
            </tr>
             <!-- <tr>
              <td data-label="Campo">ID Check-In</td>
              <td data-label="Valor">{{ selectedFactura?.check_in?.id_check_in }}</td>
            </tr>-->
            <tr>
              <td data-label="Campo">Estado</td>
              <td data-label="Valor">{{ selectedFactura?.estado }}</td>
            </tr>
            <tr>
              <td data-label="Campo">Fecha de Salida</td>
              <td data-label="Valor">{{ selectedFactura?.fecha_salida }}</td>
            </tr>
            <!--<tr>
              <td data-label="Campo">ID Reserva</td>
              <td data-label="Valor">{{ selectedFactura?.reserva?.id_reserva }}</td>
            </tr>-->
            <tr>
              <td data-label="Campo">Medio de Llegada</td>
              <td data-label="Valor">{{ selectedFactura?.check_in?.medio_llegada }}</td>
            </tr>
            <tr>
              <td data-label="Campo">Llegada Situación</td>
              <td data-label="Valor">{{ selectedFactura?.check_in?.llegada_situacion }}</td>
            </tr>
            <tr>
              <td data-label="Campo">Equipaje</td>
              <td data-label="Valor">{{ selectedFactura?.check_in?.equipaje }}</td>
            </tr>
            <tr>
              <td data-label="Campo">Fecha Reserva</td>
              <td data-label="Valor">{{ selectedFactura?.reserva?.fecha_reserva }}</td>
            </tr>
            <tr>
              <td data-label="Campo">Empresa</td>
              <td data-label="Valor">{{ selectedFactura?.reserva?.empresa }}</td>
            </tr>
            <tr>
              <td data-label="Campo">Valor Depósito</td>
              <td data-label="Valor">{{ selectedFactura?.reserva?.valor_deposito }}</td>
            </tr>
            <tr>
            <td>Porcentaje Descuento</td>
            <td>{{ selectedFactura?.descuento?.porcentaje_descuento !== undefined ? selectedFactura.descuento.porcentaje_descuento + '%' : 'N/A' }}</td>
          </tr>
            <tr>
              <td data-label="Campo">Forma de Pago-Reserva</td>
              <td data-label="Valor">{{ selectedFactura?.reserva?.forma_pago }}</td>
            </tr>

            <tr>
              <td data-label="Campo">Método de Pago Factura</td>
              <td data-label="Valor">{{ selectedFactura?.metodo_pago }}</td>
            </tr>
            <!--  <tr>
          <td>ID Descuento</td>
            <td>{{ selectedFactura?.descuento?.id_descuento || 'N/A' }}</td>
          </tr> -->
         


          </tbody>
        </table>

        <h3 class="text-lg font-semibold mb-3 mt-2">Productos Asociados</h3>
        <table class="mb-2" style="border: black  1px solid;">
          <thead>
            <tr>

              <th class=" text-sm">ID Producto</th>
              <th class=" text-sm">Cantidad</th>
              <th class=" text-sm">Precio Unitario</th>
              <th class=" text-sm">Nombre</th>
              <th class=" text-sm">Descripción</th>

            </tr>
          </thead>
          <tbody class="text-sm">
            <tr v-for="producto in productos" :key="producto.factura_producto.id_factura_producto">
              <td data-label="ID producto">{{ producto.factura_producto.id_producto || 'N/A' }}</td>
              <td data-label="cantidad">{{ producto.factura_producto.cantidad || 'N/A' }}</td>
              <td data-label="precio unitario">{{ producto.factura_producto.precio_unitario || 'N/A' }}</td>
              <td data-label="nombre">{{ producto.productos.nombre_producto || 'N/A' }}</td>
              <td data-label="descripcion">{{ producto.productos.descripcion || 'N/A' }}</td>
            </tr>


          </tbody>
        </table>
        <div class="mt-5 w-full md:w-1/2 mb-2" style="display: flex; flex-direction: column;">
            <div class="font-bold" data-label="Valor"  style="font-size: 16px;">Total precio productos: {{ selectedFactura?.total_precio_productos }}</div>
            <div class="font-bold" data-label="Valor" style="font-size: 16px;">Subtotal: {{ selectedFactura?.subtotal }}</div>
            <div class="font-bold" data-label="Valor" style="font-size: 16px;">Impuestos: {{ selectedFactura?.impuestos }}</div>
        <!--   <div class="font-bold" data-label="Valor" style="font-size: 16px;">Porcentaje descuento: {{ selectedFactura?.descuento.porcentaje_descuento }}</div>-->
            <div class="font-bold" data-label="Valor" style="font-size: 17px;">TOTAL A PAGAR: {{ selectedFactura?.total }}</div>
        </div>

      </div>
      <BaseButton type="button" @click="cerrarListaProductosModal"
        class="bg-gray-500 text-white px-4 py-2 rounded hover:bg-gray-600 transition">
        Cerrar
      </BaseButton>

    </div>
    <button @click="downloadPDF()" class="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600 transition">
            Descargar PDF
      </button>


  </CardLista>








  <!--  <div class="p-3 lg:px-6 border-t border-gray-100 dark:border-slate-800">
    <BaseLevel>
      <BaseButtons>
        <BaseButton v-for="page in pagesList" :key="page" :active="page === currentPage" :label="page + 1"
          :color="page === currentPage ? 'lightDark' : 'whiteDark'" small @click="currentPage = page" />
      </BaseButtons>
      <small>Page {{ currentPageHuman }} of {{ numPages }}</small>
    </BaseLevel>
  </div>
    -->
</template>
<style scoped>
th,
td {
  white-space: nowrap;
}

.dark input {
  background-color: #1f2937;
  /* Fondo oscuro */
  color: white;
  /* Texto claro */
  border-color: #374151;
  /* Borde oscuro */
}

/* #tabla_productos{

}
*/
</style>


