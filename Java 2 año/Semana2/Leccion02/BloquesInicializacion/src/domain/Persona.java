package Semana2.Leccion02.BloquesInicializacion.src.domain;
public class Persona {
    private final int idPersona;
    private static int contadorPersonas;

    static{ // bloque de inicializacion estatico
        System.out.println("Ejecucion bloque estatico");
        ++Persona.contadorPersonas;
        // idPersona = 10 | No es un atributo estatico por esto tenemos error|

    }
{//Bloque de inicializacion NO estatico (contexto dinamico)
    System.out.println("Ejecucion de bloque NO estatico");
    this.idPersona = Persona.contadorPersonas++; // Incrementamos el atributo
}

// Los bloques de inicializacion se ejecutan antes del constructor.
public Persona(){
    System.out.println("Ejecucion del constructor");
}
public int getidPersona(){
    return this.idPersona;
}
@Override
public String toString() {
    return "Persona [idPersona=" + idPersona + "]";
}
}
