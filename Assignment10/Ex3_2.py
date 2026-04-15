import requests
import json

url = "http://127.0.0.1:5000/prime_number/17"
response = requests.get(url).json()

print(json.dumps(response, indent=2))