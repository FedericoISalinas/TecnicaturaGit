
package Leccion2.EjercicioCicloWhite.src.ejerciciociclowhite;




public class EjercicioCicloWhite {

    
    public static void main(String[] args) {
        // Sintaxis de los ciclos while; do while; for
        System.out.println("Ciclo while"); 
        var conteo = 0; // Inferencia de tipos while
        while(conteo < 7){
            System.out.println("conteo = " + conteo);
            conteo++; // Vamos aumentando en uno la variable
        }
        System.out.println(" ");
        System.out.println("Ciclo do while");
        var contador = 0;
        do{
            System.out.println("contador = " + contador);
            contador++;
        }while(contador < 7);
        
        System.out.println(" ");
        System.out.println("Ciclo For usando Break");
            // primer parte para declarar var
            // segunda parte es la condicion
            // tercer parte es para el incremento o el decremento
        for(var contando = 7;contando >= 0;contando--){ 
        
            if(contando % 2 == 0){
            System.out.println("contando = " + contando);
            break;
            }
        }
        System.out.println(" ");
        System.out.println("Ciclo For usando Continue");
         for(var contando = 7;contando >= 0;contando--){ 
        
            if(contando % 2 == 0){
                continue;
            }
            System.out.println("contando = " + contando);
            }
            
    }
}
