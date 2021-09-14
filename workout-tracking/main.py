import requests
from dotenv import load_dotenv
import os
from datetime import datetime


load_dotenv()

APPLICATION_ID = os.getenv("APPLICATION_ID")
APPLICATION_KEY = os.getenv("APPLICATION_KEY")

GENDER = "Man"
WEIGHT_KG = "53"
HEIGHT_CM = "165"
AGE = "40"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/060b5eba408e35ff2ea94c648c3705df/workoutTracking/workouts"

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

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)

    print(sheet_response.text)