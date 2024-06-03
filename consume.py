import requests

respones = requests.get('http://127.0.0.1:8000/drinks/')
print(respones.json())