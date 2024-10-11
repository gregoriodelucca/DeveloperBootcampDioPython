class ContaBancaria:
    def __init__(self, titular, numero_conta, saldo_inicial=0):
        self.titular = titular
        self.numero_conta = numero_conta
        self.saldo = saldo_inicial

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso!")
        else:
            print("Valor de depósito inválido!")

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso!")
        else:
            print("Saldo insuficiente ou valor inválido!")

    def consultar_saldo(self):
        print(f"Saldo atual: R${self.saldo:.2f}")

    def transferir(self, valor, outra_conta):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            outra_conta.depositar(valor)
            print(f"Transferência de R${valor:.2f} para {outra_conta.titular} realizada com sucesso!")
        else:
            print("Transferência inválida. Verifique o saldo disponível.")
