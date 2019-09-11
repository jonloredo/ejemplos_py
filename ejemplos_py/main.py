import requests #Documentación completa de mòdulo requests en: https://2.python-requests.org//es/latest/index.html

#Ejemplo1. Obtención de respuesta de servidor web.

if __name__ == '__main__':
    url = 'https://www.google.com.mx/'
    response = requests.get(url)

    if response.status_code == 200:
        print(response)

