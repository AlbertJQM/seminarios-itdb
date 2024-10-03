import requests
if __name__ == '__main__':
    url = 'https://www.google.com.bo/'
    response = requests.get(url)
    print (response)
    if response.status_code == 200:
        print(response.content)
        content = response.content
        file = open ('google.hytml','wb')
        file.write(content)
        file.close()