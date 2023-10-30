class CaixaEletronico:
    def __init__(self):
        self.saldo = 0

    def consultar_saldo(self):
        return self.saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            return f"Depósito de R${valor:.2f} realizado com sucesso. Saldo total: R${self.saldo:.2f}"
        else:
            return "Valor de depósito inválido. Insira um valor positivo."

    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            return f"Saque de R${valor:.2f} realizado com sucesso. Saldo total: R${self.saldo:.2f}"
        elif valor > self.saldo:
            return "Saldo insuficiente."
        else:
            return "Valor de saque inválido. Insira um valor positivo."

def main():
    caixa = CaixaEletronico()

    while True:
        print("\nEscolha uma opção:")
        print("1. Consultar Saldo")
        print("2. Depositar Dinheiro")
        print("3. Sacar Dinheiro")
        print("4. Sair")

        opcao = input("Digite o número da opção: ")

        if opcao == "1":
            print(f"Saldo atual: R${caixa.consultar_saldo():.2f}")
        elif opcao == "2":
            valor = float(input("Digite o valor a ser depositado: "))
            print(caixa.depositar(valor))
        elif opcao == "3":
            valor = float(input("Digite o valor a ser sacado: "))
            print(caixa.sacar(valor))
        elif opcao == "4":
            print("Obrigado por usar o Caixa Eletrônico. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
