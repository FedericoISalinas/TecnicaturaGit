
package ejercicio.pkg5;

import java.util.Scanner;


public class Ejercicio5 {

   //hacer un programa que calcula e imprima la suma de tres calificaciones
    //pedir las calificaciones al usuario
    
    public static void main(String[] args) {
        Scanner entrada = new Scanner (System.in);
        float nota1, nota2, nota3, suma;
        
        //Guardamos las 3 notas
        System.out.println("Digite las tres calificaciones");
        nota1 = Float.parseFloat(entrada.nextLine());
        nota2 = Float.parseFloat(entrada.nextLine());
        nota3 = Float.parseFloat(entrada.nextLine());
        
        suma = nota1 + nota2 + nota3;
        System.out.println("suma = " + suma);
    }
    
}
