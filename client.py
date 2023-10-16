import requests

response = requests.post('http://127.0.0.1:5000//hello/world/555', json={'json_key': 'value'},
                         headers={'token': 'secret'},
                         params={'k1':'v10', 'k2': 'v20'})
print(response.status_code)
print(response.text)