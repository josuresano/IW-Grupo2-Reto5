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

        buscador.addEventListener('input', function () {
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
        campo.addEventListener('input', function () {
            this.value = this.value.toUpperCase();
        });
    });

    const btnAyuda = document.getElementById('btn-ayuda');
    const infoAyuda = document.getElementById('info-ayuda');

    if (btnAyuda && infoAyuda) {
        btnAyuda.addEventListener('click', function (e) {
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
        tips.forEach(function (tip) {
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

if (window.location.pathname === '/' && localStorage.getItem('access_token')) {
    window.location.href = '/inicio/';
}

function validarCampos(username, password) {
    let ok = true;
    document.getElementById('error-username').textContent = '';
    document.getElementById('error-password').textContent = '';
    if (!username.trim() || username.trim().length < 4) {
        document.getElementById('error-username').textContent = 'Usuario demasiado corto (mínimo 4 caracteres).';
        ok = false;
    }
    if (!password || password.length < 4) {
        document.getElementById('error-password').textContent = 'Contraseña demasiado corta (mínimo 4 caracteres).';
        ok = false;
    }
    return ok;
}

async function handleLogin() {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const msgError = document.getElementById('msg-error');
    msgError.style.display = 'none';

    if (!validarCampos(username, password)) return;
    document.getElementById('btn-login').disabled = true;
    try {
        const res = await fetch('/api/token/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ username, password })
        });
        const data = await res.json();
        if (res.ok) {
            localStorage.setItem('access_token', data.access);
            localStorage.setItem('refresh_token', data.refresh);
            window.location.href = '/inicio/';
        } else {
            msgError.textContent = 'Credenciales incorrectas. Inténtalo de nuevo.';
            msgError.style.display = 'block';
        }
    } catch (e) {
        msgError.textContent = 'Error de conexión con el servidor.';
        msgError.style.display = 'block';
    } finally {
        document.getElementById('btn-login').disabled = false;
    }
}


function cerrarSesion() {
    localStorage.removeItem('access_token');
    localStorage.removeItem('refresh_token');
    window.location.href = '/login/';
}

async function fetchConToken(url, opciones = {}) {

    const token = localStorage.getItem('access_token');

    opciones.headers = {
        ...opciones.headers,
        'Authorization': `Bearer ${token}`,
        'Content-Type': 'application/json',
    };

    let res = await fetch(url, opciones);

    if (res.status === 401) {
        const refreshToken = localStorage.getItem('refresh_token');
        if (!refreshToken) { cerrarSesion(); return; }

        const refreshRes = await fetch('/api/token/refresh/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ refresh: refreshToken })
        });

        if (refreshRes.ok) {
            const refreshData = await refreshRes.json();
            localStorage.setItem('access_token', refreshData.access);
            opciones.headers['Authorization'] = `Bearer ${refreshData.access}`;
            res = await fetch(url, opciones);
        } else {
            cerrarSesion();
            return;
        }
    }
    return res;
}