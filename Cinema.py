def exibir_filmes():
    filmes = {
        "1": {"titulo": "Filme A", "horario": "10:00"},
        "2": {"titulo": "Filme B", "horario": "14:00"},
        "3": {"titulo": "Filme C", "horario": "18:00"}
    }
    print("Escolha um filme e horário:")
    for chave, filme in filmes.items():
        print(f"{chave}. {filme['titulo']} - {filme['horario']}")

def fazer_reserva():
    exibir_filmes()
    escolha = input("Digite o número do filme desejado: ")
    quantidade_ingressos = int(input("Quantos ingressos deseja comprar? "))

    filmes = {
        "1": {"titulo": "Filme A", "horario": "10:00"},
        "2": {"titulo": "Filme B", "horario": "14:00"},
        "3": {"titulo": "Filme C", "horario": "18:00"}
    }

    if escolha in filmes:
        filme_escolhido = filmes[escolha]
        with open("reservas.txt", "a") as arquivo:
            for _ in range(quantidade_ingressos):
                arquivo.write(f"Filme: {filme_escolhido['titulo']}, Horário: {filme_escolhido['horario']}\n")
        print(f"Reserva efetuada com sucesso para o filme {filme_escolhido['titulo']} às {filme_escolhido['horario']}.")

def exibir_reservas():
    try:
        with open("reservas.txt", "r") as arquivo:
            reservas = arquivo.readlines()
        if not reservas:
            print("Nenhuma reserva encontrada.")
        else:
            print("Reservas:")
            for reserva in reservas:
                print(reserva.strip())
    except FileNotFoundError:
        print("Nenhuma reserva encontrada.")
def main():
    while True:
        print("\nEscolha uma opção:")
        print("1. Fazer reserva")
        print("2. Exibir reservas")
        print("3. Sair")

        opcao = input("Digite o número da opção desejada: ")

        if opcao == "1":
            fazer_reserva()
        elif opcao == "2":
            exibir_reservas()
        elif opcao == "3":
            print("Obrigado por usar o sistema de reservas de cinema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if _name_ == "_main_":
    main()
