import requests

def getJson():
    url = 'https://raw.githubusercontent.com/josenalde/datascience/main/datasets/restaurants.json'
    response = requests.get(url)

    if response.status_code == 200:
        linhas = response.text.split('\n')
        return linhas
    else:
        return print("Erro ao recuperar a página:", response.status_code)



