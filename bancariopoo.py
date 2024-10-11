class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

    def __str__(self):
        return f"Cliente: {self.nome}, CPF: {self.cpf}"


class Conta:
    def __init__(self, cliente, numero_conta):
        self.cliente = cliente
        self.numero_conta = numero_conta
        self.saldo = 0.0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("Valor de depósito deve ser positivo.")

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
        else:
            print("Saque inválido. Verifique o saldo ou o valor.")

    def consultar_saldo(self):
        return self.saldo

    def __str__(self):
        return f"Conta: {self.numero_conta}, Saldo: R${self.saldo:.2f}, {self.cliente}"


class Banco:
    def __init__(self):
        self.contas = {}

    def criar_conta(self, cliente, numero_conta):
        if numero_conta not in self.contas:
            nova_conta = Conta(cliente, numero_conta)
            self.contas[numero_conta] = nova_conta
            print(f"Conta {numero_conta} criada com sucesso para {cliente.nome}.")
        else:
            print("Número da conta já existe.")

    def buscar_conta(self, numero_conta):
        return self.contas.get(numero_conta, None)

# Exemplo de uso
if __name__ == "__main__":
    banco = Banco()

    cliente1 = Cliente("João Silva", "123.456.789-00")
    banco.criar_conta(cliente1, "001")

    conta1 = banco.buscar_conta("001")
    conta1.depositar(1000)
    conta1.sacar(200)
    print(conta1)
