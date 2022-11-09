
package Operaciones;


public class Aritmetica {
    //Atributos de la clase
    int a;
    int b;
    
//Metodo
    public void sumarNumeros(){ // void vacio
        int resultado = a + b;
        System.out.println("resultado = " + resultado);
    }
    
    public int sumarConRetorno (){ // int entero
        //int resultado = a + b
        return a + b;
    }
        
    public int sumarConArgumentos(int a, int b){
        this.a = a; // el argumento "a" se asigna al atributo this.a
        this.b = b;
        //return a + b;
        return sumarConRetorno();
               
    
    
}
}