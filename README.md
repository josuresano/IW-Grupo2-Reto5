# IW-Grupo2-Reto5
### Enlace al repositorio GitHub: 
https://github.com/josuresano/IW-Grupo2-Reto5

---

## Descripción del Proyecto  
  
Este proyecto es un sistema web de gestión de calidad industrial desarrollado con Django que permite el seguimiento y control de no conformidades y acciones correctivas en entornos industriales, siguiendo los estándares de calidad ISO 9001.  
  
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
  
## Arquitectura del Sistema  
  
### Estructura MVT (Model-View-Template)  
- **Models**: `NoConformidad`, `AccionCorrectiva`, `Responsable`  
- **Views**: Lógica de negocio para gestión de calidad  
- **Templates**: Interfaz de usuario en español  
  
### Tecnologías Utilizadas  
- **Backend**: Django 6.0.4
- **Frontend**: HTML5, CSS con variables personalizadas  
- **Base de Datos**: Configurable (SQLite por defecto)  
- **Estilo**: Sistema de diseño corporativo "Deusto QA"  
  
## Organización de Módulos

- Gestion_NC/ # Módulo principal de gestión
   - models.py # Modelos de datos
   - views.py # Lógica de negocio
   - forms.py # Formularios Django
- templates/HTML/ # Plantillas de interfaz
- static/CSS/ # Hojas de estilo
- static/Python/ # Scripts de procesamiento

## Flujo de Trabajo  
  
1. **Registro Inicial**: Captura de no conformidades  
2. **Asignación**: Designación de responsables  
3. **Acción Correctiva**: Implementación de soluciones  
4. **Seguimiento**: Monitorización del estado  
5. **Cierre**: Verificación y finalización  
  
## Configuración del Idioma  
  
El sistema está configurado para operar en castellano:  
- Interfaz de usuario completamente en español  
- Terminología industrial estándar  
- Configuración regional para formatos de fecha y números  
  
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

## Funcionalidades JavaScript

El proyecto incorpora un archivo JavaScript ubicado en:

static/JS/scripts.js

Este script mejora la interacción de la aplicación sin necesidad de recargar la página completa.

### Mejoras implementadas

- Buscador dinámico en las tablas de No Conformidades y Responsables.
- Botón “Limpiar” para vaciar la búsqueda y volver a mostrar todos los registros.
- Contador de registros visibles actualizado en tiempo real.
- Cambio visual automático de los estados de las no conformidades:
  - Abierta: rojo
  - Cerrada o finalizada: verde
  - Pendiente o en proceso: naranja
- Mensaje informativo añadido dinámicamente debajo del título principal.

### Técnicas utilizadas

Para implementar estas funcionalidades se han utilizado conceptos básicos de JavaScript trabajados en clase:

- `DOMContentLoaded` para ejecutar el código cuando la página ya está cargada.
- `querySelectorAll` para seleccionar tablas, filas y elementos del DOM.
- `createElement` para crear nuevos elementos HTML desde JavaScript.
- `addEventListener` para reaccionar a eventos del usuario.
- Manipulación de estilos mediante JavaScript.
- Filtrado de contenido en tiempo real sin recargar la página.

### Objetivo de la parte JavaScript

El objetivo principal de esta parte es mejorar la usabilidad de la aplicación, facilitando la búsqueda de información, la lectura de estados y el seguimiento visual de los registros de calidad.

## Mejoras en el Registro de Acciones y CSS

Se ha optimizado la interfaz de las acciones correctivas para garantizar la coherencia visual y la integridad de los datos en toda la plataforma.

- Enriquecimiento de Datos: Incorporación de columnas para NC Asociada, Responsable y Fecha Prevista, conectando la tabla directamente con los campos del modelo.
- Formateo Profesional: Aplicación de filtros de fecha (d/m/Y) y estilos de "badge" azul para los códigos, facilitando la lectura técnica.
- Consistencia Visual: Unificación del diseño mediante variables CSS y el uso del contenedor main-wrapper para mantener márgenes y sombras uniformes.
- Optimización de Tabla: Ajuste de alineaciones y anchos automáticos que evitan la deformación de la interfaz independientemente del contenido.

## Objetivo de la parte de Acciones y CSS

<<<<<<< HEAD
El objetivo principal es profesionalizar la gestión de datos, permitiendo un control visual rápido de las fechas límite y las vinculaciones entre problemas y soluciones en un entorno estético unificado.
=======
El objetivo principal es profesionalizar la gestión de datos, permitiendo un control visual rápido de las fechas límite y las vinculaciones entre problemas y soluciones en un entorno estético unificado.

## Optimización de Tablas y Navegación
Se han realizado ajustes técnicos en el CSS y en las plantillas HTML para mejorar la lectura de datos y la experiencia de usuario en las secciones críticas.

## Mejoras en CSS (Navegación y Estilos)
Persistencia Visual: Se ha optimizado el selector nav a.active para que la pestaña actual se mantenga resaltada en azul, proporcionando una ubicación clara al usuario.

## Cambios en HTML (Acciones y Responsables)
Lista No Conformidades: Se han integrado nuevas columnas para mostrar la NC Asociada, el Responsable y la Fecha Prevista de un vistazo, evitando clics innecesarios.

Lista de Responsables: Reestructuración de la tabla para unificarla con el diseño general de la aplicación, aplicando las mismas cabeceras y márgenes que en el resto de módulos.
>>>>>>> 828bdb3d5815a66aff7fdbe222ad6acb1b56e4e5

# Ampliaciones Funcionales - Backend (Django)

A. Buscador Simple de Registros

- Permite buscar No Conformidades y Responsables de forma rápida introduciendo un dato clave (como el código o el nombre) en un cuadro de búsqueda.
- Se ha programado un formulario con método GET en el HTML que se conecta con el backend mediante filtros Q de Django para buscar coincidencias exactas o parciales.
- Evita tener que buscar datos a ojo y ahorra tiempo cuando hay muchos registros guardados.

B. Paginación en Tablas y Listados

- Divide las tablas infinitas de No Conformidades, Acciones y Responsables en páginas independientes.
- Se utiliza la clase Paginator de Django en las vistas para limitar los resultados a 10 registros por página. Se ha diseñado una botonera inferior que permite avanzar o retroceder sin perder la búsqueda que esté activa.
- La página web carga muchísimo más rápido y la visualización de los datos es mucho más ordenada y limpia.

C. Registro de Mensajes mediante Logger

- Guarda un historial con todo lo que pasa en el servidor en un archivo de texto seguro (app.log).
- Se ha configurado el sistema logging de Django. Registra accesos rutinarios como informativos (logger.info), y eventos críticos como ediciones o borrados de datos como advertencias (logger.warning), apuntando qué usuario ha hecho la acción.
- Garantiza la seguridad, el control y la trazabilidad de la aplicación ante cualquier fallo o cambio en los datos.