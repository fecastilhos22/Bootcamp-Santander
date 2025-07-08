#Desafio 1
# # Dicionário com os valores de desconto
descontos = {
    "DESCONTO10": 0.10,
    "DESCONTO20": 0.20,
    "SEM_DESCONTO": 0.00
}

# Entrada do usuário
preco = float(input().strip())
cupom = input().strip()

# TODO: Aplique o desconto se o cupom for válido:

if cupom == "DESCONTO10":
    valor_final = preco * (1 - 0.10)
    print(f'{valor_final:.2f}')
elif cupom == "DESCONTO20":
    valor_final = preco * (1 - 0.20)
    print(f'{valor_final:.2f}')
elif cupom == "SEM_DESCONTO":
    print(f'{preco:.2f}')         
else:
      print("Para ativar seu cupom, digite o valor do desconto!")
      
#Desafio 2      
# Entrada do usuário
email = input().strip()

if " " in email:
    print("E-mail inválido")
elif "@" not in email:
    print("E-mail inválido")
elif email.startswith("@") or email.endswith("@"):
    print("E-mail inválido")
else:
    print("E-mail válido")