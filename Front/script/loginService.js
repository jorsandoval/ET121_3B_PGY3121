document.getElementById("form").addEventListener("submit", async (e) => {
	e.preventDefault();
	const object = {
		username: document.getElementById("email").value,
		password: document.getElementById("password").value,
	};

	let resultFetch = await fetch("http://localhost:8000/api/v1/Auth/login", {
		body: JSON.stringify(object),
		method: "POST",
		headers: {
			"Content-Type": "application/json",
		},
	}).then((data) => data.json());
	localStorage.setItem("token", resultFetch.token);
	localStorage.setItem("usuario", resultFetch.id);
	window.location = "http://localhost:5500/Front/HTML/Home";
});
