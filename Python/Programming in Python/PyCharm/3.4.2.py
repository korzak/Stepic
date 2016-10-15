'''
Напишите программу, которая считывает из файла строку, соответствующую тексту, сжатому с помощью кодирования повторов,
и производит обратную операцию, получая исходный текст.

Запишите полученный текст в файл

Sample Input:
a3b4c2e10b1

Sample Output:
aaabbbbcceeeeeeeeeeb

'''

with open('out.txt') as file:
    s = file.readline().strip()

print(s)  #Печатаем строчку, которую считали из файла

stringforletters = ''  # Создаем пустую переменую строку где будут хранится наши буквы
stringfornumbers = ''  # Создаем пустую переменую строку где будут хранится наши цифры
result = ''
for symbol in s:  # Считываем каждый символ в строке
    if not symbol.isdigit():  # Если символ не цифра то
        stringforletters += symbol  # Добавляем без пробела букву в переменную строку
        stringfornumbers += ' '  # Добавляем пробел где хранятся цифры
    else:
        stringfornumbers += symbol

numberstolist = stringfornumbers.split()  # Преобразуем строку где хранятся цифры в список. Для этого мы добавляли пробелы

i = 0
for symbol2 in stringforletters:  # Перебираем каждый символ в переменной строки где хранятся буквы
    result += symbol2 * int(numberstolist[i])  # Каждую букву умножаем на каждую цифру из списка и склеиваем с переменной строки
    i+=1

print(result)
