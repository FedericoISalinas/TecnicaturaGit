package Semana2.Leccion02.Enumeraciones.src.test;

import Semana2.Leccion02.Enumeraciones.src.Clima;
import Semana2.Leccion02.Enumeraciones.src.Continentes;
import Semana2.Leccion02.Enumeraciones.src.Dias;

public class TestEnumeraciones {
    public static void main(String[] args) {
         System.out.println("Dia 1: "+Dias.MARTES);
         System.out.println("Clima: "+Clima.CALOR);
         indicarDiaSemana(Dias.MARTES); // Las enumeraciones se tratan como cadenas
        // Ahora no se deben utilizar comillas, se accede a traves del operador de punto
         indicarClima(Clima.FRIO);
        System.out.println("Continente No. 4: " + Continentes.AMERICA);
        System.out.println("No. de paises en el 4to Continente: "
                + Continentes.AMERICA.getPaises());
        System.out.println("No. de habitantes en el 4to Continente: "
                + Continentes.AMERICA.getHabitantes());
    }

    private static void indicarDiaSemana(Dias dias) {
        switch (dias) {
            case LUNES:
                System.out.println("Primer dia de la semana");
                break;
            case MARTES:
                System.out.println("Segundo dia de la semana");
                break;
            case MIERCOLES:
                System.out.println("Tercer dia de la semana");
                break;
            case JUEVES:
                System.out.println("Cuarto dia de la semana");
                break;
            case VIERNES:
                System.out.println("Quinto dia de la semana");
                break;
            case SABADO:
                System.out.println("Sexto dia de la semana");
                break;
            case DOMINGO:
                System.out.println("Septimo dia de la semana");
                break;
        }
    }

    private static void indicarClima(Clima clima) {
        switch (clima) {
            case CALOR:
                System.out.println("Dia calido");
                break;
            case FRIO:
                System.out.println("Clima frio");
                break;

        }
    }
}
