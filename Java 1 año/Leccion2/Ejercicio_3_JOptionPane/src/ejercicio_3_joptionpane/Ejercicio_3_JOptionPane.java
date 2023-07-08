
package Leccion2.Ejercicio_3_JOptionPane.src.ejercicio_3_joptionpane;

import javax.swing.JOptionPane;

public class Ejercicio_3_JOptionPane {


    public static void main(String[] args) {
      
        int numero;
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número: "));
        while (numero != 0){
            if (numero %2 == 0){
                JOptionPane.showMessageDialog(null, "El numero ingresado "+numero+ " ese par");
            }
            else {
                JOptionPane.showMessageDialog(null, "El numero ingresado "+numero+ " ese impar");
            }
           numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro numero: "));
            }
        JOptionPane.showMessageDialog(null, "El numero ingresado "+numero+ " finaliza el programa");
        }
    }
    
//me quede en 1:03:09
