#Множества
s = set() #Создание пустого множества
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana' }
print(basket) #{'apple', 'orange', 'banana', 'pear'}
print('orange' in basket) #True
print('python' in basket) #False
'''
Операции с множествами
s.add(element)
s.remove(element) #при отсутствие элемента возникнит ошибка
s.discard(element) #удаляет, если элемента нет, ощибки не возникает
s.clear() #удаляет все элементы из множества
len(s) #число элемнтов в множестве
'''
#Перебор элементов множества
for i in basket:
    print(i)
    #Вывод:
    #banana
    #orange
    #pear
    #apple

