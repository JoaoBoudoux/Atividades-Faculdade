import csv
import os

def criar_agenda(arquivo):
    if not os.path.exists(arquivo):
        with open(arquivo, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Nome", "Telefone"])

def adicionar_contato(arquivo, nome, telefone):
    with open(arquivo, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([nome, telefone])
    print(f"Contato {nome} adicionado com sucesso!")

def listar_contatos(arquivo):
    with open(arquivo, 'r') as file:
        reader = csv.reader(file)
        next(reader)  
        for row in reader:
            nome, telefone = row
            print(f"Nome: {nome}, Telefone: {telefone}")

def buscar_contato(arquivo, nome):
    with open(arquivo, 'r') as file:
        reader = csv.reader(file)
        next(reader) 
        encontrado = False
        for row in reader:
            contato_nome, telefone = row
            if contato_nome.lower() == nome.lower():
                print(f"Nome: {contato_nome}, Telefone: {telefone}")
                encontrado = True
                break
        if not encontrado:
            print(f"Contato {nome} não encontrado.")

def remover_contato(arquivo, nome):
    with open(arquivo, 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)
    with open(arquivo, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Nome", "Telefone"])
        removido = False
        for row in rows:
            contato_nome, telefone = row
            if contato_nome.lower() == nome.lower():
                removido = True
            else:
                writer.writerow([contato_nome, telefone])
        if removido:
            print(f"Contato {nome} removido com sucesso!")
        else:
            print(f"Contato {nome} não encontrado.")

def main():
    arquivo_agenda = "agenda.csv"
    criar_agenda(arquivo_agenda)

    while True:
        print("\nEscolha uma opção:")
        print("1. Adicionar contato")
        print("2. Listar contatos")
        print("3. Buscar contato")
        print("4. Remover contato")
        print("5. Sair")
        opcao = input("Digite o número da opção: ")

        if opcao == "1":
            nome = input("Digite o nome do contato: ")
            telefone = input("Digite o telefone do contato: ")
            adicionar_contato(arquivo_agenda, nome, telefone)
        elif opcao == "2":
            print("Contatos na agenda:")
            listar_contatos(arquivo_agenda)
        elif opcao == "3":
            nome = input("Digite o nome do contato a ser buscado: ")
            buscar_contato(arquivo_agenda, nome)
        elif opcao == "4":
            nome = input("Digite o nome do contato a ser removido: ")
            remover_contato(arquivo_agenda, nome)
        elif opcao == "5":
            print("Encerrando a agenda de contatos.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
