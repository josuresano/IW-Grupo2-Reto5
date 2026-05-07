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

});