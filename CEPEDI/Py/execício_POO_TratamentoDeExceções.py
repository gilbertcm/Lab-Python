# Data 19/11/25
# ? Exercício CEPEDI - BACK-END
# ? Gilbert Carmo Macêdo

class NotaInvalidaError(ValueError):
    def __init__(self, nota: float):
        self.nota = nota
        msg = f'Nota {nota} invalida: deve estar entre 0 e 10.'
        super().__init__(msg)


class Aluno():
    def __init__(self, nome):
        self.nome = nome
        self.nota = 0
    
    def definir_nota(self, nota: float):  
        try:
            if nota < 0 or nota > 10:
                raise NotaInvalidaError(nota)
            self.nota = nota
            print(f'A nota {nota} foi atualizada com sucesso para {self.nome}!')
        except NotaInvalidaError as e:
            print(e)

# == PROGRAMA PRINCIPAL ==
Aluno = Aluno('Marcos')

Aluno.definir_nota(12)
Aluno.definir_nota(8)