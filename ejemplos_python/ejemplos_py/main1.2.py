
import requests #Documentación completa de mòdulo requests en: https://2.python-requests.org//es/latest/index.html


#Ejemplo2. Uso del método GET para visualizar atributos

if __name__ == '__main__':
    url = 'http://httpbin.org/get'
    response = requests.get(url)

    if response.status_code == 200:
        print(response.text) #print(help(content))

