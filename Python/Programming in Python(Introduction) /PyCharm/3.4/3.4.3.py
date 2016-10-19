'''
Напишите программу, которая считывает текст из файла (в файле может быть больше одной строки)
и выводит самое частое слово в этом тексте и через пробел то,
сколько раз оно встретилось. Если таких слов несколько, вывести лексикографически первое (можно использовать оператор < для строк).

Слова, написанные в разных регистрах, считаются одинаковыми.

Sample Input:
abc a bCd bC AbC BC BCD bcd ABC

Sample Output:
abc 3
'''

with open('dataset_3363_3.txt', 'r') as file:
    s = file.read().strip().lower() #читает весь файл в переменную s, преобразуя все в строчные буквы

listofs = s.split() #Создает список из всех слов файла
listofs.sort() #лексикографически сортирует
maxcount = 1
maxword = listofs[0]
count = 0

for i in range(1,len(listofs)): #перебирает каджое слово в списке с 1-ого
    count +=1
    if (i+1 < len(listofs)) and (listofs[i] != listofs[i+1]): #проверка если следующее слово другое
        if count > maxcount:
            maxword = listofs[i]
            maxcount = count
        count = 0

print(maxword+" "+str(maxcount))