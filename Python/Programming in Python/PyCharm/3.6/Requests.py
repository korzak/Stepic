#Requests
import requests
r = requests.get('https://example.com') #Простой GET запрос
with open('out1.html','w') as out:
    out.write(r.text) #запись ответа от сервера в файл

url = 'http://example.com'
par = {'key1': 'value1', 'key2': 'value2'}
r = requests.get(url, params=par)#Передача параметров в запрос
with open('out2.html','w') as out:
    out.write(r.url) #Cформированный url-адрес с учетом параметров GET запроса

url = 'http://httpbin.org' #HTTP Request & Response Service
cookies = {'cookies_are': 'working'}
r = requests.get(url, cookies = cookies) #Отправка сформированных cookies на сервер
with open('out3.html','w') as out:
    out.write(r.text)
#print(r.text)

#with open('out4.html','w') as out:
#   out.write(r.cookies[''])
#print(r.cookies['example_cookie_name']) #Использование куки, полученных от сервера