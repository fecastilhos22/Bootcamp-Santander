#Maiusculas e minusculas

nome = "GuilHermE"

print(nome.upper()) #todas em letras maiusculas
print(nome.lower()) #todas em minusculas
print(nome.title()) #primeira letra de cada palavra em maiuscula

#eliminando espaços em branco


texto = "  Olá Mundo!     "

print(texto + ".")
print(texto.strip() + ".") #elimina todos os espaços em branco
print(texto.lstrip() + ".") #elimina os espaços a esquerda
print(texto.rstrip() + ".") #elimina os espaços a direita

#junção e centralização

menu = "Python"

print("zzzz" + menu + "zzzz") #colocando espaços em volta
print(menu.center(14)) #centralizando com um número definido 
print(menu.center(14, 'z')) #dividindo os espaços entre
print("P-y-t-h-o-n")#colocando espaços (traços)entre as letras
print("-".join(menu))#sem precisar fazer manualmente(metodos join)