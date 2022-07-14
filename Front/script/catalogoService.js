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
	document.getElementById("idCategoria").addEventListener("change", (e) => {
        const responseProductos = await (
            await fetch(`http://localhost:8000/api/v1/Productos/productos/`)
        ).json();
		const body = document.getElementById("body");
		for (let i = 0; i < response.length; i += 3) {
			const row = document.createElement("div");
			row.className = "row gx-5";
			for (let j = 0; j < 3; j++) {
				const divProducto = document.createElement("div");
				const item = response[i + j];
				if (item != null) {
					divProducto.className = "col-lg-4 col-md-6 col-sm-12 pt-5";
					divProducto.innerHTML = `<div class="card" style="width: 18rem">
                    <img src="" class="card-img-top" alt="..." />
                    <div class="card-body">
                        <h5 class="card-title">${}</h5>
                        <p class="card-text">${}</p>
                        <p>${}</p>
                        <button
                            type="submit"
                            class="btn btn-success"
                            style="font-family: cursive"
                        >
                            Agregar al carrito
                        </button>
                    </div>
                </div>`;
					row.appendChild(divProducto);
				}
			}
			body.appendChild(row);
		}
	});
});
