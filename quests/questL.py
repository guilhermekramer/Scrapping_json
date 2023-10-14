from url import getJson
import json


data = getJson()
nome_restaurante = []

for line in data:
    try:
        arquivo = json.loads(line)
        tamanho = len(arquivo['name'])-3
        if arquivo['name'][tamanho:].lower() =='ces':
            print(f"restaurant_id: {arquivo['restaurant_id']}, name: {arquivo['name']}")
    except json.JSONDecodeError:
        pass