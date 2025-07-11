frutas = ("Laranja", "pera", "uva",) # por uma questão de boas práticas se coloca uma , no final para tupla

letras = tuple ("python")

numeros = tuple ([1, 2, 3, 4])

pais = ("Brasil",)

#acessando a tupla
frutas = ("maçã", "laranja", "uva", "pera",)
frutas [0] # maçã
frutas [2] # uva

frutas [-1] # pera
frutas [-3] # laranja

#tuplas aninhada (ex matriz)
matriz = ( 
    (1,"a", 2),
    ("b", 3, 4),
    (6, 5 , "c"),
)
matriz [0] # (1,"a", 2)
matriz [0][0] # 1
matriz [0][-1] # 2
matriz [-1][-1] # "c"


#fatiamento
lista = ("p","y","t","h","o","n",)

lista[2:] # ["t","h","o","n"]
lista[:2] # ["p","y"]
lista[1:3] # ["y","t"]
lista[0:3:2] # ["p","t"]
lista[::] # ["p","y","t","h","o","n"]
lista[::-1] # ["n", "o", "h", "t", "y", "p"]

#percorrer a tupla FOR
carros = ("gol", "celta", "palio",)

for carro in carros:
    print (carro)

for indice,carro in enumerate(carros): #esse contador também inicia em 0
    print(f"{indice}: {carro}")
        
#[].count conta a quantidade dos mesmos objetos na lista
cores = ("vermelho", "azul", "verde", "azul",)
cores.count("vermelho") # 1x
cores.count("azul") # 2x
cores.count("verde") # 1x   

#[].index para saber a PRIMEIRA ocorrência de um número
linguagens = ("python", "js", "c", "java", "cshap",)
linguagens.index("java") # 3
linguagens.index("python") # 0