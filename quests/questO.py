from url import getJson
import json


data = getJson()
restaurantes_porcozinha = {}

for line in data:
    try:
        arquivo = json.loads(line)
        cozinhas = arquivo['cuisine']
        bairro = arquivo['borough']

        if cozinhas in restaurantes_porcozinha:
            restaurantes_porcozinha[cozinhas].append({'restaurant_id': arquivo['restaurant_id'], 'borough': bairro})
        else:
            restaurantes_porcozinha[cozinhas] = [{'restaurant_id': arquivo['restaurant_id'], 'borough': bairro}]
    except json.JSONDecodeError:
        pass

cozinhas_sort = sorted(restaurantes_porcozinha.keys())

for cozinha in cozinhas_sort:
    restaurantes = restaurantes_porcozinha[cozinhas]
    restaurantes_ordenados = sorted(restaurantes, key=lambda x: x['borough'], reverse=True)

    print(f"Cozinha: {cozinha}")

    for restaurantes in restaurantes_ordenados:
        print(f"restaurant_id: {arquivo['restaurant_id']}, name: {arquivo['name']}, cuisine: {arquivo['cuisine']}, borough: {arquivo['borough']}")

