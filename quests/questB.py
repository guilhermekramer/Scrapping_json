#list of restaurants by his ids

from url import getJson
import json


data = getJson()

for line in data:
        try:
            arquivo = json.loads(line)
            if "restaurant_id" in arquivo:
                restaurant_id = arquivo["restaurant_id"]
                name = arquivo["name"]
                cuisine = arquivo["cuisine"]
                borough = arquivo["borough"]
                print(f"restaurant_id: {restaurant_id}, name: {name}, cuisine: {cuisine}, borough: {borough}")

        except json.JSONDecodeError:
            pass

