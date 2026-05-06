# IW-Grupo2-Reto5
### Enlace al repositorio GitHub: 
https://github.com/josuresano/IW-Grupo2-Reto5


---  
  
# Control_Calidad_Industria — Visión General del Proyecto  
  
El proyecto **Control_Calidad_Industria** es un sistema web de gestión de calidad industrial diseñado para hacer seguimiento de **No Conformidades (NC)** y sus **Acciones Correctivas (AC)** asociadas. Construido con el framework Django, la aplicación facilita el seguimiento de calidad al estilo ISO, gestionando el ciclo de vida de los problemas de calidad: desde la identificación y evaluación de severidad hasta la asignación de responsables y el seguimiento de la resolución.  
  
## Propósito y Contexto del Dominio  
  
El sistema actúa como repositorio centralizado de datos de calidad industrial. Permite a los responsables de calidad:  
  
- Registrar y categorizar No Conformidades (NC) con metadatos específicos como origen, severidad y procesos afectados.  
- Asignar múltiples **Responsables** a problemas de calidad concretos.  
- Hacer seguimiento de la ejecución de Acciones Correctivas (AC) vinculadas a NCs específicas, incluyendo fechas de finalización planificadas y reales.  
- Monitorizar KPIs globales de calidad a través de un panel de control centralizado.  
  
## Stack Tecnológico  
  
El proyecto utiliza un stack moderno basado en Python, con foco en la simplicidad y portabilidad para entornos industriales.  
  
| Componente | Tecnología | Versión |  
| :--- | :--- | :--- |  
| **Framework** | Django | 6.0.4 |  
| **Lenguaje** | Python | 3.x |  
| **Base de datos** | SQLite3 | 3.x |  
| **Utilidades** | sqlparse, tzdata, asgiref | Última (vía pip) |  
  
---  
  
## Arquitectura de Alto Nivel  
  
El proyecto sigue el patrón estándar de Django **Modelo-Vista-Plantilla (MVT)**. Está estructurado en un paquete de configuración principal (`Control_Calidad_Industria`) y un paquete de lógica de aplicación primario (`Gestion_NC`).  
  
### Diagrama de Componentes del Sistema  
  
Este diagrama relaciona los requisitos del sistema con las entidades de código definidas en el proyecto.  
  
**Mapeo del Sistema de Gestión de Calidad**  
  
```mermaid  
graph TD  
    subgraph "Dominio Industrial"  
        A["Problema de Calidad (NC)"]  
        B["Tarea de Resolución (AC)"]  
        C["Responsable de Calidad"]  
        D["Panel de KPIs"]  
    end  
  
    subgraph "Entidades de Código (Proyecto Django)"  
        A1["Clase [NoConformidad]"]  
        B1["Clase [AccionCorrectiva]"]  
        C1["Clase [Responsable]"]  
        D1["Función [calcular_datos_globales]"]  
        E1["[db.sqlite3]"]  
    end  
  
    A --- A1  
    B --- B1  
    C --- C1  
    D --- D1  
  
    A1 --> E1  
    B1 --> E1  
    C1 --> E1
