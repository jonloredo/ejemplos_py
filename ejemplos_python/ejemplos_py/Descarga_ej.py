#Programa para realizar descarga de archivo con petición a servidores


import requests

if __name__=='__main__':
    url = 'https://i.imgur.com/TWioz9o.jpg'

    response = requests.get(url, stream=True) # Realiza petición GET a servidores sin descargar contenido; stream = True indica dejar abierta conexión
    with open('imagen.jpeg', 'wb') as file: # Creamos archivo imagen.jpeg con atributos escritura 'w' y forma binaria 'b'.

        for chunk in response.iter_content(): # Método iter_content() toma contenido del servidor (la imagen) y la descarga poco a poco
            file.write(chunk) # pasamos porción 'chunk' usando función objeto file.write()

    response.close() #Cierra conexión a servidores para requerir archivo de URL


