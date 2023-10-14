# restaurants which is located in Bronx after the five first

from url import getJson
import json

contador = 0
data = getJson()

for line in data:

        try:
            arquivo = json.loads(line)

            if "Bronx" in arquivo["borough"]:
                contador+=1
                if contador > 5:
                    print(f"restaurant_id: {arquivo['restaurant_id']}, name: {arquivo['name']}, cuisine: {arquivo['cuisine']}, borough: {arquivo['borough']}")


        except json.JSONDecodeError:
            pass
