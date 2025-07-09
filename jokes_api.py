import requests

response = requests.get("https://official-joke-api.appspot.com/random_joke")
joke = response.json()

print("Joke of the day:")
print(joke["setup"])
print(joke["punchline"])