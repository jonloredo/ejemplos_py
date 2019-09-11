
import requests #Documentación completa de mòdulo requests en: https://2.python-requests.org//es/latest/index.html
import json

#Ejemplo8. Uso del método PUT para actualizar un recurso del servidor

if __name__ == '__main__':
    url = 'http://httpbin.org/put' #en url ahora usaremos objeto json POST
    payload = {"saludo": "hola", "respuesta": "si", "nombre": "jon"}
    header = {"content type": 'Application/json', 'access-token': '12345'} #Se agrega dic header

    response = requests.put(url, json=payload, headers=header) #heders se agrega al método 'PUT'
    print(response.url)

    if response.status_code == 200:
        print(response.text)

        print(response.headers) # mostrará elementos de headers accesibles mediante un diccionario.







