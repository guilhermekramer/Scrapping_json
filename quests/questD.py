#list of restaurants located in bronx

from url import getJson
import json


data = getJson()

for line in data:

        try:
            arquivo = json.loads(line)

            if "Bronx" in arquivo["borough"]:
                print(
                    f"restaurant_id: {arquivo['restaurant_id']}, name: {arquivo['name']}, cuisine: {arquivo['cuisine']}, borough: {arquivo['borough']}")
        except json.JSONDecodeError:
            pass
