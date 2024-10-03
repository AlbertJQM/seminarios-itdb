import requests
import json
if __name__ == '__main__':
    url = 'https://httpbin.org/post' 
    payload = { 'nombre': 'Fernan','curso':'python','nivel': 'intermedio' }
    headers = { 'çonten-type': 'application/jason'}

    response = requests.post(url, data=json.dumps(payload))
    
    #response = requests.post(url, headers=headers)
    
    print (response.url)
    if response.status_code == 200:
       
       #print(response.content)
       #leer encabezados
       headers_response = response.headers # dic
       #print (headers_response)
       server = headers_response ['Server']
       print (server)