#taking list of restaurants which havent American cuisine, his grades has value "A" and are located in Brookyn. Sort this list by Reverse=true

from url import getJson
import json


data = getJson()

restaurantes_ordenados = []

for line in data:
    try:
        arquivo = json.loads(line)

        if "grades" in arquivo:
            if arquivo['cuisine'] != 'American' and any(grade['grade'] == 'A' for grade in arquivo['grades']) and arquivo['borough'] != 'Brooklyn':
                restaurantes_ordenados.append(arquivo)
                # print(f"restaurant_id: {arquivo['restaurant_id']}, "
                #       f"name: {arquivo['name']}, "
                #       f"cuisine: {arquivo['cuisine']}, "
                #       f"borough: {arquivo['borough']}, "
                #       f"grades: {arquivo['grades']}")

    except json.JSONDecodeError:
        pass

restaurantes_ordenados = sorted(restaurantes_ordenados,  key=lambda x: x['cuisine'], reverse=True)

for restaurante in restaurantes_ordenados:
    print(f"restaurant_id: {restaurante['restaurant_id']}, name: {restaurante['name']}, cuisine: {restaurante['cuisine']}, borough: {restaurante['borough']}, grades: {restaurante['grades']}")