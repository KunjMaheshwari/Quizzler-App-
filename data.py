import requests

question_link = requests.get(
    url="https://opentdb.com/api.php?amount=10&category=18&type=boolean")
question_link.raise_for_status()

question_data = question_link.json()["results"]
