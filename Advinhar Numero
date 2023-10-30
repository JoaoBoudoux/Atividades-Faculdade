import random

def adivinhar_numero():
    numero_secreto = random.randint(1, 100)
    tentativas = 0

    print("Bem-vindo ao jogo Adivinhe o Número!")
    print("Tente adivinhar o número secreto entre 1 e 100.")

    while True:
        tentativa = int(input("Digite sua tentativa: "))
        tentativas += 1

        if tentativa < numero_secreto:
            print("\nTente um número maior.")
        elif tentativa > numero_secreto:
            print("\nTente um número menor.")
        else:
            print(f"Parabéns! Você adivinhou o número {numero_secreto} em {tentativas} tentativas.")
            break

if __name__ == "__main__":
    adivinhar_numero()
