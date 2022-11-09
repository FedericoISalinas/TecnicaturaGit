var nombre = "Jose";
var apellido = " Montes";
var nombreCompleto = nombre+" "+ apellido; //Primera concatenacion
console.log(nombreCompleto);

var nombreCompleto2 = "Ariel"+" "+"Betancud"; // Segunda concatenacion
console.log(nombreCompleto2)

var juntos = nombre + 219; //Lee de izq a derecha siguiendo la cadena lee el numero como str
console.log(juntos);
juntos = nombre + (78 + 17) // Si uso parentesis primero suma los numeros y despues concatena los str
console.log(juntos)
var juntos = 219 + nombre + 78 + 17; //Lee de izq a derecha siguiendo la cadena lee el numero como str
console.log(juntos);

nombre +=apellido; // Tercera concatenacion usando el operador simplificado
console.log(nombre)