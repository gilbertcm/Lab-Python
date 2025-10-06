numero = int(input("Digite um número ? "))

#antecessor = numero - 1
#sucessor = numero + 1
print(f"seu numero é o {numero}, seu antecessor é o {(numero-1)} e seu sucessor é o {(numero+1)}")


print("num é {}, o dobro é {}, o triplo é {}, a raiz quadrada é {}"
      .format(numero, (numero*2), (numero*3), (numero**(1/2))))

#média aritmetica
contador = 0
soma = 0
while True:
    num = int(input("digite um numero ? "))
    if num == 0:
        break
    soma += num
    contador += 1

if contador == 0:
    print("Nenhum numero adicionado")
else:
    print("A média aritmetica é {}".format((soma / contador)))