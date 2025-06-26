#old style % #não é muito utilizada
nome = "Guilherme"
idade = 28
profissao = "Progamador"
linguagem = "Python"
saldo = 45.435

print("Nome: %s Idade: %d" % (nome,idade))



#metodo format

dados = {"nome": "Guilerme", "Idade": 28}
nome = "Guilherme"
idade = 28
profissao = "Progamador"
linguagem = "Python"

print("Nome: {} Idade: {}" .format (nome,idade))
print("Nome: {} Idade: {}" .format (idade,nome))
print("Nome: {1} Idade: {0} Nome: {1} {1}" .format (idade,nome)) #indice
print("Nome: {nome} Idade:{Idade}" .format (**dados))

#fstring
print(f"Nome: {nome} Idade: {idade}")

#formatação
dados = {"nome": "Guilerme", "Idade": 28}
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:10.2f }")