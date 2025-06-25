#for/else (quando tiver um número definido de laços de repetição)

texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
        if letra.upper() in VOGAIS:
                print(letra, end="")
else:
    print() #adiciona uma quebra de linha  
    print("Executa no final do laço")              


#função built - in range
    
for numero in range(0, 51, 5)             :
    print(numero,end="")# end para deixar tudo na mesma linha


#while (quando não sabe quantas x será necessário repetir o laço)

opcao = -1

while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0]Sair \n:"))

    if opcao == 1:
            print("Sacando...")
    elif opcao == 2:
          print("Exibindo o extrato...") 
else:
      print("Obrigada por usar nosso sistema bancário, até logo!")


#break (cortar o laço de repetição)
#continue (pula)

while True:
    numero = int(input("Informe um número: "))

    if numero == 10:
            break
    
    print(numero)


while True:
    numero = int(input("Informe um número: "))

    if numero == 10:
          break

    if numero % 2 == 0:
            continue
    

    
    print(numero)


