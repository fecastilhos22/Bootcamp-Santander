

MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

#if
idade = int(input("Informe sua idade? "))

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")

if idade < MAIOR_IDADE:
    print ("Ainda não pode tirar CNH.")    


#else  
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")
else:
    print ("Ainda não pode tirar CNH.")     


#elif    
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")
elif idade >= IDADE_ESPECIAL:
    print("Pode fazer as aulas teóricas, mas não pode fazer as aulas práticas.")    
else:
    print ("Ainda não pode tirar CNH.")


#if aninhado
conta_normal = true
conta_universitaria = False

saque = 2000
saldo = 500
cheque_especial = 450

if conta_normal:
    if saldo>= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial")
    else:
        print("Não foi possível realizar o saque!Saldo insuficiente")   

elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente")    
else:
    print("Sistema não reconheceu seu tipo de conta, entre em contato com seu gerente.")      

#if ternário
saldo = 2000
saque = 500

status = "Sucesso" if saldo >= saque else "Falha"

print (f"{status} ao realizar o saque!")