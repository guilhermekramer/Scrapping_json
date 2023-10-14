#list of restaurants located in Bronx which his cuisine is or American or Chinese

from url import getJson
import json


data = getJson()


for line in data:
    try:
        arquivo = json.loads(line)

        if arquivo['borough'] == 'Bronx' and (arquivo['cuisine'] == 'American' or arquivo['cuisine'] == 'Chinese'):
            print(f"restaurant_id: {arquivo['restaurant_id']}, name: {arquivo['name']}, cuisine: {arquivo['cuisine']}, borough: {arquivo['borough']}")

    except json.JSONDecodeError:
        pass
