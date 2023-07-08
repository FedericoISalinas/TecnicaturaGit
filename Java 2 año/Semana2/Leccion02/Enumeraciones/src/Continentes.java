package Semana2.Leccion02.Enumeraciones.src;

public enum Continentes {
    AFRICA(54, "1.3 billones "),
    EUROPA(44, "750 millones"),
    ASIA(48,"4.6 billones"),
    AMERICA(35,"1.0 billones"),
    OCEANIA(14,"43 millones");
    
    private final int paises;
    private String habitantes;

    public String getHabitantes() {
        return habitantes;
    }

    public int getPaises() {
        return paises;
    }

    Continentes(int paises, String habitantes){
        this.paises = paises;
        this.habitantes = habitantes;
    }

}
