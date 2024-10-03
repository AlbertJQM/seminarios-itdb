import requests
import json
if __name__ == '__main__':
    url = 'https://httpbin.org/delete' 
    payload = { 'nombre': 'Fernan','curso':'python','nivel': 'intermedio' }

    response = requests.delete(url, data=json.dumps(payload))
    
    
    print (response.url)
    if response.status_code == 200:
       
       headers_response = response.headers # dic
       server = headers_response ['Server']
       print (server)