# Estrutura para armazenar dados do cliente
clientes = {}

def criar_conta(nome, saldo_inicial):
    """Cria uma nova conta para o cliente."""
    if nome in clientes:
        print("Conta já existe.")
        return
    clientes[nome] = saldo_inicial
    print(f"Conta criada para {nome} com saldo inicial de R${saldo_inicial:.2f}")

def depositar(nome, valor):
    """Deposita uma quantia na conta do cliente."""
    if nome not in clientes:
        print("Conta não encontrada.")
        return
    if valor <= 0:
        print("Valor para depósito deve ser maior que zero.")
        return
    clientes[nome] += valor
    print(f"R${valor:.2f} depositados na conta de {nome}. Saldo atual: R${clientes[nome]:.2f}")

def sacar(nome, valor):
    """Saca uma quantia da conta do cliente."""
    if nome not in clientes:
        print("Conta não encontrada.")
        return
    if valor <= 0:
        print("Valor para saque deve ser maior que zero.")
        return
    if valor > clientes[nome]:
        print("Saldo insuficiente.")
        return
    clientes[nome] -= valor
    print(f"R${valor:.2f} sacados da conta de {nome}. Saldo atual: R${clientes[nome]:.2f}")

def verificar_saldo(nome):
    """Verifica o saldo da conta do cliente."""
    if nome not in clientes:
        print("Conta não encontrada.")
        return
    print(f"Saldo da conta de {nome}: R${clientes[nome]:.2f}")

# Exemplo de uso
criar_conta("Alice", 1000)
depositar("Alice", 500)
sacar("Alice", 200)
verificar_saldo("Alice")
