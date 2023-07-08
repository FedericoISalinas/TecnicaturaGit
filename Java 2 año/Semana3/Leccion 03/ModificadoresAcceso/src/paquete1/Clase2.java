package paquete1;

class Clase2 extends Clase1 {
    String atributoDefaul = "Valor del atributo default";

    Clase2() {
        System.out.println("Contructor Default");
    }

    // VIDEO 8
    // public Clase2() {
    // super();
    // this.atributoDefaul = "Modificacion del atributo default";
    // System.out.println("atributoDefault = " + this.atributoDefaul);
    // this.metodoDefault();
    // }

    void metodoDefault() {
        System.out.println("Metodo Default");
    }
}
