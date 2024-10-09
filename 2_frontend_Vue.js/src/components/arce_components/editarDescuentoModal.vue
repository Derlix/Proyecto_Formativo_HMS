<script setup>
import CardBox from '@/components/CardBox.vue';
import { defineProps, defineEmits } from 'vue';

const props = defineProps(['visible', 'form']);
const emit = defineEmits(['update:visible', 'save']);

const close = () => {
    emit('update:visible', false);
};

const submitForm = () => {
    emit('save', { ...props.form });
    close();
};
</script>

<template>
    <div v-if="visible" class="modal-overlay">
        <CardBox class="modal">
            <h3 class="modal-title">Editar Descuento</h3>
            <form @submit.prevent="submitForm">
                <div class="form-group">
                    <label for="tipo_descuento">Tipo de Descuento:</label>
                    <input
                        id="tipo_descuento"
                        v-model="form.tipo_descuento"
                        type="text"
                        required
                        class="form-input"
                    />
                </div>
                <div class="form-group">
                    <label for="porcentaje_descuento">Porcentaje de Descuento:</label>
                    <input
                        id="porcentaje_descuento"
                        v-model.number="form.porcentaje_descuento"
                        type="number"
                        required
                        class="form-input"
                    />
                </div>
                <div class="modal-buttons">
                    <button type="submit" class="btn btn-save">Guardar Cambios</button>
                    <button type="button" @click="close" class="btn btn-cancel">Cancelar</button>
                </div>
            </form>
        </CardBox>
    </div>
</template>

<style>
.modal-overlay {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
}

.modal {
    background: white;
    padding: 20px;
    border-radius: 8px;
    max-width: 400px;
    width: 100%;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.modal-title {
    margin-bottom: 20px;
    font-size: 1.5rem;
    text-align: center;
}

.form-group {
    margin-bottom: 15px;
}

.form-input {
    width: 100%;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

.modal-buttons {
    display: flex;
    justify-content: space-between;
}

.btn {
    padding: 10px 15px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

.btn-save {
    background-color: #28a745;
    color: white;
}

.btn-cancel {
    background-color: #dc3545;
    color: white;
}
</style>
