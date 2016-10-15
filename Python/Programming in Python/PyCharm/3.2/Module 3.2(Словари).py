#Словари
'''
Словари в Python - неупорядоченные коллекции произвольных объектов с доступом по ключу.
Их иногда ещё называют ассоциативными массивами или хеш-таблицами.
Позволяет хранить пары <ключ, значение>
'''
d = {'a': 123, 10: 100}
print(d['a'])
print(d[10])
'''
Операции со словарями
    dictionary = {}
    key in dictionary
    key not in dictionary
    dictionary[key] = value
    dictionary[key] #Возникнет ошибка
    dictionary.get(key) #Ошибка не возникнет, если ключа нет, вернет None
    del dictionary[key] #Удалить по ключу


'''

if 'a' in d:
    print("key 'a' here!")
if 'qwerty' not in d:
    print("Sorry, key 'qwerty is not!")


#Перебор элементов словаря
d = {'C': 14, 'A': 12, 'T': 9, 'G': 18}
for key in d:
    print(key, end=' ') #T C G A (порядок всегда произвольный)
print(" | ", end='')
for key in d.keys():
    print(key, end=' ') #T C G A (порядок всегда произвольный)
print()
for values in d.values():
    print(values, end=' ') #14 12 18 9 (порядок всегда произвольный)
print()
for key, value in d.items():
    print(str(key)+":"+ str(value), end=' ')
