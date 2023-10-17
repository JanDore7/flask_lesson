import requests

response = requests.post('http://127.0.0.1:5000/user', json={'name': 'Вася', 'password': '1234'})

print(response.status_code)
print(response.text)
