document.addEventListener("DOMContentLoaded", () => {


    const filas = document.querySelectorAll("tbody tr");

    filas.forEach(fila => {
        const estado = fila.children[1];

        if (!estado) return;

        const textoEstado = estado.textContent.trim().toLowerCase();

        if (textoEstado.includes("abierta")) {
            estado.style.color = "red";
            estado.style.fontWeight = "bold";
        } else if (textoEstado.includes("cerrada") || textoEstado.includes("finalizada")) {
            estado.style.color = "green";
            estado.style.fontWeight = "bold";
        } else if (textoEstado.includes("proceso") || textoEstado.includes("pendiente")) {
            estado.style.color = "orange";
            estado.style.fontWeight = "bold";
        }
    });

    const tablas = document.querySelectorAll("table");

    tablas.forEach(tabla => {
        const buscador = document.createElement("input");
        buscador.type = "text";
        buscador.placeholder = "Buscar...";
        buscador.style.marginBottom = "15px";

        tabla.before(buscador);

        buscador.addEventListener("keyup", () => {
            const texto = buscador.value.toLowerCase();
            const filas = tabla.querySelectorAll("tbody tr");

            filas.forEach(fila => {
                const contenido = fila.textContent.toLowerCase();
                fila.style.display = contenido.includes(texto) ? "" : "none";
            });
        });
    });

    const tablasPagina = document.querySelectorAll("table");

    tablasPagina.forEach(tabla => {

        const filas = tabla.querySelectorAll("tbody tr");

        const contador = document.createElement("p");

        contador.textContent = "Registros visibles: " + filas.length;

        contador.style.fontWeight = "bold";
        contador.style.marginTop = "10px";

        tabla.after(contador);

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

    const titulo = document.querySelector("h1");

    if (titulo) {

        const mensaje = document.createElement("p");

        mensaje.textContent = "Sistema interactivo de gestión de calidad";

        mensaje.style.color = "#3498db";
        mensaje.style.fontWeight = "bold";

        titulo.after(mensaje);

    }

});