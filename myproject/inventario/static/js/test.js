document.addEventListener('DOMContentLoaded', () => {
    ListarCategorias();
});

function ListarCategorias() {
    fetch("http://127.0.0.1:8000/categorias/", {
        method: "GET",
        headers: {
            "Content-Type": "application/json"
        }
    })
    .then(response => response.json())
    .then(datos => {
        let tabla = document.querySelector('#tabla-categorias-body');
        tabla.innerHTML = "";

        if (datos.length === 0) {
            tabla.innerHTML += `<tr><td colspan="3">No hay datos</td></tr>`;
        } else {
            for (let dat of datos) {
                tabla.innerHTML += `
                <tr>
                    <td>${dat.id}</td>
                    <td>${dat.nombre}</td>
                    <td>${dat.descripcion}</td>
                </tr>`;
            }
        }
    })
    .catch(error => {
        console.error('Error al obtener las categorías:', error);
    });
}
