from url import getJson
import json
from pymongo import MongoClient

def insert_data_into_mongodb(data):
    client = MongoClient('localhost', 27017)
    db = client['code']
    collection = db['restaurants']

data = getJson()

resultados = {}

for line in data:
    try:
        arquivo = json.loads(line)
        if "restaurant_id" in arquivo:
            restaurant_id = arquivo["restaurant_id"]
            name = arquivo["name"]
            cuisine = arquivo["cuisine"]
            borough = arquivo["borough"]

            resultado = {
                "name": name,
                "cuisine": cuisine,
                "borough": borough
            }

            resultados[restaurant_id] = resultado

    except json.JSONDecodeError:
        pass


# Inserir dados no MongoDB
insert_data_into_mongodb(data)
print(data)