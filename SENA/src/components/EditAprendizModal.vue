<template>
    <!-- Este componente no muestra nada directamente -->
</template>

<script setup lang="ts">
import {  ref, watch } from 'vue'
import axios from 'axios';
import Swal from 'sweetalert2';
import SignaturePad from "signature_pad";

let signaturePad: SignaturePad;

interface Aprendiz {
    tipo_documento: string;
    documento: string;
    nombre: string;
    apellido: string;
    direccion?: string;
    departamento?: string;
    municipio?: string,
    correo: string;
    celular: string;
    discapacidad?: "Si" | "No";
    tipo_discapacidad?: string;
    firma?: string;
}

async function envioDatosAprendiz(aprendiz) {
    try {
        const response = await axios.patch(`http://127.0.0.1:8000/aprendices/${aprendiz.documento}`, {
            tipo_documento: aprendiz.tipo_documento,
            documento: aprendiz.documento,
            nombre: aprendiz.nombre,
            apellido: aprendiz.apellido,
            direccion: aprendiz.direccion,
            departamento: aprendiz.departamento,
            municipio: aprendiz.municipio,
            correo: aprendiz.correo,
            celular: aprendiz.celular,
            discapacidad: aprendiz.discapacidad,
            tipo_discapacidad: aprendiz.tipo_discapacidad,
            firma: aprendiz.firma
        });

        Swal.fire({
            icon: 'success',
            title: 'Editado Correctamente',
            timer: 1500,
            showConfirmButton: false,
            // SOLUCIÓN: Configuraciones para prevenir el desplazamiento
            scrollbarPadding: false,
            heightAuto: false,
            didOpen: () => {
                // Restaurar el estado normal del body
                document.body.style.paddingRight = '';
                document.body.style.overflow = '';
            }
        });

    } catch (error) {
        Swal.fire({
            icon: 'error',
            title: 'Error al editar',
            text: 'Intente nuevamente',
            showConfirmButton: true,
            // SOLUCIÓN: Aplicar la misma configuración
            scrollbarPadding: false,
            heightAuto: false,
            didOpen: () => {
                document.body.style.paddingRight = '';
                document.body.style.overflow = '';
            }
        })
    }
}

const props = defineProps<{
    aprendiz: Aprendiz | null;
    mostrar: boolean;
}>()

const emit = defineEmits<{
    (e: 'cerrar'): void;
    (e: 'actualizar', payload: Aprendiz): void;
}>()

watch(() => props.aprendiz, async (nuevoAprendiz) => {
    if (!nuevoAprendiz) return;

    const esIndividual = (nuevoAprendiz as any).modalidad === 'individual';

    const { value: formData } = await Swal.fire({
        title: 'Editar Aprendiz',
        html: `
        <div class="custom-modal-content">
        <div class="form-grid">
            <!-- Documento -->
            <div class="form-field full-width">
            <label class="field-label">Documento</label>
            <div class="document-input-group">
                <select id="tipo-doc" class="document-type-select">
                <option value="CC" ${nuevoAprendiz.tipo_documento === 'CC' ? 'selected' : ''}>CC</option>
                <option value="TI" ${nuevoAprendiz.tipo_documento === 'TI' ? 'selected' : ''}>TI</option>
                <option value="CE" ${nuevoAprendiz.tipo_documento === 'CE' ? 'selected' : ''}>CE</option>
                <option value="NUIP" ${nuevoAprendiz.tipo_documento === 'NUIP' ? 'selected' : ''}>NUIP</option>
                </select>
                <input id="numero-doc" class="document-number-input" placeholder="Número de documento" value="${nuevoAprendiz.documento}">
            </div>
            </div>
            
            <!-- Nombre y Apellidos -->
            <div class="form-field">
            <label class="field-label">Nombre</label>
            <input id="nombre" class="form-input" placeholder="Ingrese el nombre" value="${nuevoAprendiz.nombre}">
            </div>
            
            <div class="form-field">
            <label class="field-label">Apellidos</label>
            <input id="apellidos" class="form-input" placeholder="Ingrese los apellidos" value="${nuevoAprendiz.apellido}">
            </div>
            
            <!-- Dirección -->
            <div class="form-field full-width">
            <label class="field-label">Dirección</label>
            <input id="direccion" class="form-input" placeholder="Ingrese la dirección" value="${nuevoAprendiz.direccion || ''}">
            </div>

            <!-- Inputs que solo aparecen si es modalidad individual -->
            <div class="form-field" style="display: ${esIndividual ? 'block' : 'none'}">
                <label class="field-label">Departamento</label>
                <input id="departamento" class="form-input" placeholder="Ingrese el departamento" value="${nuevoAprendiz.departamento || ''}">
            </div>

            <div class="form-field" style="display: ${esIndividual ? 'block' : 'none'}">
                <label class="field-label">Municipio</label>
                <input id="municipio" class="form-input" placeholder="Ingrese el municipio" value="${nuevoAprendiz.municipio || ''}">
            </div>

            <!-- Correo y Celular -->
            <div class="form-field">
            <label class="field-label">Correo Electrónico</label>
            <input id="correo" class="form-input" type="email" placeholder="correo@ejemplo.com" value="${nuevoAprendiz.correo}">
            </div>
            
            <div class="form-field">
            <label class="field-label">Celular</label>
            <input id="celular" class="form-input" placeholder="Número de celular" value="${nuevoAprendiz.celular}">
            </div>
            
            <!-- Discapacidad -->
            <div class="form-field full-width">
            <label class="field-label">¿Tiene alguna discapacidad?</label>
            <div class="radio-group">
                <label class="radio-option">
                <input type="radio" name="discapacidad" id="discapacidad-si" value="Si" ${nuevoAprendiz.discapacidad === 'Si' ? 'checked' : ''}> 
                <span class="radio-label">Sí</span>
                </label>
                <label class="radio-option">
                <input type="radio" name="discapacidad" id="discapacidad-no" value="No" ${nuevoAprendiz.discapacidad === 'No' ? 'checked' : ''}> 
                <span class="radio-label">No</span>
                </label>
            </div>
            
            <div id="detalle-discapacidad" class="disability-detail" style="display: ${nuevoAprendiz.discapacidad === 'Si' ? 'block' : 'none'}">
                <label class="field-label">¿Cuál es la situación de discapacidad que presenta?</label>
                <input id="tipo-disc" class="form-input" placeholder="Ingrese el tipo de discapacidad" value="${nuevoAprendiz.tipo_discapacidad || ''}">
                <p class="help-text">Recuerde que debe anexar su certificado de discapacidad emitido por la EPS</p>
            </div>
            </div>

            <!-- Firma -->
            <div class="form-field full-width">
            <label class="field-label">Firma</label>
            <div class="signature-container">
                <canvas id="firma"></canvas>
                <button type="button" id="limpiar-firma" class="clear-btn">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M3 6h18M8 6V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2m3 0v14a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V6h3"/>
                    <line x1="10" y1="11" x2="10" y2="17"/>
                    <line x1="14" y1="11" x2="14" y2="17"/>
                </svg>
                Limpiar firma
                </button>
            </div>
            </div>
        </div>
        </div>`,
        showCancelButton: true,
        confirmButtonText: 'Guardar cambios',
        cancelButtonText: 'Cancelar',
        width: 600,
        
        // *** SOLUCIÓN PRINCIPAL ***
        // Estas configuraciones previenen el desplazamiento del contenido
        scrollbarPadding: false,  // No ajustar padding por scrollbar
        heightAuto: false,        // No ajustar altura automáticamente
        allowOutsideClick: true,  // Permitir click fuera del modal
        
        customClass: {
            popup: 'custom-swal-popup',
            title: 'custom-swal-title',
            htmlContainer: 'custom-swal-content',
            confirmButton: 'custom-confirm-btn',
            cancelButton: 'custom-cancel-btn',
            container: 'no-shift-container'  // Nueva clase CSS
        },
        
        willOpen: () => {
            // Guardar estado original del body
            const originalOverflow = document.body.style.overflow;
            const originalPaddingRight = document.body.style.paddingRight;
            
            // Aplicar inmediatamente para prevenir shift
            document.body.style.overflow = '';
            document.body.style.paddingRight = '';
        },
        
        didOpen: () => {
            const canvas = document.getElementById('firma') as HTMLCanvasElement;
            const limpiarBtn = document.getElementById('limpiar-firma') as HTMLButtonElement | null;

            if (!canvas || !limpiarBtn) return;

            function resizeCanvas() {
                // Usar devicePixelRatio más alto para mejor calidad
                const ratio = Math.max(window.devicePixelRatio || 1, 2); // Mínimo 2x
                const rect = canvas.getBoundingClientRect();
                
                // Dimensiones base más grandes para mejor resolución final
                const baseWidth = Math.max(rect.width, 400); // Ancho mínimo de 400px
                const baseHeight = Math.max(150, 200); // Alto mínimo de 200px
                
                canvas.width = baseWidth * ratio;
                canvas.height = baseHeight * ratio;
                
                // Aplicar el escalado al contexto
                const ctx = canvas.getContext("2d");
                if (ctx) {
                    ctx.scale(ratio, ratio);
                    // Mejorar la calidad del renderizado
                    ctx.lineCap = 'round';
                    ctx.lineJoin = 'round';
                    ctx.imageSmoothingEnabled = true;
                    ctx.imageSmoothingQuality = 'high';
                }
                
                // Mantener el tamaño visual del canvas
                canvas.style.width = baseWidth + 'px';
                canvas.style.height = baseHeight + 'px';
            }

            window.addEventListener("resize", resizeCanvas);
            resizeCanvas();

            signaturePad = new SignaturePad(canvas, {
                penColor: "black",
                backgroundColor: "white",
                minWidth: 0.8,  // Líneas más finas para mejor definición
                maxWidth: 3.5,  // Máximo un poco más alto
                throttle: 0,    // Sin throttle para capturar más puntos
                minDistance: 0.3, // Distancia mínima reducida para más suavidad
                velocityFilterWeight: 0.1, // Filtro de velocidad para líneas más suaves
                dotSize: 1.5    // Tamaño de puntos para mejor definición
            });

            // 🔘 Manejo radio buttons (sin cambios)
            const radioSi = document.getElementById('discapacidad-si') as HTMLInputElement;
            const radioNo = document.getElementById('discapacidad-no') as HTMLInputElement;
            const detalleDiscapacidad = document.getElementById('detalle-discapacidad');

            const toggleDiscapacidadDetail = () => {
                detalleDiscapacidad.style.display = radioSi.checked ? 'block' : 'none';
            };

            radioSi.addEventListener('change', toggleDiscapacidadDetail);
            radioNo.addEventListener('change', toggleDiscapacidadDetail);

            limpiarBtn.addEventListener("click", () => {
                signaturePad.clear();
            });

            // 🔥 Función mejorada para exportar firma en ultra alta calidad
            (window as any).exportFirma = () => {
                if (signaturePad.isEmpty()) return null;
                
                // Escala muy alta para PDF de calidad profesional
                const exportScale = 10; // Escala 10x para máxima calidad
                const originalCanvas = canvas;
                
                // Crear canvas temporal de alta resolución
                const tempCanvas = document.createElement("canvas");
                const tempCtx = tempCanvas.getContext("2d")!;
                
                // Dimensiones finales muy altas
                tempCanvas.width = originalCanvas.width * exportScale;
                tempCanvas.height = originalCanvas.height * exportScale;
                
                // Configurar contexto para máxima calidad
                tempCtx.imageSmoothingEnabled = true;
                tempCtx.imageSmoothingQuality = "high";
                tempCtx.scale(exportScale, exportScale);
                
                // Fondo blanco para mejor contraste en PDF
                tempCtx.fillStyle = "white";
                tempCtx.fillRect(0, 0, originalCanvas.width, originalCanvas.height);
                
                // Dibujar la firma escalada
                tempCtx.drawImage(originalCanvas, 0, 0);
                
                // Exportar como PNG de alta calidad
                return tempCanvas.toDataURL("image/png", 1.0); // Calidad máxima
            };
        },

        didClose: () => {
            // Asegurar que el body vuelva a la normalidad
            document.body.style.paddingRight = '';
            document.body.style.overflow = '';
            document.body.classList.remove('swal2-shown');
        },
        
        preConfirm: () => {
            const tipo_doc = document.getElementById('tipo-doc') as HTMLSelectElement;
            const documento = document.getElementById('numero-doc') as HTMLInputElement;
            const nombre = document.getElementById('nombre') as HTMLInputElement;
            const apellido = document.getElementById('apellidos') as HTMLInputElement;
            const direccion = document.getElementById('direccion') as HTMLInputElement;
            // Solo leemos depto/municipio si es individual; si no, los dejamos vacíos
            const departamentoEl = esIndividual ? document.getElementById('departamento') as HTMLInputElement : null;
            const municipioEl = esIndividual ? document.getElementById('municipio') as HTMLInputElement : null;
            const correo = document.getElementById('correo') as HTMLInputElement;
            const celular = document.getElementById('celular') as HTMLInputElement;
            const discapacidadSi = document.getElementById('discapacidad-si') as HTMLInputElement;
            const discapacidad = discapacidadSi.checked ? 'Si' : 'No';
            const tipo_discapacidad = document.getElementById('tipo-disc') as HTMLInputElement;
            // 📋 Uso mejorado al obtener los datos
            const firmaData = signaturePad.isEmpty()
                ? null
                : (window as any).exportFirma(); // Para PNG de alta calidad

            if (!nombre.value.trim() || !correo.value.trim()) {
                Swal.showValidationMessage('Nombre y correo son obligatorios');
                return false;
            }

            if (discapacidad === 'Si' && !tipo_discapacidad.value.trim()) {
                Swal.showValidationMessage('Debe especificar el tipo de discapacidad');
                return false;
            }

            return {
                tipo_documento: tipo_doc.value,
                documento: documento.value,
                nombre: nombre.value.trim(),
                apellido: apellido.value.trim(),
                direccion: direccion.value.trim(),
                // si no es individual, mandamos vacío
                departamento: esIndividual ? (departamentoEl?.value.trim() || '') : '',
                municipio: esIndividual ? (municipioEl?.value.trim() || '') : '',
                correo: correo.value.trim(),
                celular: celular.value.trim(),
                discapacidad: discapacidad,
                tipo_discapacidad: discapacidad === 'Si' ? tipo_discapacidad.value.trim() : null,
                firma: firmaData
            };

        }
    });

    emit('cerrar');

    if (formData) {
        emit('actualizar', formData);
        envioDatosAprendiz(formData);
    }
});
</script>
<style scoped>

/* ✅ PREVENCIÓN DEL DESPLAZAMIENTO LATERAL */
:global(body.swal2-shown) {
    padding-right: 0 !important;
    overflow-x: hidden !important;
}

:global(.swal2-container) {
    padding-left: 0 !important;
    padding-right: 0 !important;
}

:global(.swal2-popup) {
    margin-left: auto !important;
    margin-right: auto !important;
}

/* Estilos globales para el modal */
:global(.custom-swal-popup) {
    border-radius: 12px !important;
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif !important;
    box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25) !important;
    padding: 0 !important;

}

:global(.custom-swal-title) {
    font-size: 24px !important;
    font-weight: 600 !important;
    color: #1f2937 !important;
    margin-bottom: 24px !important;
    padding: 24px 24px 0 24px !important;
}

:global(.custom-swal-content) {
    padding: 0 24px 24px 24px !important;
    margin: 0 !important;
    overflow-x: hidden !important;
}

/* Contenedor principal del formulario */
:global(.custom-modal-content) {
    width: 100%;
    max-width: none;
    box-sizing: border-box !important;
}

/* Grid del formulario - OPTIMIZADO */
:global(.form-grid) {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 20px;
    align-items: start;
    width: 100% !important;
    max-width: 100% !important;
    box-sizing: border-box !important;
}

:global(.form-field) {
    display: flex;
    flex-direction: column;
    min-width: 0 !important;
    box-sizing: border-box !important;
}

:global(.form-field.full-width) {
    grid-column: 1 / -1;
}

/* Etiquetas */
:global(.field-label) {
    font-size: 14px;
    font-weight: 600;
    color: #374151;
    margin-bottom: 8px;
    display: block;
}

/* Inputs generales - OPTIMIZADOS */
:global(.form-input) {
    width: 100% !important;
    padding: 12px 16px !important;
    border: 2px solid #e5e7eb !important;
    border-radius: 8px !important;
    font-size: 14px !important;
    font-family: inherit !important;
    transition: all 0.2s ease !important;
    background-color: #ffffff !important;
    box-sizing: border-box !important;
    margin: 0 !important;
    /* ✅ Prevenir overflow en inputs */
    min-width: 0 !important;
    max-width: 100% !important;
}

:global(.form-input:focus) {
    outline: none !important;
    border-color: #3b82f6 !important;
    box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1) !important;
}

:global(.form-input:hover) {
    border-color: #d1d5db !important;
}

/* Grupo de documento - MEJORADO */
:global(.document-input-group) {
    display: flex;
    position: relative;
    width: 100%;
    max-width: 100% !important;
    box-sizing: border-box !important;
}

:global(.document-type-select) {
    width: 90px !important;
    min-width: 80px !important;
    max-width: 100px !important;
    padding: 12px 8px !important;
    border: 2px solid #e5e7eb !important;
    border-right: none !important;
    border-radius: 8px 0 0 8px !important;
    background-color: #f9fafb !important;
    font-size: 13px !important;
    font-weight: 500 !important;
    color: #374151 !important;
    cursor: pointer !important;
    appearance: none !important;
    background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' fill='none' viewBox='0 0 20 20'%3e%3cpath stroke='%236b7280' stroke-linecap='round' stroke-linejoin='round' stroke-width='1.5' d='M6 8l4 4 4-4'/%3e%3c/svg%3e") !important;
    background-position: right 6px center !important;
    background-repeat: no-repeat !important;
    background-size: 12px !important;
    margin: 0 !important;
    box-sizing: border-box !important;
}

:global(.document-number-input) {
    flex: 1 !important;
    /* ✅ Asegurar que no cause overflow */
    min-width: 0 !important;
    padding: 12px 16px !important;
    border: 2px solid #e5e7eb !important;
    border-left: none !important;
    border-radius: 0 8px 8px 0 !important;
    font-size: 14px !important;
    transition: all 0.2s ease !important;
    margin: 0 !important;
    box-sizing: border-box !important;
}

:global(.document-input-group:focus-within .document-type-select) {
    border-color: #3b82f6 !important;
}

:global(.document-input-group:focus-within .document-number-input) {
    border-color: #3b82f6 !important;
    box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1) !important;
}

/* Radio buttons para discapacidad */
:global(.radio-group) {
    display: flex;
    gap: 24px;
    margin-top: 8px;
    /* ✅ Hacer flexible en pantallas pequeñas */
    flex-wrap: wrap !important;
}

:global(.radio-option) {
    display: flex;
    align-items: center;
    gap: 8px;
    cursor: pointer;
    font-size: 14px;
    color: #374151;
    font-weight: 500;
    /* ✅ Prevenir que se rompan */
    flex-shrink: 0 !important;
}

:global(.radio-option input[type="radio"]) {
    width: 18px !important;
    height: 18px !important;
    margin: 0 !important;
    cursor: pointer !important;
    accent-color: #3b82f6 !important;
    flex-shrink: 0 !important;
}

:global(.radio-label) {
    cursor: pointer;
    user-select: none;
    white-space: nowrap;
}

/* Detalle de discapacidad */
:global(.disability-detail) {
    margin-top: 16px;
    padding-top: 16px;
    border-top: 1px solid #e5e7eb;
    animation: slideDown 0.3s ease;
}

:global(.help-text) {
    font-size: 12px;
    color: #6b7280;
    margin-top: 8px;
    margin-bottom: 0;
    font-style: italic;
    /* ✅ Permitir que el texto se ajuste */
    word-wrap: break-word !important;
    line-height: 1.4 !important;
}

/* Contenedor de firma - OPTIMIZADO */
:global(.signature-container) {
    border: 2px dashed #d1d5db;
    border-radius: 12px;
    padding: 20px;
    background-color: #f9fafb;
    text-align: center;
    position: relative;
    /* ✅ Asegurar que no cause overflow */
    width: 100% !important;
    box-sizing: border-box !important;
}

:global(#firma) {
    border: 2px solid #e5e7eb;
    border-radius: 8px;
    background-color: #ffffff;
    cursor: crosshair;
    display: block;
    margin: 0 auto 16px auto;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
    /* ✅ Hacer el canvas responsivo */
    width: 100%;     /* ocupa todo el ancho del contenedor */
    height: 150px;
}

:global(.clear-btn) {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 8px 16px;
    background-color: #ef4444;
    color: #ffffff;
    border: none;
    border-radius: 6px;
    cursor: pointer;
    font-size: 13px;
    font-weight: 500;
    transition: all 0.2s ease;
}

:global(.clear-btn:hover) {
    background-color: #dc2626;
    transform: translateY(-1px);
    box-shadow: 0 4px 12px rgba(239, 68, 68, 0.3);
}

:global(.clear-btn svg) {
    width: 14px;
    height: 14px;
}

/* Botones del modal */
:global(.custom-confirm-btn) {
    background-color: #3b82f6 !important;
    border-color: #3b82f6 !important;
    border-radius: 8px !important;
    padding: 12px 24px !important;
    font-weight: 600 !important;
    transition: all 0.2s ease !important;
}

:global(.custom-confirm-btn:hover) {
    background-color: #2563eb !important;
    border-color: #2563eb !important;
    transform: translateY(-1px) !important;
    box-shadow: 0 4px 12px rgba(59, 130, 246, 0.3) !important;
}

:global(.custom-cancel-btn) {
    background-color: #6b7280 !important;
    border-color: #6b7280 !important;
    border-radius: 8px !important;
    padding: 12px 24px !important;
    font-weight: 600 !important;
    transition: all 0.2s ease !important;
}

:global(.custom-cancel-btn:hover) {
    background-color: #4b5563 !important;
    border-color: #4b5563 !important;
    transform: translateY(-1px) !important;
}

/* Animación para el detalle de discapacidad */
@keyframes slideDown {
    from {
        opacity: 0;
        transform: translateY(-10px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

/* Responsive - MEJORADO */
@media (max-width: 640px) {
    :global(.custom-swal-popup) {
        width: 95% !important;
        max-width: 95% !important;
        margin: 10px !important;
        /* ✅ Asegurar centrado en móvil */
        left: 50% !important;
        transform: translateX(-50%) !important;
    }
    
    :global(.custom-swal-title) {
        font-size: 20px !important;
        padding: 20px 16px 0 16px !important;
    }
    
    :global(.custom-swal-content) {
        padding: 0 16px 20px 16px !important;
    }
    
    :global(.form-grid) {
        grid-template-columns: 1fr !important;
        gap: 16px !important;
    }
    
    :global(.radio-group) {
        flex-direction: column !important;
        gap: 12px !important;
        align-items: flex-start !important;
    }
    
    :global(.signature-container) {
        padding: 16px !important;
    }
    
    :global(#firma) {
        width: 100% !important;
        max-width: 100% !important;
        height: 100px !important;
    }
    
    :global(.document-type-select) {
        width: 70px !important;
        min-width: 60px !important;
        font-size: 11px !important;
        padding: 12px 4px !important;
    }
}

@media (max-width: 480px) {
    :global(.custom-swal-popup) {
        width: 98% !important;
        max-width: 98% !important;
        margin: 5px !important;
    }
    
    :global(.form-input) {
        font-size: 16px !important; /* ✅ Prevenir zoom en iOS */
    }
    
    :global(.document-number-input) {
        font-size: 16px !important; /* ✅ Prevenir zoom en iOS */
    }
    
    :global(.help-text) {
        font-size: 11px !important;
    }
}

/* ✅ ESTILOS ADICIONALES PARA PREVENIR SCROLL HORIZONTAL */
:global(.swal2-container.swal2-backdrop-show) {
    overflow-x: hidden !important;
}

:global(.swal2-html-container) {
    overflow-x: hidden !important;
    word-wrap: break-word !important;
}
</style>