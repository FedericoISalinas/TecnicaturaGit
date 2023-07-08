


import java.util.Scanner;


public class Ejercicio1 {

    
    public static void main(String[] args) {
        //Ejercicio: Tienda de Libros
//2.Digite el nombre del libro
//3.Digite el ID del libro
//4.Digite el precio del libro
//5.Indicar si el envio es Gratuito (True/False)
//6.Mostrar:
//Nombre:
//ID:
//Precio:
//Envío Gratuito?:

        try (Scanner entrada = new Scanner(System.in)) {
            System.out.println("Digite el nombre del Libro: ");
            String nombreLibro = entrada.nextLine();
            System.out.println("Digite el ID del Libro: ");
            int idLibro = Integer.parseInt(entrada.nextLine());
            System.out.println("Digite el Precio del Libro; ");
            double precioLibro = Double.parseDouble(entrada.nextLine());
            System.out.println("Confirme si el envio es Gratuito: ");
            boolean envioGratuito = Boolean.parseBoolean(entrada.nextLine());
            System.out.println(nombreLibro + "  #" + idLibro);
            System.out.println("Precio del Libro: $" + precioLibro);
            System.out.println("El envio del Libro gratuito es: $" + envioGratuito);
        } catch (NumberFormatException e) {
            
            e.printStackTrace();
        }
    }
    
}
