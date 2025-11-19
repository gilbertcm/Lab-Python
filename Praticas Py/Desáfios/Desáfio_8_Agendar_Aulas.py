# Função para agendar as aulas

def agendar_aulas(classes, horarios):
    grade = []
    
    indice = 0
    
    while indice < len(classes):
        aulas_agendada = classes[indice] + ' - ' + horarios[indice]
        grade.append(aulas_agendada)
        indice += 1
    
    return grade
    
# Programa Principal

materia = []
horario = []

while True:
    mat = input('Digite o nome da materia? ')
    hs = input('Digite um horario para turma? ')
    op = input('Deseja continua? (S - continua, N - Sair): ').upper()
    
    materia.append(mat)
    horario.append(hs)
    
    if op == 'N':
        break

aulas_agendadas = agendar_aulas(materia, horario)

print()
print('-=' * 13, end='SAÍDA')
print('-=' * 13)
for aulas in aulas_agendadas:
    print(aulas)
print('-=' * 26)
    