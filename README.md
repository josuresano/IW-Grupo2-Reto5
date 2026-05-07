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
