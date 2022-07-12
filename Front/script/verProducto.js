document.addEventListener("DOMContentLoaded", async (e) => {
    const urlParams = new URLSearchParams(window.location.search);
    const idProducto = (urlParams.get('id'));
    const response = await (
    await fetch(`http://localhost:8000/api/v1/Productos/productos/${idProducto}`)
	).json();
    const container = document.getElementById("detalleProduto");
    container.innerHTML = `<div class="row"><div class="d-flex justify-content-lg-end col-lg-12"><img src="../${response.imagen}" alt="" class="img-fluid"/></div></div><div class="col-lg-12"><h1 class="page-header d-flex justify-content-lg-between">${response.nombre}</h1></div><div><ul class="list-inline" style="list-style: none;"><li><p>$${response.valor}</p></li><li><p>Stock: ${response.stock} Und.</p></li><li><p>${response.descripcion}</p></li></ul></div><div><form action="#" method="get"><button class="btn btn-primary" type="submit">Agregar carrito</button></form></div>`
})

