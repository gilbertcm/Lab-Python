# Exercícios de POO - CEPEDI - BACK-END

# Exercício 1
class Livro:
    
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self. ano = ano
    
    def descricao(self):
        print(f'Titulo: {self.titulo}, Autor: {self.autor}, Ano: {self.ano}')
        
    

meuLivro1 = Livro('Diário de Anny Frank', 'Anny Frank', 1948)
meuLivro2 = Livro('A morte como despertar', 'Indiano', 2002)

meuLivro1.descricao()
meuLivro2.descricao()

# ===================================================================
# Exercício 2
# ===================================================================

class Carro:
    def __init__(self, modelo, ano, velocidade=0):
        self.modelo = modelo
        self.ano = ano
        self.velocidade = velocidade

    def acelerar(self, incremento=10):
        self.velocidade += incremento
    
    def frear(self, decremento=20):
        self.velocidade = max(0, self.velocidade - decremento)

    def mostrar_velocidade(self):
        print(f'Velocidade = {self.velocidade}')
    

meuCarro1 = Carro('Ferrari', 2025, 9)

meuCarro1.acelerar()
meuCarro1.mostrar_velocidade()

meuCarro1.frear()
meuCarro1.mostrar_velocidade()

# ===================================================================
# Exercício 3
# ===================================================================

class Aluno:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        
    def media(self):
        return (self.nota1 + self.nota2) / 2
        
med_Aluno = Aluno('Gilbert', 8.5, 10)

print(f'Média do Aluno {med_Aluno.nome} = {med_Aluno.media():.2f}')

# ===================================================================
# Exercício 4
# ===================================================================


class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo
        
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f'\nCliente: {self.titular}')
            print(f'Depósito de R${valor:.2f}')
            print('Realizado com sucesso!!!')
        else:
            print('Valor para depósito inválido!')
    
    def sacar(self, valor):
        if valor <= 0:
            print('Valor para saque inválido!!!')
            return
        if valor < self.saldo:
            self.saldo -= valor
            print(f'Saque de R${valor:.2f}')
            print('Realizado com sucesso!!!')
        else:
            print('Saldo insuficiente para saque!!!')
    
    def mostrar_saldo(self):
        print(f'\nCliente: {self.titular}\nSaldo disponivel total: R${self.saldo:.2f}')
        
conta1 = ContaBancaria('Gilbert', 100.00)
conta2 = ContaBancaria('Maria', 500)
conta3 = ContaBancaria('Juliana')

# Transação para Gilbert
conta1.depositar(100)
conta1.sacar(75.53)
conta1.mostrar_saldo()

# Transação para Maria
conta2.depositar(60.50)
conta2.sacar(333)
conta2.mostrar_saldo()

# Transação para juliana
conta3.depositar(28.00)
conta3.sacar(39.99)
conta3.mostrar_saldo()

# ===================================================================
# Exercício 4
# ===================================================================


class ConversorTempo:
    def __init__(self, total_segundos):
        self.total_segundos = total_segundos
    
    def converter(self):
        horas, segundos_restantes = divmod(self.total_segundos, 3600)
        return horas, segundos_restantes

# -- Programa Principal -- #

# solicita ao usuário os segundos
segundos_user = int(input('\nDigite o total dos segundos: '))

# Cria o objeto da classe
conversor = ConversorTempo(segundos_user)

# chama o metódo para converter
horas, segundos = conversor.converter()

# Saida
print(f'{horas} Horas e {segundos} Segundos')