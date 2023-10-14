from url import getJson
import json


data = getJson()
nome_restaurante = []

for line in data:
    try:
        arquivo = json.loads(line)
        if arquivo['name'][:3].lower() =='wil':
            print(f"restaurant_id: {arquivo['restaurant_id']}, name: {arquivo['name']}, cuisine: {arquivo['cuisine']}, borough: {arquivo['borough']}")
    except json.JSONDecodeError:
        pass