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

<<<<<<< HEAD
    const tablas = document.querySelectorAll("table");

    tablas.forEach(tabla => {

        const filas = tabla.querySelectorAll("tbody tr");

        const buscador = document.createElement("input");
        buscador.type = "text";
        buscador.placeholder = "Buscar...";
        buscador.style.marginBottom = "15px";

        const limpiar = document.createElement("button");
        limpiar.type = "button";
        limpiar.textContent = "Limpiar";
        limpiar.style.marginLeft = "10px";

        const contador = document.createElement("p");
        contador.style.fontWeight = "bold";
        contador.style.marginTop = "10px";

        tabla.before(buscador);
        buscador.after(limpiar);
        tabla.after(contador);

        function actualizarTabla() {

            const texto = buscador.value.toLowerCase();
            let visibles = 0;

            filas.forEach(fila => {

                const contenido = fila.textContent.toLowerCase();

                if (contenido.includes(texto)) {
                    fila.style.display = "";
                    visibles++;
                } else {
                    fila.style.display = "none";
                }

            });

            contador.textContent = "Registros visibles: " + visibles;
        }

        buscador.addEventListener("keyup", actualizarTabla);

        limpiar.addEventListener("click", () => {
            buscador.value = "";
            actualizarTabla();
        });

        actualizarTabla();

    });

    const estados = document.querySelectorAll(".estado");

    estados.forEach(estado => {

        const texto = estado.textContent.trim().toLowerCase();

        if (texto.includes("finalizada")) {

            estado.style.backgroundColor = "#d4edda";
            estado.style.padding = "5px 10px";
            estado.style.borderRadius = "5px";
            estado.style.color = "#155724";

        }

        else if (texto.includes("pendiente")) {

            estado.style.backgroundColor = "#fff3cd";
            estado.style.padding = "5px 10px";
            estado.style.borderRadius = "5px";
            estado.style.color = "#856404";

        }

    });
=======
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
>>>>>>> c9fded50c96ad0e64791a76fef0a512f23dd08c9

    const titulo = document.querySelector("h1");
    if (titulo && !document.getElementById('subtitulo-js')) {
        const mensaje = document.createElement("p");
        mensaje.id = 'subtitulo-js';
        mensaje.textContent = "Sistema interactivo de gestión de calidad";
        mensaje.style.color = "#3498db";
        mensaje.style.fontStyle = "italic";
        titulo.after(mensaje);
    }
<<<<<<< HEAD

});

if (localStorage.getItem('access_token')) {
    window.location.href = '/';
}

function validarCampos(username, password) {
    let ok = true;
    document.getElementById('error-username').textContent = '';
    document.getElementById('error-password').textContent = '';
    if (!username.trim() || username.trim().length < 3) {
        document.getElementById('error-username').textContent = 'Usuario demasiado corto (mínimo 3 caracteres).';
        ok = false;
    }
    if (!password || password.length < 6) {
        document.getElementById('error-password').textContent = 'Contraseña demasiado corta (mínimo 6 caracteres).';
        ok = false;
    }
    return ok;
}

async function handleLogin() {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const msgError = document.getElementById('msg-error');
}

=======
});
>>>>>>> c9fded50c96ad0e64791a76fef0a512f23dd08c9
