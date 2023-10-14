import requests

response = requests.post('http://127.0.0.1:5000//hello/world')
print(response.status_code)
print(response.text)