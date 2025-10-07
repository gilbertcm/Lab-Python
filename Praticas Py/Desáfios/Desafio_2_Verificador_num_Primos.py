# Código com prints internos para acompanhar o fluxo

def eh_primo(numero):
    print(f"\n🔸 Verificando se {numero} é primo...")

    if numero < 2:
        print(f"❌ {numero} é menor que 2, então não é primo.")
        return False

    limite = int(numero ** 0.5) + 1 #raiz quadrada de numero + 1
    print(f"👉 Vamos testar divisores de 2 até {limite - 1} (raiz de {numero} ≈ {numero ** 0.5:.2f})")

    for i in range(2, limite):
        print(f"  ➡ Testando divisor {i}...", end=" ")
        if numero % i == 0:
            print(f"dividiu exato! {numero} % {i} = 0 → ❌ Não é primo")
            return False
        else:
            print(f"não dividiu ({numero} % {i} = {numero % i})")

    print(f"✅ Nenhum divisor encontrado → {numero} é primo!")
    return True

#variável para armazenar um número
numero = int(input("Digite um numero natural maior que 1 ? "))


if eh_primo(numero):
    print("é primo")
else:
    print("não é primo")
