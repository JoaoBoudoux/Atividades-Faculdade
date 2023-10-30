import requests

def consultar_previsao_tempo(api_key, cidade):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        temperatura = data["main"]["temp"]
        descricao = data["weather"][0]["description"]
        print(f"Previsão do tempo em {cidade}:")
        print(f"Temperatura: {temperatura}°C")
        print(f"Condição: {descricao}")
    else:
        print("Não foi possível obter a previsão do tempo.")

def main():
    api_key = "b57a5f1e14eb66d798212962be582e85"
    cidade = input("Digite o nome da cidade para consultar a previsão do tempo: ")

    consultar_previsao_tempo(api_key, cidade)

if __name__ == "__main__":
    main()
