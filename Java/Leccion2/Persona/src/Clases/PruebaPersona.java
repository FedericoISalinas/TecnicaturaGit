
package Clases;


public class PruebaPersona {
    public static void main(String[] args) {
        Persona persona1 = new Persona(); // llamamos al constructor
        persona1.nombre = "Federico";
        persona1.apellido = "Salinas";
        persona1.ObtenerInformacion();
        
        System.out.println(" ");
        
        Persona persona2 = new Persona();
        persona2.nombre = "Florencia";
        persona2.apellido = "Arana";
        persona2.ObtenerInformacion();
    }
}
