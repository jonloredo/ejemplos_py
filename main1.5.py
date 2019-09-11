
import requests #Documentación completa de mòdulo requests en: https://2.python-requests.org//es/latest/index.html
import json

#Ejemplo5. Insertar datos dentro de parámetro data en objeto json

if __name__ == '__main__':
    url = 'http://httpbin.org/post' #en url ahora usaremos objeto json POST
    payload = {"saludo": "hola", "respuesta": "si", "nombre": "jon"} #Nuestro diccionario ahora se llamará 'payload'

    response = requests.post(url, json=payload) #ahora el método a usar será 'post' y diccionario se guardarà en parámetro json
    print(response.url)

    if response.status_code == 200:
        print(response.text)







