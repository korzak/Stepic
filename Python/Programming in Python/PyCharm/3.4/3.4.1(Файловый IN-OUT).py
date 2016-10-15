#Работа с файлами https://pythonworld.ru/tipy-dannyx-v-python/fajly-rabota-s-fajlami.html
#Чтение из файла
#-------Способ 1 ----------------------------
inf = open('file.txt', 'r') #open file.txt
s1 = inf.readline()
s2 = inf.readline()
inf.close()
#---------------------------------------------

#-------Способ 2 (Рекомендуется)---------------
with open('text.txt') as inf:
    s3 = inf.readline()
    s4 = inf.readline()
#здесь файл уже закрыт
#---------------------------------------------

#Пара полезных функций
with open('text.txt') as inf:
    s = inf.readline().strip() #strip()  - убирает все служебные символы при чтении строки
    s5 =inf.readline().strip()
#print('\t abc \n'.strip()) #-> abc

import os
#s.path.join('.','dirname','filename.txt') #-> './dirname/filename.txt' коректное чтение файла в любой системе

#Построчное чтение из файла
with open('text.txt') as file:
    for line in file:
        line = line.strip()
        print(line)

#Запись в файл
#-------Способ 1 ----------------------------
out = open('out.txt','w')
out.write('Some text about me\n')
out.write(str(25)+'\n')
out.close()

#-------Способ 2 (Рекомендуется)---------------
with open('out.txt', 'w') as out:
    out.write('Huuhhhh!!!\n')
    out.write(str(35))
#здесь файл уже закрыт