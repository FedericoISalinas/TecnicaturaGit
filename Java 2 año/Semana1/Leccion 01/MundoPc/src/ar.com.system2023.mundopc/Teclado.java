// Package: ar.com.system2023.mundopc;

public class Teclado extends DispositivoEntrada {
    private final int idRaton;
    private int idTeclado;
    private static int contadorTeclados;

    public Teclado(String tipoEntrada, String marca) {
        super(tipoEntrada, marca);
        this.idRaton = ++Teclado.contadorTeclados;
        this.idTeclado = this.idRaton;
    }

    @Override
    public String toString() {
        return "Teclado{" + "idTeclado=" + idTeclado + ", " + super.toString() + "}";
    }
}
