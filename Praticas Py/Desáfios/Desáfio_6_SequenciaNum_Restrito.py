#  Escreva um programa que mostre todos os números entre 5 e 100 que são divisíveis por 7, mas não são múltiplos de 5. Os números obtidos devem ser impressos em sequência.

for i in range(5, 100):
    if i % 7 == 0 and i % 5 != 0:
        print(f'São divisíveis por 7: {i}')
        

# Faça um programa que receba um número digitado pelo usuário e calcule a soma de todos os números de 1 até ao número digitado. Por exemplo, se o usuário digitou o número 4, a saída deve ser 10 (1+2+3+4=10).

num = int(input('Digite um valor: '))
soma = 0

for i in range(1, num + 1, 1): # (inicio, fim, passo)
    print(f'{soma} + {i} = {soma + i}')
    soma += i

print('Resultado:', soma)

# forma mais curta, usando a fórmula da soma de uma PA (progressão aritmética):
# num = int(input('Digite um valor: '))
soma = num * (num + 1) // 2
print('Resultado direto:', soma)


# Crie um algoritmo que receba um número, conte o número total de dígitos e mostre o resultado. Por exemplo, se o número é 2021 , então a saída deve ser 4
print('\t ----Contagem dos dígitos---- ')
digitos = int(input("Digite um número para contar seus dígitos : "))
contador = 0
while digitos != 0:
    digitos //= 10
    contador+= 1
print("Total de dígitos = ", contador)