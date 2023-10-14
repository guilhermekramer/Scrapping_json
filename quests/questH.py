#sum function applied for get the score of restaurant

from url import getJson
import json

contador = 0
data = getJson()

for line in data:
    try:
        arquivo = json.loads(line)

        if "grades" in arquivo:
            total_score = sum(entry["score"] for entry in arquivo["grades"])
            contador += total_score
            if 80 <= total_score <=100:
                print(f"restaurant_id: {arquivo['restaurant_id']}, name: {arquivo['name']}, cuisine: {arquivo['cuisine']}, borough: {arquivo['borough']}, score: {total_score}")
    except json.JSONDecodeError:
        pass
