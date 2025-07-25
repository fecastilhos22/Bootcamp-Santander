# Entrada do número de pacientes
n = int(input().strip())

# Lista para armazenar pacientes com ordem de chegada
pacientes = []

# Loop para entrada de dados
for i in range(n):
    nome, idade, status = input().strip().split(", ")
    idade = int(idade)
    pacientes.append((nome, idade, status, i))  # inclui ordem de chegada

# Função que define a prioridade
def prioridade(paciente):
    nome, idade, status, ordem = paciente
    if status == "urgente":
        return (0, -idade, ordem)  # mais urgente, usa ordem como critério secundário
    elif idade >= 60:
        return (1, -idade, ordem)  # idoso
    else:
        return (2, ordem)  # demais

# Ordenar a lista usando a função de prioridade
pacientes.sort(key=prioridade)

# Extrair os nomes dos pacientes na ordem correta
ordem_atendimento = [paciente[0] for paciente in pacientes]

# Exibir a ordem de atendimento
print("Ordem de Atendimento: " + ", ".join(ordem_atendimento))
