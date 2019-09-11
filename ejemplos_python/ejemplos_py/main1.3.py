
import requests #Documentación completa de mòdulo requests en: https://2.python-requests.org//es/latest/index.html


#Ejemplo3. Uso del método GET para visualizar atributos de manera dinámica por medio de diccionario

if __name__ == '__main__':
    url = 'http://httpbin.org/get'
    args = {"saludo": "hola", "respuesta": "si"}

    response = requests.get(url, params=args)

    if response.status_code == 200:

        print(response.url)
        print(response.text) #print(help(content))

