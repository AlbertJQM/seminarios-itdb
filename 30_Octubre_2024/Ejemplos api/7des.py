import requests
import json
if __name__=='__name__':
    url = ('https://i.eurosport.com/2021/04/29/3123417-64024068-2560-1440.jpg')
    response = requests.get(url, stream=True) # realiza la peticion sin descargar
    with open('image.jpg',"wb") as file:
        for chunk in response.iter_content(): # descarga el contenido poco a poco
            file.write(chunk)

    response.close()