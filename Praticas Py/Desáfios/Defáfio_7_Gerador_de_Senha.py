import random

caracteres = ['0123456789', '!@#$%^&*-_', 'abcdefghijlkmnopqrstuvxwyz', 'ABCDEFGHIJKLMNOPQRSTUVXWYZ']

tam = 10

# juntar todos os caracteres em uma unica string e escolher aleatoriamente
pool = ''.join(caracteres)
senha = ''.join(random.choices(pool, k=tam))

print(pool)
print(senha)

# pool metódo join junta todos os caracteres o separador '(aqui dentro da aspas)'
# dentro da aspas simples vai oque separa as strings neste caso sem nada dentro