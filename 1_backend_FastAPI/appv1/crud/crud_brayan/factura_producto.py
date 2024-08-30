from typing import Any, Dict, List
from pydantic import ValidationError
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from appv1.schemas.schemas_brayan.factura_producto  import  Factura_productoBase, Factura_productoResponse, ProductosDetail, Factura_productoUpdate, Factura_productoConDetalles, FacturaDetail, Factura_productosDetail,MetodoPagoType, EstadoType, FacturaConProductosResponse

from fastapi import HTTPException
#from core.utils import generate_user_id
from core.security import get_hashed_password
from sqlalchemy.orm import Session



#crear factura
def create_factura_producto_sql(db: Session, factura_producto: Factura_productoBase):
    try:
        sql_query = text(
            "INSERT INTO factura_producto (id_facturacion, id_producto, cantidad, fecha, precio_unitario) "
            "VALUES (:id_facturacion, :id_producto, :cantidad, :fecha, :precio_unitario)"
        )
        params = {
            "id_facturacion": factura_producto.id_facturacion,
            "id_producto": factura_producto.id_producto,
            "cantidad": factura_producto.cantidad,
            "fecha": factura_producto.fecha,
            "precio_unitario": factura_producto.precio_unitario,
        }
        db.execute(sql_query, params)
        db.commit()
        return True
    except IntegrityError as e:
        db.rollback()
        if 'PRIMARY' in str(e.orig):
            raise HTTPException(status_code=400, detail="Error: El ID ya existe.")
        if 'for key \'id_facturacion\'' in str(e.orig):
            raise HTTPException(status_code=400, detail="Error: El ID de facturación no existe en la tabla de facturación.")
        if 'for key \'id_producto\'' in str(e.orig):
            raise HTTPException(status_code=400, detail="Error: El ID de producto no existe en la tabla de productos.")
        raise HTTPException(status_code=400, detail="Error de integridad de datos al crear la factura del producto.")
    except SQLAlchemyError as e:
        db.rollback()
        print(f"Error al crear factura de producto: {e}")
        raise HTTPException(status_code=500, detail="Error interno del servidor al crear la factura del producto.")







#obtener los productos de una factura
def get_productos_de_factura_by_id(db: Session, id_facturacion: int) -> Dict[str, Any]:
    try:
        # Obtener la información de la factura
        factura_sql = text("""
            SELECT 
                id_facturacion,
                id_check_in,
                subtotal,
                impuestos,
                total,
                total_precio_productos,
                metodo_pago,
                estado,
                fecha_salida
            FROM facturacion
            WHERE id_facturacion = :id_facturacion
        """)
        factura_result = db.execute(factura_sql, {"id_facturacion": id_facturacion}).fetchone()

        if not factura_result:
            raise HTTPException(status_code=404, detail="Factura no encontrada")

        # Convertir los valores de método de pago y estado al tipo adecuado
        metodo_pago = MetodoPagoType(factura_result.metodo_pago)
        estado = EstadoType(factura_result.estado)

        factura_detail = FacturaDetail(
            id_facturacion=factura_result.id_facturacion,
            check_in=factura_result.id_check_in,
            subtotal=factura_result.subtotal,
            impuestos=factura_result.impuestos,
            total=factura_result.total,
            total_precio_productos=factura_result.total_precio_productos,
            metodo_pago=metodo_pago,
            estado=estado,
            fecha_salida=factura_result.fecha_salida,
        )

        # Obtener los productos asociados con la factura
        productos_sql = text("""
            SELECT
                factura_producto.id_factura_producto,
                factura_producto.id_producto,
                factura_producto.cantidad,
                factura_producto.precio_unitario,
                productos.nombre_producto,
                productos.descripcion,
                productos.precio_actual
            FROM factura_producto
            JOIN productos ON factura_producto.id_producto = productos.id_producto
            WHERE factura_producto.id_facturacion = :id_facturacion
        """)
        productos_result = db.execute(productos_sql, {"id_facturacion": id_facturacion}).fetchall()

        productos_detalle = []
        for row in productos_result:
            try:
                producto = Factura_productosDetail(
                    id_factura_producto=row.id_factura_producto,
                    id_producto=row.id_producto,
                    cantidad=row.cantidad,
                    precio_unitario=row.precio_unitario,
                )

                producto_detalle = ProductosDetail(
                    nombre_producto=row.nombre_producto,
                    descripcion=row.descripcion,
                    precio_actual=row.precio_actual,
                )

                productos_detalle.append(Factura_productoConDetalles(
                    factura_producto=producto,
                    productos=producto_detalle
                ))
                
            except ValidationError as e:
                print(f"Error de validación en la fila: {row}, Error: {e}")
                raise

        return FacturaConProductosResponse(
            factura=factura_detail,
            productos=productos_detalle
        )

    except SQLAlchemyError as e:
        db.rollback()
        print(f"Error al buscar facturas: {e}")
        raise HTTPException(status_code=500, detail="Error al buscar facturas")




#este es par buscar en el actualizar 
def get_factura_productos_by_id(db: Session, id_factura_producto: int):
    # Asegúrate de que esta función devuelva un valor que indique si el producto existe o no
    sql = text("SELECT * FROM factura_producto WHERE id_factura_producto = :id_factura_producto")
    result = db.execute(sql, {"id_factura_producto": id_factura_producto}).fetchone()
    return result



def get_all_factura_productos(db: Session) -> List[FacturaConProductosResponse]:
    try:
        # Obtener todas las facturas
        factura_sql = text("""
            SELECT 
                id_facturacion,
                id_check_in,
                subtotal,
                impuestos,
                total,
                total_precio_productos,
                metodo_pago,
                estado,
                fecha_salida
            FROM facturacion
        """)
        factura_results = db.execute(factura_sql).fetchall()

        if not factura_results:
            raise HTTPException(status_code=404, detail="No se encontraron facturas")

        all_facturas = []

        for factura_result in factura_results:
            # Convertir los valores de método de pago y estado al tipo adecuado
            metodo_pago = MetodoPagoType(factura_result.metodo_pago)
            estado = EstadoType(factura_result.estado)

            factura_detail = FacturaDetail(
                id_facturacion=factura_result.id_facturacion,
                check_in=factura_result.id_check_in,
                subtotal=factura_result.subtotal,
                impuestos=factura_result.impuestos,
                total=factura_result.total,
                total_precio_productos=factura_result.total_precio_productos,
                metodo_pago=metodo_pago,
                estado=estado,
                fecha_salida=factura_result.fecha_salida,
            )

            # Obtener los productos asociados con la factura
            productos_sql = text("""
                SELECT
                    factura_producto.id_factura_producto,
                    factura_producto.id_producto,
                    factura_producto.cantidad,
                    factura_producto.precio_unitario,
                    productos.nombre_producto,
                    productos.descripcion,
                    productos.precio_actual
                FROM factura_producto
                JOIN productos ON factura_producto.id_producto = productos.id_producto
                WHERE factura_producto.id_facturacion = :id_facturacion
            """)
            productos_result = db.execute(productos_sql, {"id_facturacion": factura_result.id_facturacion}).fetchall()

            productos_detalle = []
            for row in productos_result:
                try:
                    producto = Factura_productosDetail(
                        id_factura_producto=row.id_factura_producto,
                        id_producto=row.id_producto,
                        cantidad=row.cantidad,
                        precio_unitario=row.precio_unitario,
                    )

                    producto_detalle = ProductosDetail(
                        nombre_producto=row.nombre_producto,
                        descripcion=row.descripcion,
                        precio_actual=row.precio_actual,
                    )

                    productos_detalle.append(Factura_productoConDetalles(
                        factura_producto=producto,
                        productos=producto_detalle
                    ))
                    
                except ValidationError as e:
                    print(f"Error de validación en la fila: {row}, Error: {e}")
                    raise

            all_facturas.append(FacturaConProductosResponse(
                factura=factura_detail,
                productos=productos_detalle
            ))

        return all_facturas

    except SQLAlchemyError as e:
        db.rollback()
        print(f"Error al buscar facturas: {e}")
        raise HTTPException(status_code=500, detail="Error al buscar facturas")



#actualizar productos factura
def update_productos_factura(db: Session, id_factura_producto: int, factura_producto: Factura_productoUpdate):
    try:
        sql = "UPDATE factura_producto SET "
        params = {"id_factura_producto": id_factura_producto}
        updates = []
        if factura_producto.cantidad is not None:
            updates.append("cantidad = :cantidad")
            params["cantidad"] = factura_producto.cantidad
        if factura_producto.fecha is not None:
            updates.append("fecha = :fecha")
            params["fecha"] = factura_producto.fecha
        if factura_producto.precio_unitario is not None:
            updates.append("precio_unitario = :precio_unitario")
            params["precio_unitario"] = factura_producto.precio_unitario

        # Verifica que haya al menos un campo para actualizar
        if not updates:
            raise HTTPException(status_code=400, detail="No hay campos para actualizar")

        sql += ", ".join(updates) + " WHERE id_factura_producto = :id_factura_producto"
        sql = text(sql)

        db.execute(sql, params)
        db.commit()
        return True

    except IntegrityError as e:
        db.rollback()
        print(f"Error al actualizar producto de factura: {e}")
        if 'for key \'id_factura_producto\'' in str(e.orig):
            raise HTTPException(status_code=400, detail="Error de integridad de datos: El id de id_factura_producto que estás intentando actualizar no existe.")
        raise HTTPException(status_code=400, detail="Error de integridad de datos: Uno o más valores no cumplen con las restricciones del esquema de la base de datos.")
    except SQLAlchemyError as e:
        db.rollback()
        print(f"Error al actualizar producto de factura: {e}")
        raise HTTPException(status_code=500, detail="Error interno del servidor al actualizar el producto de factura.")




    

# Eliminar PRODUCTOS de una factura
def delete_producto_factura(db: Session, id_factura_producto: int):
    try:
        sql = text("DELETE FROM factura_producto WHERE id_factura_producto = :id_factura_producto")
        db.execute(sql, {"id_factura_producto": id_factura_producto})
        db.commit()
        return True
    except IntegrityError as e:
        db.rollback()  # Revertir la transacción en caso de error de integridad (llave foránea)
        print(f"Error al eliminar producto de la factura: {e}")
        raise HTTPException(status_code=400, detail="Error. Integridad de datos al eliminar producto de la factura")
    except SQLAlchemyError as e:
        db.rollback()  
        print(f"Error al eliminar factura: {e}")
        raise HTTPException(status_code=500, detail="Error al eliminar producto de la factura")
    