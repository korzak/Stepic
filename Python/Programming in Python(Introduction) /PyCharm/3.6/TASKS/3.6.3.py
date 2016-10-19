'''
Имеется набор файлов, каждый из которых, кроме последнего, содержит имя следующего файла.
Первое слово в тексте последнего файла: "We".
'''
import requests
word =''

with open('dataset_3378_3.txt', 'r') as line:  # Открывает файл
    l = line.readline().strip()  # Переменной l присваивается адрес
    print(l)
    r = requests.get(l).text.strip()  # скачивается файл по адресу l
    filename = r

while word != 'We':
    url = 'https://stepic.org/media/attachments/course67/3.6.3/' + filename
    r = requests.get(url).text.strip() #скачивается файл по адресу l
    print(r) #Печатает в консоль содержимое, получаемого файла
    d = r.split() #записывает в список по словам
    if d[0] != 'We':
        with open('out2.txt', 'a') as file:  # Пишит r в out.txt
            file.write(r)
            file.write('\n')
    elif d[0] == 'We':
        word = 'We'
        with open('out3.txt', 'w') as file:  # Пишит r в out.txt
            file.write(r)
    filename = r