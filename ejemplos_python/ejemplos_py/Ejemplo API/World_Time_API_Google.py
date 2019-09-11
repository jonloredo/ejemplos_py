#Este es un ejemplo de como obtener hora de API Google https://developers.google.com/maps/documentation/timezone/intro
import requests

url = 'http://maps.googleapis.com/maps/api/geocode/json?address=sanjose'

r=requests.get(url)

print(r.text)


