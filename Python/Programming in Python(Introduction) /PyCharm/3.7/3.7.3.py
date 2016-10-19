'''
Простейшая система проверки орфографии основана на использовании списка известных слов.
Каждое слово в проверяемом тексте ищется в этом списке и, если такое слово не найдено, оно помечается, как ошибочное.

Напишем подобную систему.

Через стандартный ввод подаётся следующая структура: первой строкой — количество d записей в списке известных слов, после передаётся  d
строк с одним словарным словом на строку, затем — количество l строк текста, после чего — l строк текста.

Напишите программу, которая выводит слова из текста, которые не встречаются в словаре.
Регистр слов не учитывается. Порядок вывода слов произвольный. Слова, не встречающиеся в словаре, не должны повторяться в выводе программы.

Sample Input:
3
a
bb
cCc
2
a bb aab aba ccc
c bb aaa

Sample Output:
aab
aba
c
aaa
'''
#Функция создает словарь со словами
def create_dictionary():
    word_count = int(input()) #вводим из скольки слов будет стоять словарь
    dictionary = []
    for i in range(word_count): dictionary.append(input().lower()) #добавляем слова в словарь
    return dictionary

#Функция создает текст
def create_text():
    text = []
    line_count = int(input())
    for line in range(line_count):
        text += input().lower().split()
    return text

#Функция создает текст без повторяющихся слов
def create_text_without_repeats(text):
    twr = [] #text without repeats
    for i in range(len(text)):
        repetition = 0
        for j in range(len(twr)):
            if text[i] == twr[j]:
                repetition = 1
        if repetition == 0:
            twr.append(text[i])
    return twr

dictionary = create_dictionary()
text = create_text()
text_without_repeats = create_text_without_repeats(text)

c = []
c = [i for i in text_without_repeats if i not in dictionary]

for elem in c:
    print(elem, )

'''
# анологично c
for i in range(len(d)):
    exit_code = 1
    for j in range(len(dictionary)):
        if d[i] == dictionary[j]:
            exit_code = 0 #если слово в словаре, то ощибки нет
    if exit_code == 1:
        print(d[i])
'''