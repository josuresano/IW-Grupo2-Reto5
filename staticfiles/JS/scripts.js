document.addEventListener("DOMContentLoaded", () => {

    const filas = document.querySelectorAll("tbody tr");
    filas.forEach(fila => {
        const estado = fila.children[1];
        if (!estado) return;

        const textoEstado = estado.textContent.trim().toLowerCase();
        if (textoEstado.includes("abierta") || textoEstado.includes("pendiente")) {
            estado.style.color = "orange";
            estado.style.fontWeight = "bold";
        } else if (textoEstado.includes("cerrada") || textoEstado.includes("finalizada")) {
            estado.style.color = "green";
            estado.style.fontWeight = "bold";
        }
    });

    const buscador = document.getElementById('buscar');
    const filasTabla = document.querySelectorAll('table tbody tr');

    if (buscador) {

        buscador.addEventListener('input', function() {
            const filtro = buscador.value.toLowerCase();
            let visibles = 0;
            
            filasTabla.forEach(fila => {
                
                if (fila.cells.length > 1 || !fila.textContent.includes("No se encontraron")) {
                    const textoFila = fila.textContent.toLowerCase();
                    if (textoFila.includes(filtro)) {
                        fila.style.display = '';
                        visibles++;
                    } else {
                        fila.style.display = 'none';
                    }
                }
            });
            
            const contadorElem = document.getElementById('contador-registros');
            if (contadorElem) {
                contadorElem.textContent = "Registros visibles: " + visibles;
            }
        });
    }

    const camposCodigo = document.querySelectorAll('input[name*="codigo"], #id_codigo');
    camposCodigo.forEach(campo => {
        campo.addEventListener('input', function() {
            this.value = this.value.toUpperCase();
        });
    });

    const btnAyuda = document.getElementById('btn-ayuda');
    const infoAyuda = document.getElementById('info-ayuda');

    if (btnAyuda && infoAyuda) {
        btnAyuda.addEventListener('click', function(e) {
            e.preventDefault();
            if (infoAyuda.style.display === 'none' || infoAyuda.style.display === '') {
                infoAyuda.style.display = 'block';
                btnAyuda.textContent = 'Ocultar ayuda';
            } else {
                infoAyuda.style.display = 'none';
                btnAyuda.textContent = 'Mostrar ayuda';
            }
        });
    }

    const contenedorTips = document.getElementById('contenedor-tips');
    if (contenedorTips) {
        const tips = ["Revisar fechas", "Códigos en mayúsculas", "Asignar responsable"];
        let htmlStr = "<ul style='color: #3498db; font-weight: bold;'>";
        tips.forEach(function(tip) {
            htmlStr += "<li>" + tip + "</li>";
        });
        htmlStr += "</ul>";
        contenedorTips.innerHTML = htmlStr;
    }

    const titulo = document.querySelector("h1");
    if (titulo && !document.getElementById('subtitulo-js')) {
        const mensaje = document.createElement("p");
        mensaje.id = 'subtitulo-js';
        mensaje.textContent = "Sistema interactivo de gestión de calidad";
        mensaje.style.color = "#3498db";
        mensaje.style.fontStyle = "italic";
        titulo.after(mensaje);
    }
});