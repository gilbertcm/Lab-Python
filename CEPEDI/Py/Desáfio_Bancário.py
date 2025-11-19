""" Criar uma Classe Bancária
    Contendo: Encapsulamento
              Validações
              métodos de depósito/saque"""
              
class Conta_Bancaria:
    def __init__(self, titular: str, num_conta: str, saldo: float = 0.0, limite: float = 0.0):
        self.titular = titular
        self.__num_conta = num_conta
        self.__saldo = saldo # ou float(saldo)
        self.limite = limite
    
# ------------------------------------ 
#  METÓDOS GETTERS (Somente Leituras)
# ------------------------------------
    @property
    def titular(self) -> str:
        return self.__titular

    @property
    def num_conta(self) -> str:
        return self.__num_conta

    @property
    def saldo(self) -> float:
        """ Saldo atual (somente leitura) """
        return self.__saldo
    
    @property
    def limite(self) -> float:
        return self.__limite
# ---------------------------------------------        
    #  SETTER APENAS PARA O TITULAR
# ---------------------------------------------
    @titular.setter
    def titular(self, novo_titular: str):
        if not novo_titular.strip():
            raise ValueError("O nome do titular não pode ser vazio.")
        if len(novo_titular) < 3:
            raise ValueError("O nome do titular deve conter pelo menos 3 caracteres.")
        self.__titular = novo_titular
    
    @limite.setter
    def limite(self, novo_limite: float):
        if novo_limite < 0:
            raise ValueError("limite não pode ser negativo.")
        self.__limite = novo_limite
# ---------------------------------------------        
    #  METÓDOS DE OPERAÇÃO
# ---------------------------------------------
    def saldo_total_disponivel(self) -> float:
        return self.__saldo + self.__limite

    def deposito(self, valor: float) -> float:
        if valor < 0:
            raise ValueError("O valor de depósito deve ser positivo")
        self.__saldo += float(valor)
        return self.__saldo # Retorna saldo atualizado

    def saque(self, valor: float) -> float:
        if valor <= 0:
            raise ValueError("O valor para saque deve ser positivo")
        if valor > self.saldo_total_disponivel():
            raise ValueError("Saldo + limite insuficiente.")
        self.__saldo -= valor
        return self.__saldo # Retorna saldo atualizado
    
    def transferir(self, valor: float, outra_conta: "Conta_Bancaria") -> None:
        """ Transfere saldo para outra conta.
            A lógica reutiliza o sacar() e depositar() para não duplicar validação."""
        if not isinstance(outra_conta, Conta_Bancaria):
            raise TypeError("Transferência só pode ser feita para outra conta.")
        
        self.saque(valor) # Valida saldo/valor e subtrai
        outra_conta.deposito(valor) # valida depósito e adiciona
    
    # -------------------------
    # SAIDA TELA
    # ------------------------
    def detalhes_conta(self) -> str:
        return (
            f"Titular: {self.__titular}\n"
            f"Conta: {self.__num_conta}\n"
            f"Saldo atual: R${self.__saldo:.2f}\n"
        )
    
    def __str__(self):
        return self.detalhes_conta()
# -----------------------------------------------------
# SEGUNDA CLASSE - HISTÒRICO
# -----------------------------------------------------
class Historico(Conta_Bancaria):
    def __init__(self, titular, num_conta, saldo = 0, limite = 0):
        super().__init__(titular, num_conta, saldo, limite)
        self.__historico = []
        
# ========================
# Getters
# ========================
    @property
    def historico(self) -> list:
        """ Retorna cópia do histórico (para não permitir modificação direta). """
        return list(self.__historico)

# =====================================
        
    def registrar(self, mensagem):
        self.__historico.append(mensagem)
    
    def deposito(self, valor):
        saldo_atual = super().deposito(valor)
        self.registrar(f"Depósito de R${valor:.2f}")
        return saldo_atual
    
    def saque(self, valor):
        saldo_atual = super().saque(valor)
        self.registrar(f"Saque de R${valor:.2f}")
        return saldo_atual
    
    def transferir(self, valor, outra_conta):
        super().transferir(valor, outra_conta)
        destinatario = getattr(outra_conta, "titular", "destinatário")
        self.registrar(f"Transferência de R${valor:.2f} para {destinatario}")
    
    def extrato(self):
        """ Retorna o extrato como string (apresentação na camada de UI). """
        linhas = ["=== EXTRATO ===",
                  f"Titular: {self.titular}",
                  f"Conta: {self.num_conta}",
        ]
        linhas.extend(self.__historico or ["Nenhuma operação registrada."])
        linhas.append(f"Saldo atual: R${self.saldo:.2f}")
        return "\n".join(linhas)
# -----------------------------------------------------
# PROGRAMA PRINCIPAL
# -----------------------------------------------------
print("-=" * 20 + 'BANCO PYTHON' + "-=" * 20)

conta1 = Historico('Gilbert', '1234-0', 2000) #Saldo inicial
conta2 = Historico('Carol', '1234-1', 3000)

#ler campos via getters quando necessário
print(conta1.titular)
print(conta1.num_conta)
print(f"Saldo: R${conta1.saldo:.2f}")

# Operações
conta1.deposito(1200)
conta1.saque(250)
conta1.transferir(777, conta2)

# Mostrar detalhes (apenas na apresentação)
# print(conta1.detalhes_conta())
print()
print(conta1)
print(conta2)

# Alteração direta via setter no titular
conta1.titular = "Gilbert Macedo"
print(conta1)

# Consultar Extrato
print()
print(conta1.extrato())
print()
print(conta2.extrato())