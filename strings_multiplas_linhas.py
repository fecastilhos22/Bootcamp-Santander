#um boa forma para usar é para fazere menu
nome = "Guilherme"

mensagem = f""" 
Olá meu nome é {nome}, 
Eu estou aprendendo Python
""" 
# Olá meu nome é Guilherme, 
#Eu estou aprendendo Python

print(mensagem)


nome = "Guilherme"  

mensagem = f'''
   Olá meu nome é {nome},
 Eu estou aprendendo Python.
     Essa mensagem tem diferentes recuos.
'''
#   Olá meu nome é Guilherme,
# Eu estou aprendendo Python.    
#   Essa mensagem tem diferentes recuos.

print(
    """
    ============== MENU ============

    1 - Depositar
    2 - Sacar
    0 - Sair

    ================================

            Obrigada por usar nosso sistema!!
"""
)