import javax.management.monitor.Monitor.*;

public class mundoPC {
    public static void main(String[] args) {
        Monitor monitorHP = new Monitor("HP", 13); // Importar la clase
        Teclado tecladoHP = new Teclado("Blutooth", "HP");
        Raton ratonHP = new Raton("Bluetooth", "HP");
        Computadora computadoraHP = new Computadora("Computadora HP", monitorHP, tecladoHP, ratonHP);

        // Creamos otros objetos de diferentes marcas
        Monitor monitorGamer = new Monitor("Gamer", 32);
        Teclado tecladoGamer = new Teclado("Blutooth", "Gamer");
        Raton ratonGamer = new Raton("Bluetooth", "Gamer");
        Computadora computadoraGamer = new Computadora("Computadora Gamer", monitorGamer, tecladoGamer, ratonGamer);

        // Tarea
        Monitor monitorZowie = new Monitor("Zowie", 30);
        Teclado tecladoZowie = new Teclado("Blutooth", "Zowie");
        Raton ratonZowie = new Raton("Bluetooth", "Zowie");
        Computadora computadoraZowie = new Computadora("Computadora Zowie", monitorZowie, tecladoZowie, ratonZowie);

        Orden orden1 = new Orden(); // inicializams el arreglo vacio
        Orden orden2 = new Orden(); // Una nueva lista para el orbjeto orden2
        Orden orden3 = new Orden();
        orden1.agregarComputadora(computadoraHP);
        orden1.agregarComputadora(computadoraGamer);

        Computadora computadoraVarias = new Computadora("Computadoras de diferentes marcas", monitorHP, tecladoGamer,
                ratonHP);
        orden2.agregarComputadora(computadoraVarias);
        orden3.agregarComputadora(computadoraZowie);

        orden1.mostrasOden();
        orden2.mostrasOden();
        orden3.mostrasOden();
    }
}