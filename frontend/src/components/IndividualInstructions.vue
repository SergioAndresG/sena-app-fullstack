<!-- src/components/ModalInstrucciones.vue -->
<template>
    <div class="modal-overlay" @click.self="$emit('cerrar')">
        <div class="modal">
            <!-- Header del modal -->
            <div class="modal-header">
                <h1 class="title-gi">
                    <span class="icon">📋</span>
                    INSTRUCCIONES PARA EL DILIGENCIAMIENTO DEL FORMATO INDIVIDUAL
                </h1>
                <button @click="$emit('cerrar')" class="close-button" aria-label="Cerrar modal">
                    ×
                </button>
            </div>

            <!-- Contenido scrolleable -->
            <div class="modal-content">
                <div class="content-wrapper">
                    
                    <div class="section-header">
                        <h2>1. Generalidades</h2>
                    </div>

                    <div class="instructions-list">
                        <div class="instruction-item classification-note">
                            <div class="instruction-content">
                                <strong>CLASIFICACIÓN DE LA INFORMACIÓN:</strong> Marque con una equis (X) la
                                clasificación del
                                documento según los lineamientos establecidos en la GOR-G-015 Guía Etiquetado de
                                Información, que puede
                                ser consultada en la herramienta de gestión del SIGA.
                                <br><br>
                                <em>Importante:</em> solo se debe clasificar la información cuando se diligencie el
                                formato, por si el
                                formato vacío no contiene información por ende no se etiqueta.
                            </div>
                        </div>

                        <div class="instruction-item">
                            <div class="instruction-label">a)</div>
                            <div class="instruction-content">
                                El formato tiene como objetivo que la persona con rol de aprendiz realice la selección o
                                modificación de la alternativa en forma individual.
                            </div>
                        </div>

                        <div class="instruction-item">
                            <div class="instruction-label">b)</div>
                            <div class="instruction-content">
                                Este formato está directamente relacionado con la GFPI-G-040 Guía desarrollo etapa
                                productiva, se ubica dentro del GFPI-P-006 Proceso ejecución de la formación.
                            </div>
                        </div>

                        <div class="instruction-item">
                            <div class="instruction-label">c)</div>
                            <div class="instruction-content">
                                Persona con rol de aprendiz es responsable de diligenciar el presente formato.
                            </div>
                        </div>

                        <div class="instruction-item">
                            <div class="instruction-label">d)</div>
                            <div class="instruction-content">
                                Este formato podrá ser diligenciado para seleccionar o modificar la alternativa de etapa
                                productiva. Una vez diligenciado debe ser entregado a la coordinación académica en
                                formato físico o digital según las indicaciones brindadas por esta para su aval.
                            </div>
                        </div>

                        <div class="instruction-item">
                            <div class="instruction-label">e)</div>
                            <div class="instruction-content">
                                Solo imprimir el formato en caso de ser requerido.
                            </div>
                        </div>

                        <div class="instruction-item">
                            <div class="instruction-label">f)</div>
                            <div class="instruction-content">
                                La coordinación académica del centro de formación tiene a su cargo la custodia del
                                formato.
                            </div>
                        </div>

                        <div class="instruction-item">
                            <div class="instruction-label">g)</div>
                            <div class="instruction-content">
                                En caso de considerarse pertinente la coordinación de formación salvaguardará el
                                formato.
                            </div>
                        </div>
                    </div>
                </div>

                <div class="content-wrapper">
                    <div class="section-header">
                        <h2>2. Instrucciones para diligenciar las casillas</h2>
                    </div>
                    <table>
                        <colgroup>
                            <col style="width: 20%;">
                            <col style="width: 44%;">
                            <col style="width: 20%;">
                        </colgroup>
                        <thead>
                            <tr>
                                <th>NOMBRE DE LA CASILLA</th>
                                <th>INSTRUCCIONES</th>
                                <th>TENER EN CUENTA</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>
                                    Fecha de solicitud:
                                </td>
                                <td>
                                    Registrar la fecha en que se hace la solicitud de selección o modificación de la
                                    alternativa.
                                </td>
                                <td></td>
                            </tr>
                            <tr>
                                <td>
                                    Tipo de documento de identificación
                                </td>
                                <td>
                                    Indicar el tipo de documento de identidad de la persona con rol de aprendiz (ej. CC,
                                    TI, etc.).
                                </td>
                                <td></td>
                            </tr>
                            <tr>
                                <td>
                                    Número de identificación
                                </td>
                                <td>
                                    Registrar el número de identificación acorde al tipo de documento sin comas o puntos
                                </td>
                                <td></td>
                            </tr>
                            <tr>
                                <td>
                                    Nombres
                                </td>
                                <td>
                                    Ingresar el nombre completo de la persona con rol de aprendiz.
                                </td>
                                <td></td>
                            </tr>
                            <tr>
                                <td>
                                    Apellidos
                                </td>
                                <td>
                                    Especificar los apellidos completos de la persona con rol de aprendiz
                                </td>
                                <td></td>
                            </tr>
                            <tr>
                                <td>
                                    Teléfono
                                </td>
                                <td>
                                    Ingresar el número de teléfono de contacto de la persona con rol de aprendiz.
                                </td>
                                <td></td>
                            </tr>
                            <tr>
                                <td>
                                    Correo electrónico
                                </td>
                                <td>
                                    Especificar el correo electrónico de la persona con rol de aprendiz.
                                </td>
                                <td></td>
                            </tr>
                            <tr>
                                <td>
                                    Dirección de residencia
                                </td>
                                <td>
                                    Ingresar la dirección de residencia de la persona con rol de aprendiz.
                                </td>
                                <td></td>
                            </tr>
                            <tr>
                                <td>
                                    Departamento
                                </td>
                                <td>
                                    Ingresar el departamento donde reside la persona con rol de aprendiz.
                                </td>
                                <td></td>
                            </tr>
                            <tr>
                                <td>
                                    Ciudad
                                </td>
                                <td>
                                    Ingresar la Ciudad o Municipio donde reside la persona con rol de aprendiz.
                                </td>
                                <td></td>
                            </tr>
                            <tr>
                                <td>
                                    Persona en situación de discapacidad
                                </td>
                                <td>
                                    Indique "Sí" o "No", según corresponda, si la persona con rol de aprendiz presenta
                                    alguna condición de discapacidad.
                                </td>
                                <td></td>
                            </tr>
                            <tr>
                                <td>
                                    ¿ Cuál es la situación de discapacidad que presenta?
                                </td>
                                <td>
                                    En caso afirmativo en la anterior casilla, especificar el tipo de discapacidad
                                    (visual, auditiva, física, cognitiva, etc.).
                                </td>
                                <td></td>
                            </tr>
                            <tr>
                                <td colspan="3" style="text-align: center;">
                                    <strong>2. Información académica</strong>
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    Código / Nombre de Regional:
                                </td>
                                <td>
                                    Indicar el nombre de la regional a la que pertenece el centro de formación junto con
                                    el código.
                                </td>
                                <td></td>
                            </tr>
                            <tr>
                                <td>
                                    Código / Nombre centro de formación:
                                </td>
                                <td>
                                    Especificar el código y el nombre del centro de formación.
                                </td>
                                <td></td>
                            </tr>
                            <tr>
                                <td>
                                    Fecha inicio Grupo - ficha:
                                </td>
                                <td>
                                    Indicar la fecha de inicio de la etapa lectiva registrada en SOFIAPlus, en formato
                                    (DD/MM/AAAA).
                                </td>
                                <td></td>
                            </tr>
                            <tr>
                                <td>
                                    Fecha inicio etapa productiva:
                                </td>
                                <td>
                                    Registrar fecha de inicio de la etapa productiva registrada en SOFIAPlus, en formato
                                    (DD/MM/AAAA).
                                </td>
                                <td></td>
                            </tr>
                            <tr>
                                <td>
                                    Nivel y programa de formación:
                                </td>
                                <td>
                                    Ingresar el nombre completo del programa de formación (ej. "Tecnólogo en Gestión de
                                    Mercados")
                                </td>
                                <td></td>
                            </tr>
                            <tr>
                                <td>
                                    Modalidad de formación:
                                </td>
                                <td>
                                    Especificar la modalidad en la que se desarrolla la formación (Presencial, virtual o
                                    a distancia).
                                </td>
                                <td></td>
                            </tr>
                            <tr>
                                <td>
                                    Jornada:
                                </td>
                                <td>
                                    Especificar la jornada a la que pertenece el grupo - ficha (ej. Mañana, tarde,
                                    nocturna, fin de semana- mañana, fin de semana - nocturna).
                                </td>
                                <td></td>
                            </tr>
                            <tr>
                                <td>
                                    Fecha fin del Grupo - ficha:
                                </td>
                                <td>
                                    Ingresar la fecha en la que finaliza el grupo -ficha, en formato (DD/MM/AAAA).
                                </td>
                                <td></td>
                            </tr>
                            <tr>
                                <td>
                                    Marque con una X el tipo de solicitud
                                </td>
                                <td>
                                    Con una equis (X), indique si la solicitud es de; Selección de alternativa o
                                    Modificación de alternativa
                                </td>
                                <td></td>
                            </tr>
                            <tr>
                                <td>
                                    Fecha inicio etapa productiva:
                                </td>
                                <td>
                                    Registrar fecha en que tiene concertado el inicio de su etapa productiva con el ente
                                    coformador, en formato (DD/MM/AAAA).
                                </td>
                                <td></td>
                            </tr>
                            <tr>
                                <td>
                                    Fecha fin etapa productiva:
                                </td>
                                <td>
                                    Ingresar la fecha en la que se espera culmine la ejecución de su etapa productiva,
                                    en formato (DD/MM/AAAA).
                                </td>
                                <td></td>
                            </tr>
                            <tr>
                                <td colspan="3" style="text-align: center;">
                                    <strong>3. Selección o modificación de la alternativa de etapa productiva</strong>
                                </td>
                            </tr>
                            <tr>
                                <td colspan="3" style="text-align: center;">
                                    <strong>Marque con una (X) la alternativa de etapa productiva seleccionada por la persona con rol de aprendiz</strong>
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    Contrato de aprendizaje
                                </td>
                                <td>
                                    El contrato de aprendizaje es una forma especial dentro del derecho laboral que, permite a las personas con rol de aprendiz, desarrollar su formación teórico-práctica a cambio de que la empresa patrocinadora proporcione los medios para adquirir esta y le otorgue un apoyo de sostenimiento mensual, que en ningún caso constituye salario, por un tiempo determinado no superior a dos (2) año- Ley 789 del 2002
                                </td>
                                <td>
                                    En caso de que el contrato de aprendizaje  pertenezca a la estrategia SENNOVA o Prácticas en la economía popular y/o campesina seleccione la que corresponda. En caso contrario marque con una X en la fila "contrato de aprendizaje (Regular)"	
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    Monitoría
                                </td>
                                <td>
                                    La monitoria es el conjunto de actividades mediante las cuales las personas con rol de aprendiz seleccionadas apoyan los procesos de formación a través de actividades complementarias, para garantizar mayores niveles de calidad en todos los elementos que confluyen en el proceso de aprendizaje.  Con la Resolución 1234 de 2013, el desarrollo de monitorias por parte de las personas con rol de aprendiz en las especialidades afines tecnológicamente a su programa de formación, se consideran alternativa para la etapa productiva.
                                </td>
                                <td>
                                    En caso de que la monitoría pertenezca a la estrategia SENNOVA seleccione dicha opción. En caso contrario marque con una X en la fila "monitoría (Regular)"	
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    Sena empresa
                                </td>
                                <td>
                                    Es una estrategia que tiene como objetivo acercarse a la realidad de las empresas mediante la producción eficiente de bienes y servicios en los centros de formación, a través de la integración de los procesos productivos y la optimización del uso de los recursos del SENA, integrando de manera natural todas las actividades de las diferentes áreas de formación, trascendiendo las propias del centro a otras áreas de empresa como: la financiera y contable, administrativa y de recursos humanos, comercialización, mercadeo y logística, la de producción y control de calidad y la gerencial. De esta manera, se articulan las personas con rol de aprendiz de los programas de aprendizaje de las diferentes áreas, a través de la rotación por los diferentes roles de esta empresa en un modelo evaluado y mejorado continuamente. (https://www.sena.edu.co/es-co/ciudadano/Lists/glosario_sena/DispForm.aspx?ID=16&ContentTypeId=0x0100D3A8BC444C104E43840BB7D7E24AAA81)
                                </td>
                                <td></td>
                            </tr>
                            <tr>
                                <td>
                                    Sena proveedor Sena
                                </td>
                                <td>
                                    Es una estrategia para desarrollar las competencias a lograr por las personas con rol de aprendiz y que están previstas en un programa de formación o en el desarrollo de actividades que contribuyen a los procesos de formación integral de los centros de formación, a través de proyectos que tengan como objetivo la producción de bienes y servicios, en un centro de formación, que sean demandados por otros centros, regionales, direcciones, o las redes de conocimiento a nivel local, regional y nacional.  (GRF-I-005  Instructivo Aplicación Estrategia SENA Proveedor SENA y SENA Autoconsumo). 
                                </td>
                                <td></td>
                            </tr>
                            <tr>
                                <td>
                                    Producción de centros
                                </td>
                                <td>
                                    Se entiende como los bienes y servicios que se obtienen en los centros de formación a través de los proyectos formativos desarrollados por las personas con rol de aprendiz como parte de las actividades para desarrollar las competencias previstas en los programas de aprendizaje y las acciones adelantadas por los centros de formación para la resolución de problemas y necesidades de instituciones, empresas y comunidad en general, con el fin de mejorar la productividad, elevar la calidad y promover el desarrollo tecnológico del país. (GRF-I-001 V3.  Instructivo para Recaudo de Producción de Centros) 
                                </td>
                                <td></td>
                            </tr>
                            <tr>
                                <td>
                                    Proyecto productivo bajo enfoque empresarial
                                </td>
                                <td>
                                    En este enfoque, la persona con rol de aprendiz mediante la formulación de un plan de negocio identifica, describe y analiza un problema, una necesidad o una oportunidad de negocio, a través de la viabilidad técnica, económica y financiera del mismo, desarrollando todos los procedimientos y estrategias necesarias para convertir la citada oportunidad en un proyecto productivo, sea este de una unidad productiva que se encuentra constituida, que se desea poner en marcha o solo como una idea de negocio.
                                </td>
                                <td></td>
                            </tr>
                            <tr>
                                <td>
                                    Proyecto productivo bajo enfoque I+D+i
                                </td>
                                <td>
                                    En este enfoque, la persona con rol de aprendiz participa en una investigación en curso relacionada con las competencias del programa de formación al cual pertenece o propone una nueva investigación o un plan de innovación para una empresa o sector productivo, con entregables propios a los productos de su perfil como egresado, mediante la formulación de una vigilancia tecnológica y el desarrollo de un prototipo.
                                </td>
                                <td></td>
                            </tr>
                            <tr>
                                <td>
                                    Proyectos ruta emprendedora
                                </td>
                                <td>
                                    La persona con rol de aprendiz realiza la etapa productuva  a través de las unidades de emprendimiento, contando con el respectivo aval por parte de la coordinación académica del centro de formación en el cual se encuentra matriculado.
                                </td>
                                <td></td>
                            </tr>
                            <tr>
                                <td>
                                    SENNOVA
                                </td>
                                <td>
                                    Seleccione esta opción en caso de que el proyecto productivo se desarrolle en el marco de la estrategía SENNOVA. 
                                </td>
                                <td></td>
                            </tr>
                            <tr>
                                <td>
                                    Prácticas en la economía popular y/o campesena
                                </td>
                                <td>
                                    Seleccione esta opción en caso de que el proyecto productivo se desarrolle en el marco de la estrategía CampeSENA o economía Popular - Full popular. 
                                </td>
                                <td></td>
                            </tr>
                            <tr>
                                <td>
                                    Contrato de Vínculo formativo
                                </td>
                                <td>
                                    Anteriormente denominada "pasantía", en la que la persona con rol de aprendiz concerta con una empresa, institución, organización o entidad; la aplicación de las competencias de su programa de formación. Para la ejecución de esta alternativa se suscribe el GFPI-F-191 Formato de vínculo formativo - Práctica del Programa (o en entidades públicas se emite un acto administrativo), en el marco de la Resolución 623 de 2020. 
                                </td>
                                <td></td>
                            </tr>
                            <tr>
                                <td>
                                    Asesoría a Pymes
                                </td>
                                <td>
                                    Opción de la alternativa de contrato de vínculo formativo, constituye un escenario específico de práctica, donde la persona con rol de aprendiz tiene la oportunidad de brindar apoyo estratégico para el fortalecimiento empresarial de micro, pequeñas y medianas empresas (MIPYMES). 
                                </td>
                                <td></td>
                            </tr>
                            <tr>
                                <td>
                                    Apoyo a una unidad productiva familiar
                                </td>
                                <td>
                                    Opción de la alternativa de vínculo formativo en la que la persona con rol de aprendiz pueda aplicar en las actividades que desarrolla las competencias adquiridas durante su proceso de formación en una unidad productiva familiar. (Puede no ser propiedad de algún miembro de su familia). La persona con rol de aprendiz hace una concertación con la persona con rol de propietario u administrador de la unidad productiva sobre las condiciones de estadía, esto es; pago de algún auxilio económico, transporte, alimentación entre otros. 
                                </td>
                                <td></td>
                            </tr>
                            <tr>
                                <td>
                                    Apoyo a una institución estatal nacional, territorial, ONG o entidad sin ánimo de lucro
                                </td>
                                <td>
                                    Opción de la alternativa de contrato de vínculo formativo, donde la persona con rol de aprendiz concerta con una institución estatal nacional, territorial, ONG o entidad sin ánimo de lucro. Estas actividades se ejecutan en un ambiente de formación facilitado por la organización u entidad. Aquí la persona con rol de aprendiz concerta con el ente co-formador las condiciones de estadía, esto es: pago de algún auxilio económico o en especie. 
                                </td>
                                <td></td>
                            </tr>
                            <tr>
                                <td>
                                    SENNOVA
                                </td>
                                <td>
                                    Seleccione esta opción en caso de que el vínculo formativo se ejecute en el marco de la estrategía SENNOVA. 
                                </td>
                                <td></td>
                            </tr>
                            <tr>
                                <td>
                                    Prácticas en la economía popular y/o campesena
                                </td>
                                <td>
                                    Seleccione esta opción en caso de que el vínculo formativo se ejecute en el marco de la estrategía CampeSENA o economía Popular - Full popular. 
                                </td>
                                <td></td>
                            </tr>
                            <tr>
                                <td>
                                    Vínculo laboral
                                </td>
                                <td>
                                    Esta alternativa considera la relación laboral que la persona con rol de aprendiz establece con una organización, entidad o empresa a través de un vínculo laboral o contractual o a través de prestación de servicios. Esta alternativa puede ejecutarse a partir del último trimestre de la etapa lectiva. 
                                </td>
                                <td></td>
                            </tr>
                            <tr>
                                <td>
                                    Prácticas en la economía popular y/o campesena
                                </td>
                                <td>
                                    Seleccione esta opción en caso de que el vínculo laboral se ejecute en el marco de la estrategía CampeSENA o economía Popular - Full popular.  
                                </td>
                                <td></td>
                            </tr>
                            <tr>
                                <td>
                                    Nombre y firma de la persona con rol de aprendiz
                                </td>
                                <td>
                                    La firma del documento se realizará de acuerdo a las indicaciones brindadas por la coordinación académica, teniendo en cuenta que, podría ser manuscrita, digital,  o en caso de que las circunstancias lo ameriten agregando "participación virtual"  al tratarse de un diligenciamiento realizado durante una sesión sincrónica (en la que puede adjuntar el acta y/o grabación de la sesión). 
                                </td>
                                <td></td>
                            </tr>
                            <tr>
                                <td>
                                    Nombre y firma de la persona con rol de coordinador académico
                                </td>
                                <td>
                                    Registrar el nombre completo y firma de la persona con rol de coordinador académico que brinda el aval.
                                </td>
                                <td></td>
                            </tr>
                            <tr>
                                <td>
                                    Fecha de aval: 
                                </td>
                                <td>
                                    Especificar la fecha en la que se brinda aval a la alternativa, en formato (DD/MM/AAAA).
                                </td>
                                <td></td>
                            </tr>
                        </tbody>
                    </table>
                </div>


            </div>

            <!-- Footer del modal -->
            <div class="modal-footer">
                <button @click="$emit('cerrar')" class="close-button-main">
                    Cerrar
                </button>
            </div>
        </div>
    </div>
</template>

<style scoped>
.modal-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background: rgba(0, 0, 0, 0.6);
    backdrop-filter: blur(2px);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 9999;
    animation: fadeIn 0.3s ease-out;
}

@keyframes fadeIn {
    from {
        opacity: 0;
    }

    to {
        opacity: 1;
    }
}

.modal {
    background: white;
    border-radius: 16px;
    max-width: 90vw;
    width: 980px;
    max-height: 85vh;
    box-shadow:
        0 25px 50px -12px rgba(0, 0, 0, 0.25),
        0 0 0 1px rgba(255, 255, 255, 0.8);
    display: flex;
    flex-direction: column;
    overflow: hidden;
    animation: slideIn 0.3s ease-out;
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
}

@keyframes slideIn {
    from {
        opacity: 0;
        transform: scale(0.9) translateY(10px);
    }

    to {
        opacity: 1;
        transform: scale(1) translateY(0);
    }
}

.modal-header {
    background: linear-gradient(135deg, #1c9247 0%, #16a34a 100%);
    color: white;
    padding: 24px 32px;
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    position: relative;
}

.title-gi {
    font-size: 20px;
    font-weight: 700;
    margin: 0;
    line-height: 1.3;
    display: flex;
    align-items: center;
    gap: 12px;
    flex: 1;
    padding-right: 20px;
}

.icon {
    font-size: 24px;
}

.close-button {
    background: rgba(255, 255, 255, 0.2);
    color: white;
    border: none;
    width: 36px;
    height: 36px;
    border-radius: 50%;
    font-size: 24px;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: all 0.2s ease;
    flex-shrink: 0;
}

.close-button:hover {
    background: rgba(255, 255, 255, 0.3);
    transform: scale(1.1);
}

.modal-content {
    flex: 1;
    overflow-y: auto;
    padding: 0;
}

.content-wrapper {
    padding: 32px;
}

.section-header {
    margin-bottom: 24px;
    border-bottom: 3px solid #118a1f;
    padding-bottom: 12px;
}

.section-header h2 {
    margin: 0;
    font-size: 24px;
    font-weight: 600;
    color: #13213c;
}

.instructions-list {
    display: flex;
    flex-direction: column;
    gap: 20px;
}

.instruction-item {
    display: flex;
    gap: 16px;
    padding: 20px;
    background: #ffffff;
    border-radius: 12px;
    border-left: 4px solid #0c985c;
    transition: all 0.2s ease;
    box-shadow: 0 4px 12px rgba(55, 71, 144, 0.3);
}

.instruction-item:hover {
    background: #ffffff;
    transform: translateX(4px);
    box-shadow: 0 4px 12px rgba(0, 0, 1, 0.641);
}

.classification-note {
    background: linear-gradient(135deg, #e4ffe8 0%, #73de85 100%);
    border-left-color: #148f1c;
}

.classification-note:hover {
    background: linear-gradient(135deg, #d2f5d7 0%, #55ba66 100%);
}

.instruction-label {
    font-weight: 700;
    color: #05623d;
    font-size: 16px;
    min-width: 24px;
    flex-shrink: 0;
}

.instruction-content {
    color: #0f295b;
    line-height: 1.6;
    font-size: 15px;
}

.instruction-content strong {
    color: #1e2a3f;
}

.instruction-content em {
    color: #066f1d;
    font-weight: 600;
}

.modal-footer {
    background: #f8fafc;
    padding: 20px 32px;
    border-top: 1px solid #e2e8f0;
    display: flex;
    justify-content: flex-end;
}

.close-button-main {
    background: linear-gradient(135deg, #17b152 0%, #05963d 100%);
    color: white;
    border: none;
    padding: 12px 32px;
    border-radius: 8px;
    font-weight: 600;
    font-size: 16px;
    cursor: pointer;
    transition: all 0.2s ease;
    box-shadow: 0 4px 12px rgba(16, 20, 37, 0.3);
}

.close-button-main:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 20px rgba(102, 126, 234, 0.4);
}

.close-button-main:active {
    transform: translateY(0);
}

/* Scrollbar personalizado */
.modal-content::-webkit-scrollbar {
    width: 8px;
}

.modal-content::-webkit-scrollbar-track {
    background: #f1f5f9;
}

.modal-content::-webkit-scrollbar-thumb {
    background: #cbd5e0;
    border-radius: 4px;
}

.modal-content::-webkit-scrollbar-thumb:hover {
    background: #a0aec0;
}

/* Estilos para la tabla */
table {
    width: 100%;
    border-collapse: separate;
    border-spacing: 0;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    font-size: 14px;
    background-color: #ffffff;
    color: #407255;
    border-radius: 12px;
    overflow: hidden;
    box-shadow:
        0 10px 25px -5px rgba(0, 0, 0, 0.1),
        0 4px 6px -2px rgba(0, 0, 0, 0.05);
    border: 1px solid #e2e8f0;
}

thead {
    background: linear-gradient(135deg, #0c985c 0%, #059669 100%);
    position: relative;
}

thead::after {
    content: '';
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    height: 2px;
    background: linear-gradient(90deg, #10b981, #059669);
}

thead th {
    padding: 16px 18px;
    border: none;
    text-align: left;
    font-weight: 600;
    color: #ffffff;
    font-size: 15px;
    letter-spacing: 0.3px;
    text-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
    position: relative;
}

thead th:not(:last-child)::after {
    content: '';
    position: absolute;
    right: 0;
    top: 25%;
    height: 50%;
    width: 1px;
    background: rgba(44, 35, 35, 0.2);
}

tbody td {
    padding: 14px 18px;
    border: none;
    border-bottom: 1px solid #e2f9ee;
    vertical-align: top;
    line-height: 1.6;
    transition: all 0.2s ease;
}

tbody tr {
    transition: all 0.3s ease;
    position: relative;
}

tbody tr:nth-child(even) {
    background-color: #c8f7dc;
}

tbody tr:nth-child(odd) {
    background-color: #ffffff;
}

tbody tr:hover {
    background: linear-gradient(135deg, #e8faf3 0%, #e0fef2 100%);
    transform: translateY(-1px);
    box-shadow:
        0 4px 12px rgba(0, 0, 0, 0.08),
        0 2px 4px rgba(0, 0, 0, 0.03);
}

tbody tr:hover td {
    border-bottom-color: #9dcfbb;
}

/* Efecto de hover más sutil en las celdas */
tbody td:hover {
    background: rgba(59, 246, 146, 0.04);
}

/* Bordes redondeados mejorados */
thead th:first-child {
    border-top-left-radius: 12px;
}

thead th:last-child {
    border-top-right-radius: 12px;
}

tbody tr:last-child td:first-child {
    border-bottom-left-radius: 12px;
}

tbody tr:last-child td:last-child {
    border-bottom-right-radius: 12px;
}

tbody tr:last-child td {
    border-bottom: none;
}

/* Mejoras adicionales para texto */
tbody td {
    font-size: 14px;
    color: #09103a;
}

tbody td strong {
    color: #1f372b;
    font-weight: 600;
}

tbody td em {
    color: #059669;
    font-style: normal;
    font-weight: 500;
}

/* Efecto de carga suave */
table {
    animation: tableSlideIn 0.5s ease-out;
}

@keyframes tableSlideIn {
    from {
        opacity: 0;
        transform: translateY(10px);
    }

    to {
        opacity: 1;
        transform: translateY(0);
    }
}

/* Responsive mejorado */
@media (max-width: 768px) {
    table {
        font-size: 13px;
        border-radius: 8px;
    }

    thead th {
        padding: 12px 14px;
        font-size: 14px;
    }

    tbody td {
        padding: 12px 14px;
    }
}

/* Estilos para contenido específico */
.table-container {
    padding: 20px;
    background: #f9fafb;
    border-radius: 16px;
    margin: 20px 0;
}

.table-title {
    font-size: 18px;
    font-weight: 600;
    color: #031125;
    margin-bottom: 16px;
    display: flex;
    align-items: center;
    gap: 8px;
}

.table-title::before {
    content: '📊';
    font-size: 20px;
}

/* Si usas contenedor alrededor */
.section-header {
    margin-bottom: 16px;
    font-size: 18px;
    font-weight: 600;
    color: #406230;
}

/* Responsive */
@media (max-width: 768px) {
    .modal {
        max-width: 95vw;
        max-height: 90vh;
        margin: 20px;
    }

    .modal-header {
        padding: 20px;
    }

    .title-gi {
        font-size: 18px;
    }

    .content-wrapper {
        padding: 24px 20px;
    }

    .instruction-item {
        flex-direction: column;
        gap: 8px;
    }

    .instruction-label {
        min-width: auto;
    }

    .modal-footer {
        padding: 16px 20px;
    }
}
</style>