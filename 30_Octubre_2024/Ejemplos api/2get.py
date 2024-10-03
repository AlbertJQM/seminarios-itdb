import requests
if __name__ == '__main__':
    url = 'https://httpbin.org/get?nombre=Fernan&curso=Python'
    #url = 'https://httpbin.org/get'
    #args = { 'nombre': 'Ferna','curso':"python" }
    response = requests.get(url, params=args)
    #print (response.url)
    if response.status_code == 200:
        content = response.content
        print (content)