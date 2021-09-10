import requests
from dotenv import load_dotenv
import os

load_dotenv()

APPLICATION_ID = os.getenv("APPLICATION_ID")
APPLICATION_KEY = os.getenv("APPLICATION_KEY")

GENDER = "Man"
WEIGHT_KG = "53"
HEIGHT_CM = "165"
AGE = "40"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APPLICATION_ID,
    "x-app-key": APPLICATION_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)