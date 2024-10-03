import requests
import json
if __name__ == '__main__':
    url = 'https://httpbin.org/post'
    #args = { 'nombre': 'Fernan','curso':'python','nivel': 'intermedio' }
    payload = { 'nombre': 'Fernan','curso':'python','nivel': 'intermedio' }
    #response = requests.post(url, params=args)
    #response = requests.post(url, json=payload)
    response = requests.post(url, data=json.dumps(payload))
    #json postse encarga de serializarlos
    #data nosotros tenemos que serializarlos
    print (response.url)
    if response.status_code == 200:
       print(response.content)