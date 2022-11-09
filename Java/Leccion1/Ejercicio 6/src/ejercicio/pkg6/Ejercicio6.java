
package ejercicio.pkg6;

import java.util.Scanner;


public class Ejercicio6 {

   // Guillermo tiene N dolares. Luis tiene la mitad de lo que tiene Guillermo
    // Juan tiene la mitad de lo que poseen Luis y Guillermo juntos. 
    // Hacer un programa que calcule e imprima la cantida de dinero que
    //tienen entre los tres.
    
    public static void main(String[] args) {
    
        Scanner entrada = new Scanner(System.in);
        float guillermo, luis, juan, total;
        System.out.println("Digite la cantidad de dinero de Guillermo");
        guillermo = Float.parseFloat(entrada.nextLine());
        
        luis = guillermo / 2;
        juan = (luis + guillermo)/ 2;
        total = luis + guillermo + juan;
        System.out.println("El dinero de luis es: US$" + luis);
        System.out.println("El dinero de juan es: US$" + juan);
        System.out.println("El dinero total es: US$" + total);
        
    }
    
}
