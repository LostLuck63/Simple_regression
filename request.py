import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'number1':2, 'number2':9})

print(r.json())