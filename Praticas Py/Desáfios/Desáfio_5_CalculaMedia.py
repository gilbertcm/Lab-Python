nota = 0
contador = 0
soma = 0

while nota >= 0 and nota <= 10:
    contador +=1
    nota = float(input(f'Digite a nota {contador}: '))
    if nota >= 0 and nota <= 10:
        soma += nota
        media = soma / contador
        
    
print('A media é:', media)