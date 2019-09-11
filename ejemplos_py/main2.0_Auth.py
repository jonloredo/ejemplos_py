import requests

payload = {'username' : 'jon', 'password': 'prueba'}
r = requests.get('http://httpbin.org/basic-auth/jon/prueba', auth=('jon','prueba'))

print(r.text)
print(r.status_code)