document.addEventListener("DOMContentLoaded", async (event) => {
	const bodyProductos = document.getElementById("body-productos");
	const bodyTotal = document.getElementById("body-total");
	var lista = localStorage.getItem("carrito");
	let total = 0;
	if (lista != "") {
		lista = JSON.parse(lista);
		const unic = lista.reduce(function (obj, name) {
			obj[name] = obj[name] ? ++obj[name] : 1;
			return obj;
		}, {});

		const keys = Object.keys(unic);
		const listOfProducts = Promise.all(
			keys.map(async (element, index) => {
				const result = await (
					await fetch(
						`http://localhost:8000/api/v1/Productos/productos/byId/${element}`
					)
				).json();
				result["total"] = result["valor"] * unic[result.idProducto];
				return result;
			})
		);
		(await listOfProducts).forEach((result, index) => {
			total += result["valor"] * unic[keys[index]];
			bodyProductos.innerHTML =
				bodyProductos.innerHTML +
				`<tr><td>${result.idProducto}</td><td>${result.nombre}</td><td>$${result.valor
				}</td><td>${unic[keys[index]]}</td><td><a href="./verProducto.html?id=${result.idProducto
				}" class="font-weight-bold text-dark">Ver</a></td></tr>`;
		});

		bodyTotal.innerHTML = await `<tr><td>${total}</td><td>${Math.ceil(
			total * 0.19
		)}</td><td>${Math.ceil(
			total * 1.19
		)}</td><td><button type="button" id="pago" class="btn btn-success"style="font-family: cursive" >Pagar</button></td></tr>`;

		document.getElementById("pago").addEventListener("click", async (e) => {
			var user = localStorage.getItem("usuario");
			var token = localStorage.getItem("token");
			if (
				user || token
			) {

				const usuario = Number(localStorage.getItem("usuario"));
				const venta = { usuario: usuario, estadoVenta: 1, totalVenta: total };
				const response = await (
					await fetch("http://localhost:8000/api/v1/Ventas/ventas/", {
						method: "POST",
						body: JSON.stringify(venta),
					})
				).json();

				keys.forEach(async (element) => {
					const detalleVenta = { venta: response.idVenta, producto: element };
					console.log(detalleVenta);
					const responseDetalle = await (
						await fetch("http://localhost:8000/api/v1/Ventas/detalleVentas/", {
							method: "POST",
							body: JSON.stringify(detalleVenta),
						})
					).json();

					const result = await (
						await fetch(
							`http://localhost:8000/api/v1/Productos/productos/byId/${element}`
						)
					).json();
					await fetch(`http://localhost:8000/api/v1/Productos/productos/byId/${element}`, {
						method: "PUT",
						body: JSON.stringify({ stock: result.stock - unic[element] }),
					})
				});


				localStorage.setItem("carrito", "");
				bodyProductos.innerHTML =
					`<tr>
						<td scope="col">Sin producto seleccionado</td>
						<td scope="col"></td>
						<td scope="col"></td>
						<td scope="col"></td>
						<td scope="col"></td>
					</tr>`;
				bodyTotal.innerHTML =
				`<tr>
				<td scope="col">0</td>
				<td scope="col">0</td>
				<td scope="col">0</td>
				<td scope="col"><button type="button" disabled id="pago" class="btn btn-success"style="font-family: cursive" >Pagar</button></td>
				</tr>`;

			} else {
				alert("Debe iniciar sesión para finalizar la compra")
			}
		});
	}
	else {
		bodyProductos.innerHTML =
			bodyProductos.innerHTML +
			`<tr>
				<td scope="col">Sin producto seleccionado</td>
				<td scope="col"></td>
				<td scope="col"></td>
				<td scope="col"></td>
				<td scope="col"></td>
			</tr>`;
	}

});

