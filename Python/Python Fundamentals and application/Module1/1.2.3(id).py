#Получить идентификатор id
x = [1, 2, 3]
y = x
z = x is y #Оператор равенства
print(id(x))
print(id(y))
print(z)
print(id([1, 2, 3]))

print()
a = ["Retention", 3, None]
b = ["Retention", 3, None]
print(a is b) # False

#Изменяется обьект, а не переменная
print()
x = [1, 2, 3]
y = x
print(y is x)
x.append(4)
print(x)
print(y)

print()
x = [1, 2, 3]
y = x
y.append(4)

s = "123"
t = s
t = t + "4"
print(t)
print(s)
print(str(x) + " " + s)

#Тип обьекта
x = [1, 2, 3]
print(type(x))
print(type(4))

#here comes a mindblowing example
print(type(type(x)))
