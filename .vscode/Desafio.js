//Desafios JavaScript na DIO tem funções "gets" e "print" acessíveis globalmente:
//'gets" : lê UMA linha com dado(s) de entrada (inputs) do usuário;
// "set" :imprime um texto de Saída (Output) e pulando uma linha.



//lê os valores de Entrada:
const valorSalario = parseFloat(gets());
const valorBeneficios = parseFloat(gets());

//calcula o imposto através da função "calcularImposto":
 const valorImposto = valorImposto(valorSalario);

//calcula e mprime a Saída (com 2 casas decimais):
const saida = valorSalario - valorImposto + valorBeneficios; 
prin(saida.toFixed(2));

//Função útil para o calculo do imposto (baseado nas aliquotas).
function calcularImposto(salario) {
    Let aliquota;
    if (salario >= 0 && salario <= 1100){
        aliquota = 0.05;
    }else if (valorSalario >= 1100.01 && valorSalario <= 2500){
        valorImposto = 0.10F * valorSalario;
    }   else {
        valorImposto = 0.15F valorSalario;
    }    
    return aliquota * salario
}





 