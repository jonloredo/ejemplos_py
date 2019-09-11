#Este es un ejemplo de como obtener hora de API http://worldtimeapi.org/
import requests

url = 'http://worldtimeapi.org/api/timezone/America/Mexico_City'

r=requests.get(url)


consulta = r.json()

#consulta = r.headers

print(consulta)

#print(consulta['timezone'])

