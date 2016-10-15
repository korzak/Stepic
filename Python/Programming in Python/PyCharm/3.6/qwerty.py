import requests	
r = requests.get('http://yandex.ru')
print(r.text)