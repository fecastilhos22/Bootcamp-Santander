//Para ler e escrever dados em java(Padrão DIO):
//new Scanner (System.in): cria um leitor de Entradas, com métodos úteis com prefixo "next";
// System.out.println: imprime um texto de Saída (output) e pulamos uma linha

import java.util.Scanner;

public class Desafio {
    
    public static void main(String[] args) {
        //lê os valores de Entrada:
        Scanner leitorDeEntradas = new Scanner(System.in);
        float valorSalario = leitorDeEntradas.nextFloat();
        float valorBeneficios = leitorDeEntradas.nextFloat();

        float valorImposto = 0;
        if (valorSalario >= 0 && valorSalario <= 1100) {
            //atribiu a aliquota de 5% mediante o salário:
            valorImposto = 0.05F *valorSalario;
        }
        else if (valorSalario >= 1100.01 && valorSalario <= 2500) {
            //atribiu a aliquota de 5% mediante o salário:
            valorImposto = 0.10F *valorSalario;
        }
        else {
            //atribiu a aliquota de 5% mediante o salário:
            valorImposto = 0.55F *valorSalario;
        }
    
        //Calcula e imprime a Saída(com 2 casas decimais):
        float saida = valorSalario - valorImposto + valorBeneficios;
        System.out.println(String.format("%.2f", saida));
    }
}

