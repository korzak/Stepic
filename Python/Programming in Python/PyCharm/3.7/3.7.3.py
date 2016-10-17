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



dictionary = create_dictionary()
text = create_text()
d = []
#
for i in range(len(text)):
    repetition = 0
    for j in range(len(d)):

        if text[i] == d[j]:
            repetition = 1
    if repetition == 0:
        d.append(text[i])

#


for i in range(len(d)):
    exit_code = 1
    for j in range(len(dictionary)):
        if d[i] == dictionary[j]:
            exit_code = 0 #если слово в словаре, то ощибки нет
    if exit_code == 1:
        print(d[i])
