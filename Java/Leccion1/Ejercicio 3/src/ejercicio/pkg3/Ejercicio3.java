package ejercicio.pkg3;

import java.util.Scanner;

//Ejercicio calcular area de un rectangulo
public class Ejercicio3 {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite el alto del rectangulo");
        int alto = Integer.parseInt(entrada.nextLine());
        System.out.println("Digite el ancho del rectangulo");
        int ancho = Integer.parseInt(entrada.nextLine());
        int Area = alto * ancho;
        int Perimetro = (alto + ancho) * 2;
        System.out.println("Area = " + Area);
        System.out.println("Perimetro = " + Perimetro);

    }

}
