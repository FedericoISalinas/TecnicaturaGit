// Ejercicio 1: Calcular estacion del año

let Estacion;
let mes = 5;
if (mes == 12 || mes == 1 || mes == 2){
    Estacion = "Verano";
}
else if (mes == 3 || mes == 4 || mes == 5){
    Estacion = "Otoño";
}
else if (mes == 6 || mes == 7 || mes == 8){
    Estacion = "Invierno";
}
else if (mes == 9 || meses == 10 || meses == 11){
    Estacion = "Primavera";
}
else{
    Estacion = ("El valor es incorrecto")
}

console.log("El valor corresponde a la estacion de: " +Estacion);


// Ejercicio 2: Hora del dia
// de 6 a 11 nos saluda: Buen dia
// de 12 a 16 nos saluda: Buenas tardes
// de 17 a 19 nos saluda: Buenas tarde/noche
// de 20 a 23 nos saluda: Buenas noches

let Hora = 7;
let mensaje;

if(Hora >= 6 && Hora <=11){
    mensaje = "Buenos dias";
}
else if(Hora >=12 && Hora <=16){
    mensaje = "Buenas tardes";
}
else if(Hora >= 17 && Hora <= 19){
    mensaje = "Buenas tardes/noches";
}
else if(Hora >= 20 && Hora <= 23){
    mensaje = "Buenas noches";
}
else{
   mensaje = "Hora del dia no correcta"
}

console.log(mensaje)

// Ejercicio 3: Estacion del año con estructura switch(sintaxis igual a Java)

switch(mes){ // No solo se puede utilizar numero, tambien cadenas
    case 1: case 2: case 12:
        Estacion = "Verano";
        break;
    case 3: case 4: case 5:
        Estacion = "Otoño";
        break;
    case 6: case 7: case 8:
        Estacion = "Invierno";
    case 9: case 10: case 11:
        Estacion = "Primavera";
        break;
    default:
        Estacion = "Valor incorrecto";
    }

console.log("Bienvenido a la estacion de: "+Estacion);




