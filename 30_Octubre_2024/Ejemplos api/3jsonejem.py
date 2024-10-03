import requests
import json
if __name__ == '__main__':
    url = 'https://httpbin.org/get'
    args = { 'nombre': 'Ferna','curso':'python','nivel': 'intermedio' }
    response = requests.get(url, params=args)
    print (response.url)
    if response.status_code == 200:
        response_json = json.loads (response.text)
        origin = response_json ['origin']
        print (origin)