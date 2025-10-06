#Desáfio 4: Tabuada
#Peça ao usuário um número e exiba a tabuada de 1 a 10 para ele.

#Solicita um numero ao usuário
numero = int(input("Digite um número ? "))

#imprime o resultado do 1 ao 10
print(f"Tabuda do {numero}:\n")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}\n")