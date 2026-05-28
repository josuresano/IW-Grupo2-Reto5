# IW-Grupo2-Reto5
### Enlace al repositorio GitHub:
https://github.com/josuresano/IW-Grupo2-Reto5

---

## Descripción general del proyecto

Deusto QA es una aplicación web para gestionar calidad en entornos industriales. Registra no conformidades y acciones correctivas según ISO 9001, con un dashboard donde ver el estado de cada incidencia, asignar responsables y hacer seguimiento hasta el cierre.

---

## Flujo ISO 9001

1. **Detección** — Se registra la no conformidad
2. **Asignación** — Se designa un responsable
3. **Corrección** — Se implementa la acción correctiva
4. **Seguimiento** — Se controla el estado (Abierta / En Proceso / Cerrada) desde el dashboard

---

## Stack tecnológico

| Componente | Tecnología | Función |
|---|---|---|
| Backend | Django 6.0.5 | Lógica, ORM y enrutamiento |
| API | Django REST Framework | Endpoints para consumo externo |
| Autenticación | JWT (SimpleJWT) | Acceso seguro a las vistas API |
| Base de datos | SQLite | Almacenamiento por defecto |
| Frontend | HTML5 / CSS | UI con el sistema de diseño "Deusto QA" |
| Scripts | JavaScript | Filtrado y actualizaciones dinámicas |

---

## Arquitectura

Sigue el patrón MVT de Django con una capa REST encima. Un detalle: `procesador.py` vive dentro de `static/` y se encarga del cálculo de KPIs globales.

Organización del código:

- `Gestion_NC/` — Modelos, formularios y vistas
- `templates/HTML/` — Layouts, incluyendo el template de formulario universal
- `static/` — CSS (`estilos.css`), scripts (`JS/scripts.js`) y `procesador.py`
- `Control_Calidad_Industria/` — `settings.py` y tabla de rutas en `urls.py`

---

## Características Principales

### Gestión de Calidad Integral
- **Registro de No Conformidades (NC)**: Documentación y seguimiento de desviaciones de calidad
- **Acciones Correctivas**: Gestión de planes de acción para eliminar causas raíz
- **Equipo de Responsables**: Directorio de personal asignado a la gestión de calidad

### Panel de Control
- **Dashboard Principal**: Métricas globales en tiempo real
- **KPIs Visuales**: Contadores de NC registradas, acciones correctivas y responsables
- **Navegación Intuitiva**: Acceso rápido a todas las funcionalidades

### Funcionalidades Técnicas
- **CRUD Completo**: Crear, leer, actualizar y eliminar registros
- **Fichas Técnicas**: Vistas detalladas de cada no conformidad
- **Formularios Universales**: Templates reutilizables para todas las operaciones
- **Confirmaciones de Seguridad**: Diálogos de confirmación para eliminaciones

---

## Instalación y Uso

1. Clonar el repositorio
2. Configurar entorno virtual
3. Instalar dependencias con `pip install -r requirements.txt`
4. Ejecutar migraciones: `python manage.py migrate`
5. Iniciar servidor: `python manage.py runserver`

## Acceso al Sistema

- **Inicio**: Panel principal con métricas globales
- **No Conformidades**: Listado y gestión de NCs
- **Acciones Correctivas**: Registro y seguimiento de ACs
- **Responsables**: Directorio del equipo de calidad

---

## Funcionalidades JavaScript

El proyecto incorpora un archivo JavaScript ubicado en:

`static/JS/scripts.js`

Este script mejora la interacción de la aplicación sin necesidad de recargar la página completa.

### Mejoras implementadas

- Buscador dinámico en las tablas de No Conformidades y Responsables.
- Botón "Limpiar" para vaciar la búsqueda y volver a mostrar todos los registros.
- Contador de registros visibles actualizado en tiempo real.
- Cambio visual automático de los estados de las no conformidades:
  - Abierta: rojo
  - Cerrada o finalizada: verde
  - Pendiente o en proceso: naranja
- Mensaje informativo añadido dinámicamente debajo del título principal.

### Técnicas utilizadas

- `DOMContentLoaded` para ejecutar el código cuando la página ya está cargada.
- `querySelectorAll` para seleccionar tablas, filas y elementos del DOM.
- `createElement` para crear nuevos elementos HTML desde JavaScript.
- `addEventListener` para reaccionar a eventos del usuario.
- Manipulación de estilos mediante JavaScript.
- Filtrado de contenido en tiempo real sin recargar la página.

---

## Mejoras en el Registro de Acciones y CSS

Se ha optimizado la interfaz de las acciones correctivas para garantizar la coherencia visual y la integridad de los datos en toda la plataforma.

- **Enriquecimiento de Datos**: Incorporación de columnas para NC Asociada, Responsable y Fecha Prevista, conectando la tabla directamente con los campos del modelo.
- **Formateo Profesional**: Aplicación de filtros de fecha (d/m/Y) y estilos de "badge" azul para los códigos, facilitando la lectura técnica.
- **Consistencia Visual**: Unificación del diseño mediante variables CSS y el uso del contenedor `main-wrapper` para mantener márgenes y sombras uniformes.
- **Optimización de Tabla**: Ajuste de alineaciones y anchos automáticos que evitan la deformación de la interfaz independientemente del contenido.

## Optimización de Tablas y Navegación

Se han realizado ajustes técnicos en el CSS y en las plantillas HTML para mejorar la lectura de datos y la experiencia de usuario en las secciones críticas.

## Mejoras en CSS (Navegación y Estilos)

Se ha optimizado el selector `nav a.active` para que la pestaña actual se mantenga resaltada en azul, proporcionando una ubicación clara al usuario.

## Cambios en HTML (Acciones y Responsables)

Lista No Conformidades: Se han integrado nuevas columnas para mostrar la NC Asociada, el Responsable y la Fecha Prevista de un vistazo, evitando clics innecesarios.

Lista de Responsables: Reestructuración de la tabla para unificarla con el diseño general de la aplicación, aplicando las mismas cabeceras y márgenes que en el resto de módulos.


## NEON

En lugar de tener cada miembro del equipo con su propia base de datos local, usamos NEON: una base de datos PostgreSQL en la nube. Todos comparten los mismos datos, y la aplicación es accesible desde cualquier sitio. La conexión se configura con la variable `DATABASE_URL` en el `.env`.

---

## NGROK

Cuando ejecutas `python manage.py runserver`, tu web solo existe en `localhost:8000`, tu ordenador, y nadie más. NGROK cambia eso: crea un túnel entre tu máquina e internet y te da una URL pública del tipo `https://xxxx.ngrok-free.app`. Cualquiera con esa URL puede acceder a tu aplicación sin que tengas que desplegarla en ningún servidor. Útil para demos y pruebas rápidas.

---

## JWT (JSON Web Token)

Es el sistema de autenticación que hemos implementado. Cuando el usuario introduce su usuario y contraseña, el servidor genera dos tokens: un access token que dura 15 minutos y un refresh token que dura 7 días. A partir de ese momento, en lugar de enviar usuario y contraseña en cada petición, el navegador envía ese token. El servidor lo verifica matemáticamente sin consultar la base de datos, lo que lo hace más rápido y escalable. Si el token expira, el sistema lo renueva automáticamente con el refresh token sin que el usuario lo note.

Para cerrar sesión, pulsa sobre tu nombre de usuario en la barra de navegación.

---

## Documentación adicional

- *Getting Started & Installation* — Entorno, dependencias desde `salida_pip_freeze.txt` y arranque con `manage.py`
- *Project Configuration* — `settings.py` al detalle: middleware WhiteNoise, JWT y rutas de estáticos