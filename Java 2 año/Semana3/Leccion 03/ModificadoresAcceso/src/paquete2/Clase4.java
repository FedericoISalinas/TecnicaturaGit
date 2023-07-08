package paquete2;

public class Clase4 {
    private String atributoPrivate = "atributo Privado";

    private Clase4() {
        System.out.println("Contructor privado");
    }

    // Creamos un contructor publico para poder crar objetos
    public Clase4(String argumento) { // Aqui se puede llamar la contrucot vacio
        this();
        System.out.println("Contructor publico");
    }

    // Metodo private
    private void metodoPrivado() {
        System.out.println("Metodo privado");
    }

    public String getAtributoPrivate() {
        return atributoPrivate;
    }

    public void setAtributoPrivate(String atributoPrivate) {
        this.atributoPrivate = atributoPrivate;
    }

}
