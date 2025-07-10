frutas = ["laranja","maca", "uva"]#valores da lista
print (frutas)

frutas = [] #lista vaziaRun AUTHOR_NAME="fecastilhos22"
Changed files:
fecastilhos22
ERROR: Invalid PR. More or different files than expected were changed.
Error: Process completed with exit code 1.

print(frutas)

letras = list("python") #lista cada letra é um elemento p - y - t...
print(letras)

numeros = list(range(10)) #vai gerar uma lista de 0 a 9
print (numeros)

carro = ["Ferrari", "f8", 420000, 2020, 2900,"São Paulo", True] #atricutos de um carro com string, int e boleano
print(carro)

#LISTA SEMPRE COMEÇA DO 0

#acessando a lista
frutas = ["maca","laranja", "uva","pera"]
frutas[0] # maça
frutas[2] # uva
frutas[-1] # pera número negativo mostra de trás para frente
frutas[-3] # laranja número negativo mostra de trás para frente

#lista aninhada (ex matriz)
matriz = [
    [1,"a", 2],
    ["b", 3, 4],
    [6, 5 , "c"]
]

matriz [0] # [1,"a", 2]
matriz [0][0] # 1
matriz [0][-1] # 2
matriz [-1][-1] # "c"

#fatiamento
lista = ["p","y","t","h","o","n"]

lista[2:] # ["t","h","o","n"]
lista[:2] # ["p","y"]
lista[1:3] # ["y","t"]
lista[0:3:2] # ["p","t"]
lista[::] # ["p","y","t","h","o","n"]
lista[::-1] # ["n", "o", "h", "t", "y", "p"]

#percorrer a lista FOR
carros = ["gol", "celta", "palio"]

for carro in carros:
    print (carro)

for indice,carro in enumerate(carros): #esse contador também inicia em 0
    print(f"{indice}: {carro}")
    
#compressão de listas
numeros = [1, 30, 21, 2, 9, 65, 34]    
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
  
numeros = [1, 30, 21, 2, 9, 65, 34]        
pares = [numero for numeros in numeros if numero % 2 == 0]

#modificando valores
numeros = [1, 30, 21, 2, 9, 65, 34] 
quadrado = []

for numero in numeros:
    quadrado.append(numeros ** 2)
    
numeros = [1, 30, 21, 2, 9, 65, 34] 
quadrado = [numero ** 2 for numero in numeros]    

# métodos em listas
#[].append
lista = []
lista.append(1)
lista.append("Python")
lista.append([40, 30, 20])

print(lista) # [1, "Python", [40, 30, 20]]

#[].clear
lista = [1,"Python", [40, 30, 20]]
print(lista)# [1, "Python", [40, 30, 20]]

lista.clear()
print(lista)

#[].copy
lista = [1,"Python", [40, 30, 20]]
lista.copy()
print(lista) # [1, "Python", [40, 30, 20]]

#[].count conta a quantidade dos mesmos objetos na lista
cores = ["vermelho", "azul", "verde", "azul"] 

cores.count("vermelho") # 1x
cores.count("azul") # 2x
cores.count("verde") # 1x

#[].extend
linguagens = ["python", "js", "c"]
print (linguagens) # ["python", "js", "c"]
linguagens.extend (["java", "csharp"])
print(linguagens) # ["python", "js", "c", "java", "cshap"]

#[].index para saber a PRIMEIRA ocorrência de um número
linguagens = ["python", "js", "c", "java", "cshap"]
linguagens.index("java") # 3
linguagens.index("python") # 0

# [].pop tem que passar qual o indice para ele percorrer
linguagens = ["python", "js", "c", "java", "cshap"]
linguagens.pop() # csharp
linguagens.pop() # java
linguagens.pop() # c
linguagens.pop(0) # python

#[].remove tem que passar qual o objeto para ele percorrer
linguagens = ["python", "js", "c", "java", "cshap"]
linguagens.remove("c")
print(linguagens) # ["python", "js", "c", "java", "cshap"]

#[].sort
linguagens = ["python", "js", "c", "java", "cshap"]
linguagens.sort() # ["c", "csharp", "java", "js", "python"]

linguagens = ["python", "js", "c", "java", "cshap"]
linguagens.sort(reverse=True) # ["python", "js", "java", "csharp", "c" ]

linguagens = ["python", "js", "c", "java", "cshap"]
linguagens.sort(key=lambda x: len(x)) # ["c", "js", "java", "python", "csharp"]

linguagens = ["python", "js", "c", "java", "cshap"]
linguagens.sort(key=lambda x: len(x), reverse=True) # ["python", "csharp", "java", "js", "c"]

#len conta quantas strings no caso
linguagens = ["python", "js", "c", "java", "cshap"]
len(linguagens) #5

#sorted
linguagens = ["python", "js", "c", "java", "cshap"]
sorted(linguagens,key=lambda x: len(x)) # ["c", "js", "java", "python", "csharp"]
sorted(linguagens,key=lambda x: len(x), reverse=True) # ["python", "csharp", "java", "js", "c"]


