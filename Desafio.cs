//Para ler e escrever dados em C# utilizamos os seguintes métodos da classe Console:
//Console.ReadLine :  Lê UMA linha com dado(s) de Entrada (Inputs) do usuário;
// Console.WriteLine:imprime um texto de Saída (Output) e pulando uma linha.


using System;

public class Desafio
{
    public static void Main()
    {
        //lê os valores de Entrada:
        float valorSalario = float.Parse(Console.ReadLine());
        float valorBeneficios = float.Parse(Console.ReadLine());

        float valorImposto = 0;
        if (valorSalario >= 0 && valorSalario <= 1100)
        {
            //atribiu a aliquota de 5% mediante o salário:
            valorImposto = 0.05F * valorSalario;
        }
        else if (valorSalario >= 1100.01 && valorSalario <= 2500)
        {
            //atribiu a aliquota de 5% mediante o salário:
            valorImposto = 0.10F * valorSalario;
        }
        else
        {
            //atribiu a aliquota de 5% mediante o salário:
            valorImposto = 0.55F * valorSalario;
        }

        //Calcula e imprime a Saída(com 2 casas decimais):
        float saida = valorSalario - valorImposto + valorBeneficios;
        Console.WriteLine(saida.ToString("0.00"));
    }
}
