document.addEventListener("DOMContentLoaded", async (e) => {
	const response = await (
		await fetch(`http://localhost:8000/api/v1/Productos/categoria`)
	).json();
	response.forEach((element) => {
		document.getElementById("idCategoria").appendChild(
			new Option(
				element.nombreCategoria.replace(/\b\w/g, (c) => c.toUpperCase()),
				element.idCategoria
			)
		);
	});
	document
		.getElementById("idCategoria")
		.addEventListener("change", async (e) => {
			const responseProductos = await (
				await fetch(
					`http://localhost:8000/api/v1/Productos/productos/byCategoria/${e.target.value}`
				)
			).json();
			const body = document.getElementById("body-card");
			body.innerHTML = "";
			for (let i = 0; i < responseProductos.length; i += 3) {
				const row = document.createElement("div");
				row.className = "row gx-5";
				for (let j = 0; j < 3; j++) {
					const divProducto = document.createElement("div");
					const item = responseProductos[i + j];
					if (item != null) {
						divProducto.className = "col-lg-4 col-md-6 col-sm-12 pt-5";
						divProducto.innerHTML = `<div class="card" style="width: 18rem">
                    <img src="../${
											item.imagen
										}" class="card-img-top" alt="..." />
                    <div class="card-body">
                        <h5 class="card-title">${item.nombre}</h5>
                        <p class="card-text">${
													item.descripcion.length > 50
														? item.descripcion.substr(0, 50).trim() + "..."
														: item.descripcion
												}</p>
                        <p class="font-weight-bold">$${item.valor}</p>
                        <a
                            class="btn btn-success"
                            style="font-family: cursive"
							href="./verProducto.html?id=${item.idProducto}"
                        >
                            Ver Producto
                        </a>
                    </div>
                </div>`;
						row.appendChild(divProducto);
					}
				}
				body.appendChild(row);
			}
		});
});
