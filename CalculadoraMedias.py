def calcular_media(notas):
    if not notas:
        return None

    media = sum(notas) / len(notas)
    
    if media >= 10:
        return media, 'A'
    elif media >= 8:
        return media, 'B'
    elif media >= 7:
        return media, 'C'
    elif media >= 6:
        return media, 'D'
    else:
        return media, 'F'

def main():
    notas = []
    while True:
        nota = input("Digite uma nota (pressione 'q' para finalizar e receber o resultado): ")
        if nota.lower() == 'q':
            break
        try:
            nota = float(nota)
            if 0 <= nota <= 10:
                notas.append(nota)
            else:
                print("Por favor, insira uma nota entre 0 e 10.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido.")

    resultado = calcular_media(notas)

    if resultado:
        media, nota_final = resultado
        print(f"A média das notas é: {media}")
        print(f"A nota correspondente é: {nota_final}")

if __name__ == "__main__":
    main()
