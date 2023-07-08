package paquete2;

import paquete1.Clase1;

public class Clase3 extends Clase1 {
    public Clase3() {
        super("protected");
        this.atrubutoProtected = "Accedemos desde la clase hija";
        System.out.println("AtributoProtected = " + this.atrubutoProtected);
        this.atributoPublic = "es totalemnte publico";
    }

}
