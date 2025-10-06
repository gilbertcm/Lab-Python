#Desáfio_2: Verificador de numeros primos
#Solicite um número ao usuário e determine se ele é primo.

#função para verificar se o número é primo
def eh_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True


#variável para armazenar um número
numero = int(input("Digite um numero natural maior que 1 ? "))


if eh_primo(numero):
    print("é primo")
else:
    print("não é primo")