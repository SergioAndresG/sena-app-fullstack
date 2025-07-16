<!-- components/EditarAprendizModal.vue -->
<template>
    <!-- Este componente no muestra nada directamente -->
</template>

<script setup>
import { ref, watch } from 'vue'
import Swal from 'sweetalert2'

const props = defineProps({
    aprendiz: Object,
    mostrar: Boolean
})
const emit = defineEmits(['cerrar', 'actualizar'])

watch(() => props.aprendiz, async (nuevoAprendiz) => {

    if (!nuevoAprendiz) return;

    const { value: formData } = await Swal.fire({
        title: 'Editar Aprendiz',
        html: `<div class="form-container">
          <div class="form-group">
            <label class="form-label">Documento</label>
            <div class="documento-container">
              <select id="tipo-doc" class="tipo-documento">
                <option value="CC" ${nuevoAprendiz.tipo_documento === 'CC' ? 'selected' : ''}>CC</option>
                <option value="TI" ${nuevoAprendiz.tipo_documento === 'TI' ? 'selected' : ''}>TI</option>
                <option value="CE" ${nuevoAprendiz.tipo_documento === 'CE' ? 'selected' : ''}>CE</option>
                <option value="NUIP" ${nuevoAprendiz.tipo_documento === 'NUIP' ? 'selected' : ''}>NUIP</option>
              </select>
              <input id="numero-doc" class="numero-documento" placeholder="Número de documento" value="${nuevoAprendiz.documento}">
            </div>
          </div>
          
          <div class="form-group">
            <label class="form-label">Nombre</label>
            <input id="nombre" class="swal2-input" placeholder="Ingrese el nombre" value="${nuevoAprendiz.nombre}">
          </div>
          
          <div class="form-group">
            <label class="form-label">Apellidos</label>
            <input id="apellidos" class="swal2-input" placeholder="Ingrese los apellidos" value="${nuevoAprendiz.apellido}">
          </div>
          
          <div class="form-group">
            <label class="form-label">Dirección</label>
            <input id="direccion" class="swal2-input" placeholder="Ingrese la dirección" value="${nuevoAprendiz.direccion || ''}">
          </div>
          
          <div class="form-group">
            <label class="form-label">Correo Electrónico</label>
            <input id="correo" class="swal2-input" placeholder="correo@ejemplo.com" value="${nuevoAprendiz.correo}">
          </div>
          
          <div class="form-group">
            <label class="form-label">Celular</label>
            <input id="celular" class="swal2-input" placeholder="Número de celular" value="${nuevoAprendiz.celular}">
          </div>
          
          <div class="form-group">
            <label class="form-label">¿Tiene alguna discapacidad?</label>
            <div class="checkbox-group">
              <div class="checkbox-item">
                <input type="checkbox" id="discapacidad-si" ${nuevoAprendiz.discapacidad === 'Sí' ? 'checked' : ''}> 
                <label for="discapacidad-si">Sí</label>
              </div>
              <div class="checkbox-item">
                <input type="checkbox" id="discapacidad-no" ${nuevoAprendiz.discapacidad === 'No' ? 'checked' : ''}> 
                <label for="discapacidad-no">No</label>
              </div>
            </div>
          </div>
          
          <div class="form-group">
            <label class="form-label">Firma</label>
            <div class="firma-container">
              <canvas id="firma" width="380" height="150"></canvas>
              <button type="button" id="limpiar-firma" class="btn-limpiar">Limpiar</button>
            </div>
          </div>
        </div>`,
        showCancelButton: true,
        confirmButtonText: 'Guardar',
        cancelButtonText: 'Cancelar',
        width: 500,
        didOpen: () => {
            const canvas = document.getElementById('firma');
            const ctx = canvas.getContext('2d');
            const limpiarBtn = document.getElementById('limpiar-firma');
            let isDrawing = false;

            // Configurar canvas con fondo blanco
            ctx.fillStyle = '#ffffff';
            ctx.fillRect(0, 0, canvas.width, canvas.height);

            // Función para limpiar canvas
            const limpiarCanvas = () => {
                ctx.fillStyle = '#ffffff';
                ctx.fillRect(0, 0, canvas.width, canvas.height);
            };

            limpiarBtn.addEventListener('click', limpiarCanvas);

            // Manejar checkboxes exclusivos
            const checkboxSi = document.getElementById('discapacidad-si');
            const checkboxNo = document.getElementById('discapacidad-no');

            checkboxSi.addEventListener('change', () => {
                if (checkboxSi.checked) checkboxNo.checked = false;
            });

            checkboxNo.addEventListener('change', () => {
                if (checkboxNo.checked) checkboxSi.checked = false;
            });

            // Función para obtener posición del mouse/touch
            const getPosition = (e) => {
                const rect = canvas.getBoundingClientRect();
                const clientX = e.clientX || (e.touches && e.touches[0].clientX);
                const clientY = e.clientY || (e.touches && e.touches[0].clientY);
                return {
                    x: clientX - rect.left,
                    y: clientY - rect.top
                };
            };

            // Función para iniciar dibujo
            const startDrawing = (e) => {
                e.preventDefault();
                isDrawing = true;
                const pos = getPosition(e);
                ctx.beginPath();
                ctx.moveTo(pos.x, pos.y);
            };

            // Función para dibujar
            const draw = (e) => {
                e.preventDefault();
                if (!isDrawing) return;
                
                const pos = getPosition(e);
                ctx.lineWidth = 2;
                ctx.lineCap = 'round';
                ctx.strokeStyle = '#000000';
                ctx.lineTo(pos.x, pos.y);
                ctx.stroke();
                ctx.beginPath();
                ctx.moveTo(pos.x, pos.y);
            };

            // Función para terminar dibujo
            const stopDrawing = (e) => {
                e.preventDefault();
                isDrawing = false;
            };

            // Eventos para mouse
            canvas.addEventListener('mousedown', startDrawing);
            canvas.addEventListener('mousemove', draw);
            canvas.addEventListener('mouseup', stopDrawing);
            canvas.addEventListener('mouseout', stopDrawing);

            // Eventos para touch (móvil)
            canvas.addEventListener('touchstart', startDrawing);
            canvas.addEventListener('touchmove', draw);
            canvas.addEventListener('touchend', stopDrawing);
            canvas.addEventListener('touchcancel', stopDrawing);
        },
        preConfirm: () => {
            const tipo_doc = document.getElementById('tipo-doc').value;
            const numero_documento = document.getElementById('numero-doc').value;
            const nombre = document.getElementById('nombre').value;
            const apellidos = document.getElementById('apellidos').value;
            const direccion = document.getElementById('direccion').value;
            const correo = document.getElementById('correo').value;
            const celular = document.getElementById('celular').value;
            const discapacidad = document.getElementById('discapacidad-si').checked ? 'Sí' : 'No';
            const firma = document.getElementById('firma').toDataURL();

            if (!nombre || !correo) {
                Swal.showValidationMessage('Nombre y correo son obligatorios');
                return false;
            }

            return {
                tipo_documento: tipo_doc,
                numero_documento,
                nombre,
                apellidos,
                direccion,
                correo_electronico: correo,
                celular,
                discapacidad,
                firma
            };
        }
    });

    emit('cerrar');

    if (formData) {
        emit('actualizar', formData);
        Swal.fire('¡Actualizado!', 'Los datos han sido guardados.', 'success');
    }
});
</script>

<style scoped>
:global(.swal2-popup) {
    border-radius: 8px !important;
    font-family: 'Inter', sans-serif;
}

:global(.swal2-title) {
    font-size: 20px !important;
    font-weight: 600 !important;
    color: #333 !important;
}

:global(.form-container) {
    text-align: left;
    padding: 20px 10px;
}

:global(.form-group) {
    margin-bottom: 25px;
}

:global(.form-label) {
    display: block;
    margin-bottom: 8px;
    font-weight: 600;
    color: #333;
    font-size: 14px;
}

:global(.documento-container) {
    position: relative;
    display: flex;
    align-items: stretch;
}

:global(.tipo-documento) {
    position: absolute;
    left: 0;
    top: 0;
    z-index: 10;
    width: 80px !important;
    height: 42px !important;
    padding: 8px 6px !important;
    border: 1px solid #ddd !important;
    border-radius: 4px 0 0 4px !important;
    background-color: #f8f9fa !important;
    font-size: 12px !important;
    font-weight: 500 !important;
    color: #495057 !important;
    appearance: none !important;
    background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' fill='none' viewBox='0 0 20 20'%3e%3cpath stroke='%236b7280' stroke-linecap='round' stroke-linejoin='round' stroke-width='1.5' d='M6 8l4 4 4-4'/%3e%3c/svg%3e") !important;
    background-position: right 4px center !important;
    background-repeat: no-repeat !important;
    background-size: 12px !important;
    cursor: pointer !important;
    margin: 0 !important;
}

:global(.numero-documento) {
    width: 100% !important;
    padding: 8px 12px 8px 90px !important;
    border: 1px solid #ddd !important;
    border-radius: 4px !important;
    font-size: 14px !important;
    height: 42px !important;
    box-sizing: border-box !important;
    margin: 0 !important;
}

:global(.swal2-input) {
    width: 100% !important;
    padding: 12px 15px !important;
    border: 1px solid #ddd !important;
    border-radius: 4px !important;
    font-size: 14px !important;
    height: 42px !important;
    box-sizing: border-box !important;
    margin: 0 !important;
    transition: border-color 0.3s ease !important;
}

:global(.swal2-input:focus) {
    outline: none !important;
    border-color: #007bff !important;
    box-shadow: 0 0 0 2px rgba(0, 123, 255, 0.25) !important;
}

:global(.checkbox-group) {
    display: flex;
    gap: 20px;
    margin-top: 8px;
}

:global(.checkbox-item) {
    display: flex;
    align-items: center;
    gap: 8px;
}

:global(.checkbox-item input[type="checkbox"]) {
    width: 18px !important;
    height: 18px !important;
    margin: 0 !important;
    cursor: pointer !important;
}

:global(.checkbox-item label) {
    font-size: 14px !important;
    color: #333 !important;
    cursor: pointer !important;
    margin: 0 !important;
    font-weight: normal !important;
}

:global(.firma-container) {
    position: relative;
    border: 2px dashed #ddd;
    border-radius: 8px;
    padding: 15px;
    background-color: #fafafa;
    text-align: center;
}

:global(#firma) {
    border: 1px solid #ccc;
    border-radius: 4px;
    background-color: white;
    cursor: crosshair;
    display: block;
    margin: 0 auto;
}

:global(.btn-limpiar) {
    margin-top: 10px;
    padding: 6px 12px;
    background-color: #dc3545;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 12px;
    transition: background-color 0.3s ease;
}

:global(.btn-limpiar:hover) {
    background-color: #c82333;
}
</style>