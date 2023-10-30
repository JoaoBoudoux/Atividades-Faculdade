import random

def escolher_palavra():
    palavras = ["python", "programacao", "computador", "linguagem", "desenvolvimento", "inteligencia", "professor", "jogos"]
    return random.choice(palavras)

def jogar_forca(palavra):
    palavra = palavra.lower()
    letras_corretas = set()
    letras_incorretas = set()
    tentativas = 6

    while True:
        palavra_exibida = ""
        for letra in palavra:
            if letra in letras_corretas:
                palavra_exibida += letra
            else:
                palavra_exibida += "_"

        print("\nPalavra: " + palavra_exibida)
        print("Tentativas restantes: " + str(tentativas))
        print("Letras erradas: " + ", ".join(letras_incorretas))

        if palavra_exibida == palavra:
            print("Parabéns! Você adivinhou a palavra: " + palavra)
            break

        if tentativas == 0:
            print("Você perdeu! A palavra era: " + palavra)
            break

        palpite = input("\nDigite uma letra: ").lower()

        if len(palpite) != 1 or not palpite.isalpha():
            print("Por favor, digite uma única letra válida.")
            continue

        if palpite in letras_corretas or palpite in letras_incorretas:
            print("Você já tentou essa letra.")
            continue

        if palpite in palavra:
            letras_corretas.add(palpite)
        else:
            letras_incorretas.add(palpite)
            tentativas -= 1

if __name__ == "__main__":
    palavra_aleatoria = escolher_palavra()
    print("Bem-vindo ao Jogo da Forca!")
    jogar_forca(palavra_aleatoria)
