//WHILE, comprueba si la condicion es verdadera y despues ejectua el bloque de codigo
let contador = 0;
while(contador <= 4){
    console.log(contador);
    contador++;
}
console.log("Fin del ciclo while");

//DO WHILE, ejecuta al menos una vez el bloque antes de verificar si la condicion es verdadera
let conteo = 0;
do{
    console.log(conteo);
    conteo++;
}while (conteo < 3);
console.log("Fin del ciclo do while");

//FOR, la estructura es la inicializacion, despues condicion y luego incremento/decremento
for(let contando = -1; contando < 3; contando++){ 
    console.log(contando);
}
console.log("Fin del ciclo for");

// BREAK
for(let contando = 3; contando <= 10; contando++){
    if(contando % 2 == 0){ // se utiliza para comprobar si contando es numero par o impar
        console.log(contando); //muestra todos los pares
        break; // termina el bloque de codigo 
    }
}
console.log("Termina el ciclo al encontrar el primer numero par")

// CONTINUE Y ETIQUETAS LABELS
inicio:
for(let contando = 0; contando <= 10; contando++){
    if(contando % 2 !== 0){ // los numeros que no sean pares los ignora y no los imprime
        continue inicio; // ir a la siguiente iteracion
    }
    console.log(contando);
}
console.log("Termina el ciclo")



