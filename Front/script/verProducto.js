document.addEventListener("DOMContentLoaded", async (e) => {
    const urlParams = new URLSearchParams(window.location.search);
    const idProducto = (urlParams.get('id'));
    const response = await (
    await fetch(`http://localhost:8000/api/v1/Productos/productos/${idProducto}`)
	).json();
    const container = document.getElementById("detalleProduto");
    container.innerHTML = `<div class="row"><div class="d-flex justify-content-center col-lg-6"><img src="../${response.imagen}"alt=" "class="img-fluid"/></div><div class="col-lg-6 d-flex"style="flex-direction: column; justify-content: space-evenly"><h1 class="page-header">${response.nombre}</h1><ul class="list-inline" style="list-style: none"><li><p>$${response.valor}</p></li><li><p>Stock: ${response.stock} Und.</p></li><li><p>${response.detalle}</p></li></ul><button class="btn btn-block"style="background-color: rgb(133, 185, 11); color: #fff"type="submit">Agregar carrito</button></div></div>`
})

