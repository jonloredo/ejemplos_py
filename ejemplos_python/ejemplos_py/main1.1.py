import requests #Documentación completa de mòdulo requests en: https://2.python-requests.org//es/latest/index.html

#Ejemplo2. Creación de archivo html

if __name__ == '__main__':
    url = 'https://www.google.com.mx/'
    response = requests.get(url)

    if response.status_code == 200:
       content = response.content
       file = open ('google.html', 'wb')
       file.write(content)
       file.close()
