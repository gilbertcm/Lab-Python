class Flor:
    def __init__(self, nome): # Não adicionando os parametros, inibi o usuário adicionar um valor ao instanciar o objeto
        self.nome = nome
        self.altura = 0
        self.rega = 0
        
    def regar(self, incremento=2):
        self.altura += incremento
        self.rega += 1
        print('A flor foi regada')
    
    def mostrar_status(self):
        print(f'Nome da flor: {self.nome}')
        print(f'Sua Altura: {self.altura}cm')
        print(f'Quantidade de vezes regada: {self.rega}')
    
    
# Programa principal

flor1 = Flor('Girassol')
flor2 = Flor('Tulipa')

flor1.regar()
flor1.regar()
flor2.regar()

flor1.mostrar_status()
print()
flor2.mostrar_status()
