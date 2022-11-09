
package ejercicio_3;

import java.util.Scanner;


public class Ejercicio_3 {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numero;
        System.out.println("Digite un número: ");
        numero = Integer.parseInt(entrada.nextLine()); 
        while(numero !=0){
            if(numero % 2 == 0){
        
            System.out.println("El número ingresado "+numero+" es par");
                
    }
            else{
                System.out.println("El numero ingresado "+numero+" es impar");
            }
            System.out.println("Digite otro numero: ");
            numero = Integer.parseInt(entrada.nextLine());
        }
        System.out.println("El número ingresado es "+numero+" finaliza el programa");
    }
}
