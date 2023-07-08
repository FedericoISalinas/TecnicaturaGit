package Leccion1.Ejercicio4.src.ejercicio4;

import java.util.Scanner;

//Ejercicio pedir 2 numeros al usuario y imprimir el mayor con numero termario
public class Ejercicio4 {

    public static void main(String[] args) {
        try (Scanner entrada = new Scanner(System.in)) {
            System.out.println("Digite un numero: ");
            int num1 = Integer.parseInt(entrada.nextLine());
            System.out.println("Digite otro numero: ");
            int num2 = Integer.parseInt(entrada.nextLine());
            System.out.println("El numero mayor es: ");
            System.out.println(num1 > num2 ? num1 : num2);
        } catch (NumberFormatException e) {
           
            e.printStackTrace();
        }
    }

}
