var lista = localStorage.getItem("carrito");
const unic = lista.reduce(function(obj, name) {
    obj[name] = obj[name] ? ++obj[name] : 1;
    return obj;
}, {})

console.log(unic);