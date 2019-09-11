
import requests #Documentación completa de mòdulo requests en: https://2.python-requests.org//es/latest/index.html
import json

#Ejemplo4. Regreso de un parámtro json en forma de diccionario

if __name__ == '__main__':
    url = 'http://httpbin.org/get'
    args = {"saludo": "hola", "respuesta": "si"}

    response = requests.get(url, params=args)


    if response.status_code == 200:

        response_json=response.json() #la url regresa parámetros tipo json
        print(response_json)
        origin = response_json['origin']
        print(origin)
        '''
        response_json = json.loads(response.text) #Alternativa para visualizar objeto json mediante manipulación json
        origin = response_json['origin']
        print(origin)
        '''







