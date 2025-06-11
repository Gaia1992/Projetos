import requests

def obter_previsao(cidade):
    chave_api = 'c9081f510fd5caad1871eea8a6732280'  # Substitua com sua chave
    
    url = f'http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={chave_api}&units=metric&lang=pt_br'

    resposta = requests.get(url)
    print(f'status da API;{resposta.status_code}') #Debug
    dados = resposta.json()

    if dados['cod'] == 200:
        temperatura = dados['main']['temp']
        descricao = dados['weather'][0]['description']
        return f"A previsão para {cidade} é de {temperatura}°C com {descricao}."
    else:
        return "Desculpe, não consegui obter a previsão do tempo."
    
   