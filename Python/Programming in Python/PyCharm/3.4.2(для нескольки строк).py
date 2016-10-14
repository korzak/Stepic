stringforletters = ''  # Создаем пустую переменую строку где будут хранится наши буквы
stringfornumbers = ''  # Создаем пустую переменую строку где будут хранится наши цифры
i = 0
with open('dataset_3363_2.txt', 'r') as inf:
    for line in inf:
        result = ''  # Сюда запишем результат и с каждой новой строки эта переменная опять становится пустой

        line = line.strip()
        for symbol in line:  # Считываем каждый символ в строке
            if not symbol.isdigit():  # Если символ не цифра то
                stringforletters += symbol  # Добавляем без пробела букву в переменную строку
                stringfornumbers += ' '  # Добавляем пробел где хранятся цифры
            else:
                stringfornumbers += symbol  # Если символ цифра то добавляем ее в переменую

        numberstolist = stringfornumbers.split()  # Преобразуем строку где хранятся цифры в список. Для этого мы добавляли пробелы

        i = 0
        for symbol2 in stringforletters:  # Перебираем каждый символ в переменной строки где хранятся буквы
            result += symbol2 * int(numberstolist[i])  # Каждую букву умножаем на каждую цифру из списка и склеиваем с переменной строки
            i += 1  # для  чтения каждой цифры из списка мы сделали итератор, который обнуляется с каждым чтением новой строки

with open('outputfile.txt', 'w') as outf:
    outf.write(result)  # Записываем результат в наш файл