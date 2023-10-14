#catchin the restaurants in a repository

from url import getJson
import json

data = getJson()



for line in data:
        try:
            arquivo = json.loads(line)
            if "restaurant_id" in arquivo:
                name = arquivo["name"]
                cuisine = arquivo["cuisine"]
                borough = arquivo["borough"]
                print(f"name: {name}, cuisine: {cuisine}, borough: {borough}")

        except json.JSONDecodeError:
            pass




