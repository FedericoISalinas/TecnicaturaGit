package Leccion1.HolaMundo.test.holamundo;


public class HolaMundo {

    public static void main(String[] args) {
        /*System.out.println("Hola Mundo desde Java"); //sout + tab
        
        int miVariable = 10; // tipo de escritura CAMELLO (miVariable)
        System.out.println(miVariable);
        miVariable = 5;
        System.out.println(miVariable);
        //Tipos String = no es un tipo primitivo es una clase
        String miVariableCadena = "Bienvenidos";
        System.out.println(miVariableCadena);
        miVariableCadena = "Sigamos creciendo en programación";
        System.out.println(miVariableCadena);
         */

 /*
        //Var - inferencia de tipos de Java
        var miVariableEntera2 = 10;
        var miVariableCadena2 = "Seguimos Estudiando";
        System.out.println("miVariableEntera2 = " + miVariableEntera2);
        System.out.println("miVariableCadena2 = " + miVariableCadena2); //soutv + tab
        
        //Reglas para definir una variable en Java
        var usuario = "Osvaldo";
        var titulo = "Ingeniero";
        var union = titulo +" "+ usuario;
        System.out.println("union = " + union);
        //click derecho = format = ordena todo el codigo 
        
        
        var a = 8;
        var b = 4;
        System.out.println(usuario + (a + b));
        
        //Ejercicios: Caracteres Especiales con Java
        var nombre = "Natalia";
        System.out.println("Nueva linea: \n"+nombre); // Diagonal iinversa
        System.out.println("Tabulador: \t"+nombre); //Tabulador un espacio para centrar
        System.out.println("\t\t.MENU:.");
        System.out.println("Retroseso: \b\b"+nombre); //Caracter de Retroceso
        System.out.println("Comillas simples: \'"+nombre+"\'");
        System.out.println("Comillas dobles: \""+nombre+"\"");
        
        
        //Clase Scanner
        Scanner entrada = new Scanner(System.in);
        System.out.println("Diguite su nombre: ");
        var usuario2 = entrada.nextLine();
        System.out.println("usuario2 = " + usuario2);
        System.out.println("Escribia el titulo: ");
        var titulo2 = entrada.nextLine();
        System.out.println("Resultado: "+titulo2+" "+usuario2);*/
 /*
        // Clase 4
        byte numEnteroByte = 127;
        System.out.println("numEnteroByte = " + numEnteroByte);
        System.out.println("Valor minimo del Byte:"+ Byte.MIN_VALUE);
        System.out.println("Valor maximo del Byte:"+ Byte.MAX_VALUE);
     
        short numEnteroShort = 32767;
        System.out.println("numEnteroShort = " + numEnteroShort);
        System.out.println("Valor minimo del Short:"+ Short.MIN_VALUE);
        System.out.println("Valor maximo del Short:"+ Short.MAX_VALUE);
        
        int numEnteroInt = 2147483647;
        System.out.println("numEnteroInt = " + numEnteroInt);
        System.out.println("Valor minimo del int"+ Integer.MIN_VALUE);
        System.out.println("Valor maximo del int"+ Integer.MAX_VALUE);
        
  
        long numEntroLong = 9223372036854775807L;
        System.out.println("numEntroLong = " + numEntroLong);
        System.out.println("Valor minimo del long"+ Long.MIN_VALUE);
        System.out.println("Valor maximo del long"+ Long.MAX_VALUE);*/
 /*float numFloat = 3.4028235E38F;
        System.out.println("numFloat = " + numFloat);
        System.out.println("El valor minimo de float:"+ Float.MIN_VALUE);
        System.out.println("El valor maximo de float:"+ Float.MAX_VALUE);
        
        double numDouble = 1.7976931348623157E308D;
        System.out.println("numDouble = " + numFloat);
        System.out.println("El valor minimo de double:"+ Double.MIN_VALUE);
        System.out.println("El valor maximo de double:"+ Double.MAX_VALUE);*/
        //Inferencia de tipos var y tios primitivos 
        /*var numEntero = 20; // Las literlaes sin punto auutomaticamente son de tipo inte
        System.out.println("numEntero = " + numEntero);
        var numFloat = 10.0F; // Automaticamente con el punto se tranforma en tipo double
        System.out.println("numFloat = " + numFloat);
        var numDouble = 10.0;
        System.out.println("numDouble = " + numDouble);*/
 /*
        //Tipos primitivos char
        char miVariableChar = 'a';
        System.out.println("miVariableChar = " + miVariableChar);
        
        char varCaracter = '\u0024';  // Idicamos a Java la asignacion con el codigo unicode
        System.out.println("varCaracter = " + varCaracter);          
        char varCaracterDecimal = 36; // Este es el valor decimal del juego de caracter unicode
        System.out.println("varCaracterDecimal = " + varCaracterDecimal);
        char varCaracterSimbolo = '$'; //UN caracter especial, podemos copiar y pegar desde unicode
        System.out.println("varCaracterSimbolo = " + varCaracterSimbolo);
        
        var varCaracter1 = '\u0024';  // Idicamos a Java la asignacion con el codigo unicode
        System.out.println("varCaracter1 = " + varCaracter1);          
        var varCaracterDecimal1 = (char)36; // Este es el valor Entero y lo asigna como tipo int
        System.out.println("varCaracterDecimal1 = " + varCaracterDecimal1);
        var varCaracterSimbolo1 = '$'; //UN caracter especial, podemos copiar y pegar desde unicode
        System.out.println("varCaracterSimbolo1 = " + varCaracterSimbolo1);
        
        int varEnteoChar = '$';
        System.out.println("varEnteoChar = " + varEnteoChar);
        int caracterchar = 'b'; 
        System.out.println("caracterchar = " + caracterchar);
        
        //Tipos primitivos tipos booleanos
        boolean varBool = true;
        System.out.println("varBool = " + varBool );
        if(varBool){
            System.out.println("La bandera es verde");
        }
        else{
            System.out.println("La bandera es roja");
        }   
        
        //A gotirmo: Es mayor de dada?
        var edad = 18; //Litertal tener presente la inferencia de tipos
        //var adulto = edad>+ 18; //Esta es una exprecion booleana
        if(edad >= 18) {
            System.out.println("Esres mayor de edad");
        }
        else{
            System.out.println("Eres menor de edad");
        }  */
 /*
        //Converciones de tipos primitivos
        var edad = Integer.parseInt("20");
        System.out.println("edad = " + (edad + 1));
        var valorPI = Double.parseDouble("3.1415");
        System.out.println("valorPI =" + valorPI);
        
        //Pedir un valor
        var entrada = new Scanner(System.in);
        System.out.println("Digite su edad: ");
        edad = Integer.parseInt(entrada.nextLine());
        System.out.println("edad = " + edad);*/
 /*
        //Conversion de tipos primitivos de Java Parte 2
        var edadTexto = String.valueOf(10);
        System.out.println("edadTexto = " + edadTexto);
       
        var fesesChar = "programadores".charAt(3);
        System.out.println("fesesChar = " + fesesChar);
        
        System.out.println("Diguite un caracter: ");
        fesesChar = entrada.nextLine().charAt(0);
        System.out.println("fesesChar = " + fesesChar);
        
        //Clase 7
 
        int num1 = 5, num2 = 4;
        var solucion = num1 + num2;
        System.out.println("solucion suma = " + solucion);

        solucion = num1 - num2;
        System.out.println("solucion de la resta = " + solucion);

        solucion = num1 * num2;
        System.out.println("solucion de la multiplicacion = " + solucion);

        solucion = num1 / num2;
        System.out.println("solucion de la division = " + solucion);

        var solucion2 = 3.4 / num2;
        System.out.println("solucion de resultado de la division = " + solucion2);

        solucion = num1 % num2; //Guarda el residuo entero de la division
        System.out.println("solucion = " + solucion); // 5/4

        if (num1 % 2 == 0)
            System.out.println("Es un numero par");
        else 
            System.out.println("Es un numero impar");
         
        
        int varNum1 = 2, varNum2 = 4;
        int varNum3 = varNum1 + 6 - varNum2; // Una operacion
        System.out.println("varNum3 = " + varNum3);

        varNum1 += 1; // varNum1 = varNum1 + 1;
        System.out.println("varNum1 suma = " + varNum1);

        varNum1 -= 2;
        System.out.println("VarNum1 resta = " + varNum1);

        varNum1 /= 2;
        System.out.println("varNum1 division = " + varNum1);

        varNum1 *= 2;
        System.out.println("varNum1 multiplicacion = " + varNum1);
        
        //Clase 8
        //Operadores Unirarios: Cambio de signo
        var varA = 7;
        var varB = -varA;
        System.out.println("varA = " + varA);
        System.out.println("varB = " + varB); // El resultado sera negativo
        
        //Operador de negacion
        var varC = true; //Esta literal por default es de tipo boolean
        var varD = !varC; //Aqui esta invirtiendo el valor
        System.out.println("varC = " + varC);
        System.out.println("!varC = " + !varC);
        
        //Operadores Unarios de incremento: Preincremento
        var varE = 9; // Se va a modificar su valor
        var varF = ++varE; //Simbolo antes de la variable
        //Primero se incrementa la variable y despues se usa su valor
        System.out.println("varF = " + varF);//Se incremente en la unidad
        System.out.println("varF = " + varF);//Va a sumar uno
        
        //Postincremento  (el simbolo va despues de la variable)
        var varG = 3;
        var varH = varG++;
        System.out.println("varG = " + varG);
        System.out.println("varH = " + varH);
               
        //Operadores Unarios de decremento
        var varI = 6;
        var varJ = --varI;
        System.out.println("varI = " + varI);
        System.out.println("varJ = " + varJ);
        
        //Postincremento
        var varK = 8;
        var varL = varK--;
        System.out.println("varK = " + varK); //Aqui va a decrementar en 1
        System.out.println("varL = " + varL);
        
        
       //Operadores de igualdad y relacionales
       var aNum = 5; //Tipo int
       var bNum = 4; // Tipo int
       var cNum = (aNum == bNum);// Por la inferencia de tipo le da un valor booleano
        System.out.println("cNum = " + cNum);
        
        var dNum = aNum != bNum; 
        System.out.println("dNum = " + dNum);
        // cuando se trabaja con cadenas no se usan los ==
       
        var cadenaA = "Hola"; //tipo string
        var cadenaB = "adios"; //tipo string
        var cVar = cadenaA == cadenaB; // compara referencias, no el contenido
        System.out.println("cVar = " + cVar);
 
        var fVar = cadenaA.equals(cadenaB);// .equals compara el contenido, el == referencias
        System.out.println("fVar = " + fVar);
       
         //.equals se usa para tipo string para comparar cadenas, que sean identicas las cadenas
         
        var gVar = aNum >= bNum;
        System.out.println("gVar = " + gVar);
        
        if (aNum % 2 == 0){
            System.out.println("El numero es par");
        }else{
            System.out.println("El numero es impar");
        }
        var edad = 30;
        var adulto = -18;
        if (edad >= adulto){
            System.out.println("Es mayor de edad");
        }
        else {
            System.out.println("Es menor de edad");
        }
        
         
        //Operador condicional AND
        var valorA = 7;
        var valorMinimo = 0;
        var valorMaximo = 10;
        var respuesta = valorA >= 0 && valorA <= 10; // tipo booleano

        if (respuesta) {
            System.out.println("Esta dentro del rango establecido");
        } else {
            System.out.println("Esta fuera del rango establecido");
        }
        
        //Operador condicional OR
        var vacaciones = false;
        var diaLibre = true;
        if(vacaciones || diaLibre)
            System.out.println("Papa puede asistir al juego de su hijo");
        else
            System.out.println("Papa no puede asistir al juego de su hijo");
         
        //Operador termario
        var resultadoT = (5 > 4) ? "verdadero" : "falso"; //compara condiciones segun la condicion, es booleano
        System.out.println("resultadoT = " + resultadoT);

        var numeroT = 5;
        resultadoT = (numeroT % 2 == 0) ? "Es par" : "Es impar";
        System.out.println("resultadoT = " + resultadoT);
       
        var x = 5;
        var y = 10;
        var z = ++x + y--;
        System.out.println("x = " + x); // 5 + 1 = 6
        System.out.println("y = " + y); // 10 - 1 = 9
        System.out.println("z = " + z); // Como lee de izquierda a derecha suma 6 + 10 = 16 antes de que le este 1 a 10
   
        var solucionAritmetica = 4 + 5 * 6 / 3; // 4+(5*6)/3 = 4+(30/3)= 14
        System.out.println("solucionAritmetica = " + solucionAritmetica);
        
        solucionAritmetica = (4 + 5) * 6 / 3; // (9 * 6) /3 = 54/3= 18
        System.out.println("solucionAritmetica = " + solucionAritmetica);
         */
    }
}
