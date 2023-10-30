taxas_cambio = {
    "USD": 1.0,
    "EUR": 0.85,
    "GBP": 0.73,
    "JPY": 109.55,
    "BRL": 5.00,
}

def converter_moeda(valor, moeda_origem, moeda_destino):
    if moeda_origem not in taxas_cambio or moeda_destino not in taxas_cambio:
        return "Moeda não suportada."

    taxa_origem = taxas_cambio[moeda_origem]
    taxa_destino = taxas_cambio[moeda_destino]

    valor_convertido = valor * (taxa_destino / taxa_origem)
    return valor_convertido

def main():
    print("Bem-vindo ao Conversor de Moedas!")

    while True:
        valor = float(input("Digite o valor a ser convertido: "))
        moeda_origem = input("Digite a moeda de origem (por exemplo, BRL): ").upper()
        moeda_destino = input("Digite a moeda de destino (por exemplo, EUR): ").upper()

        resultado = converter_moeda(valor, moeda_origem, moeda_destino)
        if isinstance(resultado, str):
            print(resultado)
        else:
            print(f"{valor} {moeda_origem} é igual a {resultado:.2f} {moeda_destino}")

        continuar = input("Deseja fazer outra conversão? (S/N): ").upper()
        if continuar != "S":
            print("Obrigado por usar o Conversor de Moedas!")
            break

if __name__ == "__main__":
    main()
