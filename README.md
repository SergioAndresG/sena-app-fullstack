# 📋 Sistema de Gestión F-165

<p align="center">
  <strong>Plataforma Full-Stack para digitalización completa del formato F-165 (Contrato de Aprendizaje)</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/FastAPI-0.123-009688?logo=fastapi&logoColor=white" alt="FastAPI" />
  <img src="https://img.shields.io/badge/Vue.js-3.x-4FC08D?logo=vue.js&logoColor=white" alt="Vue.js" />
  <img src="https://img.shields.io/badge/TypeScript-5.x-3178C6?logo=typescript&logoColor=white" alt="TypeScript" />
  <img src="https://img.shields.io/badge/MySQL-8.0-4479A1?logo=mysql&logoColor=white" alt="MySQL" />
</p>

---

## 📋 Tabla de Contenidos

- [🎯 ¿Qué es este sistema?](#-qué-es-este-sistema)
- [💡 Problema que Resuelve](#-problema-que-resuelve)
- [✨ Características Principales](#-características-principales)
- [🏗️ Arquitectura del Sistema](#️-arquitectura-del-sistema)
- [👥 Roles y Permisos](#-roles-y-permisos)
- [📁 Estructura del Proyecto](#-estructura-del-proyecto)
- [🛠️ Tecnologías Utilizadas](#️-tecnologías-utilizadas)
- [🔒 Seguridad](#-seguridad)
- [🤝 Contribuciones](#-contribuciones)
- [📧 Contacto y Soporte](#-contacto-y-soporte)
- [👥 Equipo de Desarrollo](#-equipo-de-desarrollo)
---

## 🎯 ¿Qué es este sistema?

El **Sistema de Gestión F-165** es una plataforma full-stack diseñada específicamente para el **Centro de Biotecnología Agropecuaria (CBA) del SENA** que digitaliza completamente el proceso del formato F-165, utilizado para recopilar información de aprendices que migrarán a la plataforma SGVA (Sistema de Gestión de Contrato de Aprendizaje).

### 🎬 Flujo de Trabajo

```
┌─────────────────────────────────────────────────────────────┐
│  1️⃣  Admin carga reportes de Sofia Plus (Excel)            │
│  2️⃣  Admin carga reporte PE-04 con fechas y fichas         │
│  3️⃣  Sistema valida estructura y cruza información         │
│  4️⃣  Instructor busca su ficha y ve aprendices             │
│  5️⃣  Instructor edita información de aprendices            │
│  6️⃣  Aprendices firman digitalmente en canvas              │
│  7️⃣  Sistema genera formato F-165 completo (.xlsx          │
│  8️⃣  Limpieza automática de fichas obsoletas               │
└─────────────────────────────────────────────────────────────┘
```

---

## 💡 Problema que Resuelve

### El proceso manual tradicional

El formato F-165 es un documento crítico que históricamente se gestionaba de forma manual:

- 📄 **Recopilación manual** de datos de cada aprendiz
- ✍️ **Firmas físicas** que requieren presencia de todos los aprendices
- 📋 **Transcripción propensa a errores** de reportes de Sofia Plus
- 🗂️ **Validación manual** de fechas y números de ficha en base a Sofia Plus
- ⏰ **Proceso lento** que toma días o semanas por ficha

### La solución digital

Esta plataforma transforma completamente el proceso:

<table>
<tr>
<td align="center" width="33%">

### ⚡ Automatización
Carga masiva desde Excel con validación automática de estructura

</td>
<td align="center" width="33%">

### 🖊️ Firma Digital
Canvas interactivo para firmas digitales dentro del aplicativo

</td>
<td align="center" width="33%">

### 🔄 Gestión Inteligente
Limpieza automática de datos obsoletos

</td>
</tr>
</table>

### Beneficios cuantificables

| Aspecto | Proceso Manual | Con el Sistema |
|---------|---------------|----------------|
| ⏱️ **Tiempo por ficha** | 3-5 días | 1-2 horas |
| ⚠️ **Tasa de error** | 10-15% | <2% |
| 📊 **Generación de reportes** | Manual | Digital |
| 🔍 **Trazabilidad** | Baja | Alta (logs completos) |

---

## ✨ Características Principales

### 🔐 Sistema de Autenticación y Roles

- **Login seguro** con JWT (JSON Web Tokens)
- **Seguridad** contra ataques como DDoS
- **Dos roles diferenciados:** Administrador e Instructor
- **Generación automática** de credenciales para nuevos usuarios
- **Registro de actividad** en logs de seguridad

### 📊 Gestión de Reportes

#### Para Administradores:
- **Carga de Reportes de Sofia Plus** (.xls/.xlsx)
  - Validación automática de estructura requerida
  - Procesamiento masivo de datos de aprendices y fichas
  
- **Carga de Reporte PE-04**
  - Información de fechas de inicio y fin
  - Números de ficha y nombres de programas
  - Validación cruzada con datos de Sofia Plus

- **Dashboard de reportes generados**
  - Quién generó cada formato
  - Fecha y hora de generación
  - Cantidad de aprendices procesados
  - Modalidad (Grupal/Individual)

#### Para Instructores:
- **Búsqueda de fichas**
- **Visualización de aprendices** registrados
- **Edición de información** de aprendices
- **Generación de formatos** F-165

### 📝 Gestión de Formatos

#### Formato Grupal:
- Un documento .xlsx con todos los aprendices de la ficha
- Firmas digitales de múltiples aprendices
- Información validada del reporte PE-04

#### Formato Individual:
- .xlsx individual por cada aprendiz
- Información personalizada
- Firma digital del aprendiz

### 🖊️ Sistema de Firma Digital

- **Canvas** para firma
- **Guardado en base64** para almacenamiento eficiente
- **Integración automática** en el .xlsx generado
- **Validación de firma** antes de generar formato

### 🗃️ Gestión Inteligente de Datos

- **Validación de estructura** de archivos Excel
- **Cruce automático** de información entre reportes
- **Detección de inconsistencias** (fichas sin PE-04, fechas inválidas)
- **Limpieza automática** de fichas obsoletas después de X tiempo
- **Sistema de logs** para auditoría completa
  
- ** 🗃️ Procesamiento de Datos**
- **Pandas 2.0+** - Conversión de formatos Excel legacy
- **Polars 2.0+** - Procesamiento masivo de alto rendimiento
- **openpyxl 3.1+** - Lectura/escritura Excel

### 📥 Exportación y Descarga

- **Generación de .xlsx** con formato oficial F-165
- **Descarga** de formatos

---

## 🏗️ Arquitectura del Sistema

### Diagrama de Arquitectura

```
┌──────────────────────────────────────────────────────────────┐
│                    FRONTEND (Vue.js 3)                       │
│  ┌────────────────┐  ┌────────────────┐  ┌────────────────┐ │
│  │ Admin          │  │ Instructor      │  │ Auth           │ │
│  │ Dashboard      │  │ Dashboard       │  │ Service        │ │
│  └────────────────┘  └────────────────┘  └────────────────┘ │
│          │                    │                    │          │
│          └────────────────────┴────────────────────┘          │
│                             │                                 │
└─────────────────────────────┼─────────────────────────────────┘
                              │ HTTP/REST API
┌─────────────────────────────▼─────────────────────────────────┐
│                    BACKEND (FastAPI)                          │
│  ┌──────────────────────────────────────────────────────────┐ │
│  │              Security Middleware (JWT)                   │ │
│  └──────────────────────────────────────────────────────────┘ │
│  ┌────────────┐  ┌────────────┐  ┌────────────┐             │
│  │ Endpoints  │  │ Schemas    │  │ Models     │             │
│  │ (Routes)   │  │ (Pydantic) │  │ (ORM)      │             │
│  └────────────┘  └────────────┘  └────────────┘             │
│  ┌──────────────────────────────────────────────────────────┐ │
│  │                    Funciones (Business Logic)            │ │
│  │  • procesador_excel.py                                   │ │
│  │  • procesador_maestro_excel.py                           │ │
│  │  • tokens_service.py                                     │ │
│  │  • generador_contraseñas.py                              │ │
│  └──────────────────────────────────────────────────────────┘ │
└─────────────────────────────┬─────────────────────────────────┘
                              │ SQL
┌─────────────────────────────▼─────────────────────────────────┐
│                     DATABASE (MySQL 8.0)                      │
│  ┌────────────┐  ┌────────────┐  ┌────────────┐             │
│  │ Usuarios   │  │ Fichas     │  │ Aprendices │             │
│  └────────────┘  └────────────┘  └────────────┘             │
│  ┌────────────┐  ┌────────────┐                              │
│  │ Formatos   │  │ Logs       │                              │
│  └────────────┘  └────────────┘                              │
└───────────────────────────────────────────────────────────────┘
```


---

## 👥 Roles y Permisos

### Matriz de Permisos

| Funcionalidad | Administrador | Instructor |
|--------------|---------------|------------|
| **Login** | ✅ | ✅ |
| **Crear usuarios** | ✅ | ❌ |
| **Editar usuarios** | ✅ | ❌ |
| **Eliminar usuarios** | ✅ | ❌ |
| **Cargar Reporte PE-04** | ✅ | ❌ |
| **Cargar Reporte Sofia Plus** | ✅ | ❌ |
| **Consultar fichas** | ✅ | ✅ |
| **Editar aprendices** | ✅ | ✅ |
| **Recolectar firmas** | ❌ | ✅ |
| **Generar formatos** | ✅ | ✅ |
| **Ver dashboard reportes** | ✅ | ❌ |
| **Descargar formatos** | ✅ | ✅ |

---

## 📁 Estructura del Proyecto

### Backend (FastAPI)

```
backend/
├── main.py                          # Punto de entrada de la aplicación
│
├── endpoints/                       # Rutas de la API (Controllers)
│   ├── __init__.py
│   ├── login.py                     # POST /login
│   ├── usuarios.py                  # CRUD usuarios
│   ├── fichas.py                    # CRUD fichas
│   ├── aprendices.py                # CRUD aprendices
│   └── formatos.py                  # Generación de formatos
│
├── models/                          # Modelos de base de datos (ORM)
│   ├── __init__.py
│   ├── usuario.py                   # Modelo Usuario
│   ├── ficha.py                     # Modelo Ficha
│   ├── aprendiz.py                  # Modelo Aprendiz
│   ├── formato.py                   # Modelo Formato
│   └── log.py                       # Modelo Log
│
├── schemas/                         # Esquemas Pydantic (Validación)
│   ├── __init__.py
│   ├── usuario_schema.py            # UsuarioCreate, UsuarioResponse
│   ├── ficha_schema.py              # FichaCreate, FichaResponse
│   ├── aprendiz_schema.py           # AprendizCreate, AprendizResponse
│   └── formato_schema.py            # FormatoCreate, FormatoResponse
│
├── funciones/                       # Lógica de negocio
│   ├── __init__.py
│   ├── procesador_excel.py          # Procesamiento Sofia Plus
│   ├── procesador_maestro_excel.py  # Procesamiento PE-04
│   ├── tokens_service.py            # Gestión JWT
│   ├── generador_contraseñas.py    # Generación de contraseñas
│   ├── generador_pdf.py             # Generación de PDFs F-165
│   └── limpieza_fichas.py           # Cleanup de datos obsoletos
│
├── middleware/                      # Middleware personalizado
│   ├── __init__.py
│   └── security_middleware.py       # Verificación JWT
│
├── database/                        # Configuración de BD
│   ├── __init__.py
│   └── connection.py                # Conexión SQLAlchemy
│
├── logs/                            # Logs de la aplicación
│   └── security.log                 # Registro de seguridad
│
├── scripts/                         # Scripts de utilidad
│   ├── init_db.py                   # Inicializar BD
│   └── create_admin.py              # Crear admin inicial
│
├── tests/                           # Tests unitarios
│   ├── __init__.py
│   ├── test_usuarios.py
│   ├── test_fichas.py
│   └── test_formatos.py
│
├── requirements.txt                 # Dependencias Python
├── .env                            # Variables de entorno
└── README.md                       # Este archivo
```

### Frontend (Vue.js 3)

```
frontend/
├── src/
│   ├── main.js                      # Punto de entrada Vue
│   │
│   ├── router/                      # Vue Router
│   │   └── router.js                # Definición de rutas
│   │
│   ├── views/                       # Páginas principales
│   │   ├── Login.vue                # Página de login
│   │   ├── AdminDashboard.vue       # Dashboard administrador
│   │   ├── InstructorDashboard.vue  # Dashboard instructor
│   │   ├── DashboardUsers.vue       # Gestión de usuarios
│   │   ├── GroupFormat.vue          # Formato grupal
│   │   └── IndividualFormat.vue     # Formato individual
│   │
│   ├── components/                  # Componentes reutilizables
│   │   ├── Header.vue               # Cabecera
│   │   ├── Footer.vue               # Pie de página
│   │   ├── Sidebar.vue              # Menú lateral
│   │   ├── AddUsers.vue             # Modal agregar usuario
│   │   ├── EditAprendizModal.vue    # Modal editar aprendiz
│   │   ├── SignatureCanvas.vue      # Canvas de firma
│   │   ├── FileUploader.vue         # Componente carga archivos
│   │   └── DataTable.vue            # Tabla de datos genérica
│   │
│   ├── services/                    # Servicio
│   │   ├── auth_service.ts          # Autenticación
│   │
│   ├── assets/                      # Recursos estáticos
│   │   ├── images/
│   │   │   ├── logo-sena.png
│   │   │   └── icon-edit.svg
│   │   └── styles/
│   │       └── main.css
│   │
│
├── public/                          # Archivos públicos
│   └── favicon.ico
│
├── package.json                     # Dependencias Node
├── vite.config.ts                  # Configuración Vite
├── tsconfig.json                   # Configuración TypeScript
```

---

## 🛠️ Tecnologías Utilizadas
```

### Backend

| Tecnología | Versión | Propósito |
|------------|---------|-----------|
| **Python** | 3.10+ | Lenguaje base |
| **FastAPI** | 0.100+ | Framework web de alto rendimiento |
| **SQLAlchemy** | 2.0+ | ORM para base de datos |
| **Pydantic** | 2.0+ | Validación y serialización de datos |
| **PyMySQL** | 1.1+ | Driver MySQL para Python |
| **Python-Jose** | 3.3+ | Manejo de JWT |
| **Passlib** | 1.7+ | Hashing de contraseñas |
| **Pandas** | 2.0+ | Procesamiento de archivos Excel |
| **Polars** | 2.0+ | Procesamiento de archivos Excel |
| **openpyxl** | 3.1+ | Lectura/escritura Excel |
| **ReportLab** | 4.0+ | Generación de PDFs |
| **Uvicorn** | 0.23+ | Servidor ASGI |



### Frontend

| Tecnología | Versión | Propósito |
|------------|---------|-----------|
| **Vue.js** | 3.x | Framework progresivo de UI |
| **TypeScript** | 5.x | Tipado estático |
| **Vite** | 4.x | Build tool y dev server |
| **Vue Router** | 4.x | Enrutamiento SPA |
| **Axios** | 1.x | Cliente HTTP |

### Base de Datos

| Tecnología | Versión | Propósito |
|------------|---------|-----------|
| **MySQL** | 8.0+ | Base de datos relacional |

### Herramientas de Desarrollo

| Herramienta | Propósito |
|-------------|-----------|
| **Git** | Control de versiones |
| **Postman** | Testing de API |
| **MySQL Workbench** | Gestión de BD |
| **VS Code** | Editor de código |

```

---

## 🔒 Seguridad
---

### Medidas Implementadas

- ✅ **Autenticación JWT** con tokens de corta duración
- ✅ **Hashing de contraseñas** con bcrypt
- ✅ **Middleware de seguridad** para verificar permisos
- ✅ **Logs de seguridad** para auditoría
- ✅ **Validación de entrada** con Pydantic
- ✅ **CORS configurado** para orígenes permitidos
- ✅ **SQL Injection protection** mediante ORM

### Buenas Prácticas

- 🔐 Cambiar contraseña en primer inicio de sesión
- 🔐 No compartir credenciales entre usuarios
- 🔐 Revisar logs de seguridad periódicamente
- 🔐 Mantener el sistema actualizado
- 🔐 Realizar backups regulares de la base de datos

---
## 🤝 Contribuciones
---


¡Las contribuciones son bienvenidas! Para contribuir:

### Proceso

1. **Fork** el repositorio
2. Crea una rama para tu feature:
   ```bash
   git checkout -b feature/nueva-funcionalidad
   ```
3. Haz tus cambios siguiendo las convenciones del proyecto
4. Escribe tests para nuevas funcionalidades
5. Asegúrate de que todos los tests pasen:
   ```bash
   # Backend
   pytest tests/
   
   # Frontend
   npm run test
   ```
6. Commit con mensajes descriptivos:
   ```bash
   git commit -m "Add: nueva funcionalidad X que hace Y"
   ```
7. Push a tu fork:
   ```bash
   git push origin feature/nueva-funcionalidad
   ```
8. Abre un **Pull Request** detallado

### Convenciones de Código

**Python (Backend):**
- Sigue **PEP 8**
- Usa **type hints**
- Documenta con **docstrings**
- Nombres en `snake_case`

**TypeScript (Frontend):**
- Sigue **ESLint** configurado
- Usa **tipos explícitos**
- Componentes en `PascalCase`
- Funciones en `camelCase`

**Git Commits:**
```
Add: nueva funcionalidad
Fix: corrección de bug
Update: actualización de funcionalidad
Refactor: refactorización de código
Docs: cambios en documentación
Style: cambios de formato (sin cambios de lógica)
```



---

## 📧 Contacto y Soporte

### ¿Necesitas ayuda?

- 🐛 **Reportar bugs**: [Issues del repositorio](https://github.com/SergioAndresG/sena-app-fullstack/issues)
- 💡 **Sugerencias**: [Discussions](https://github.com/SergioAndresG/sena-app-fullstack/discussions)
- 📧 **Contacto directo**: sergiogarcia3421@gmail.com
---

## 👥 Equipo de Desarrollo

Este proyecto fue desarrollado colaborativamente por:

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/SergioAndresG">
        <img src="https://github.com/SergioAndresG.png" width="100px;" alt="Sergio García"/>
        <br />
        <sub><b>Sergio Andrés García</b></sub>
      </a>
      <br />
      <sub>Full-Stack Developer</sub>
      <br />
      💻 📊 🎨 📖
    </td>
    <td align="center">
      <a href="https://github.com/JohannaB95">
        <img src="https://github.com/JohannaB95.png" width="100px;" alt="Johanna"/>
        <br />
        <sub><b>Leidy Johanna Bolivar Gonzalez</b></sub>
      </a>
      <br />
      <sub>Full-Stack Developer</sub>
      <br />
      💻 🎨 🐛 📖
    </sub>
    </td>
  </tr>
</table>

<p align="center">
  <sub>Sistema de digitalización completa del formato F-165 para migración a SGVA</sub>
</p>

<p align="center">
  <a href="#-tabla-de-contenidos">⬆️ Volver arriba</a>
</p>
