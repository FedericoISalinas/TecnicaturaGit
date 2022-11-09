//Tipo string
 var nombre = "Federico";
 console.log(typeof nombre)
 nombre = 7;
 console.log(typeof nombre)
 nombre = 12.2
 console.log(typeof nombre)
 //Tipo numerico 
 var numero = 3000
 console.log(numero)
 //Tipo objeto 
 var objeto = {
    nombre : "Federico",
    apellido : "Salinas",
    edad : "21",
 }
 console.log(objeto)

 //Tipo de dato boolean
 var bandera = true
 console.log(bandera)
 
 //Tipo de dato funcion
 function esMayordeEdad(edad){
    return edad >= 18;}

 
 console.log(typeof miFuncion);

 //Tipo de dato symbol
 var simbolo = Symbol("Mi simbolo");
 console.log(simbolo);

 //Tipo de dato clase
 class Persona{
    constructor(nombre, apellido){
        this.nombre = nombre;
        this.apellido = apellido;
    }
 }
 console.log(Persona)

 //Tipo de dato undefined
 var x;
 console.log(typeof x);

 x = undefined;
 console.log(x);

 //null: significa ausencia de valor

 var y = null; // null no es un tipo de dato, pero su origen es objet
 console.log(y);

 
 // Tipo de dato array y empty string
 var autos = ["Citroen, Audi, BMW, Ford"];
 console.log(autos);
 console.log(typeof autos);

 var z = "";
 console.log(z)
 console.log(typeof z )