package Semana2.Leccion02.ArgumentosVariables.src.test.Leccion_2.ArgumentosVariables.src.test;
public class TestArgumentosVariables{
    public static void main(String[] args) {
        imprimirNUmeros(3, 4, 5);
        imprimirNUmeros(1, 2);
        variosParametros("Juan", "Perez", 8, 9);
    }
    private static void variosParametros(String nombre, String apellido, int ...numeros){
        System.out.println("Nombre: "+nombre+" | Apellido: "+apellido);
        imprimirNUmeros(numeros);
    }
    private static void imprimirNUmeros(int ...numeros){
        for (int i =0; i < numeros.length; i++){
            System.out.println("Elementos; "+numeros[i]);
        }
    }
}
