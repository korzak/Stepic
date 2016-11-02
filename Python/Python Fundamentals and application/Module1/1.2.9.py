#print(1 == True)
#print(True is not 1)

#objects = [1, 2, 1, 2, 3]
objects = [1, 2, 1, 2, 3, True, False, True, False, "true"]
result = []
count = 0
for i in range(len(objects)):
    objects[i] = id(objects[i])
for i in range(len(objects)):
    if objects[i] not in result:
        result.append(objects[i])
print(len(result))

#Вариант 2
objects = [1, 2, 1, 2, 3, True, False, True, False, "true"]
n = len(objects)
ans = n
for i in range(n):
    for j in range(i):
        if id(objects[i]) == id(objects[j]):
            ans -= 1
            break

print(ans)

#Вариант 3
objects = [1, 2, 1, 2, 3, True, False, True, False, "true"]
print(len(set(map(id, objects)))) #Разобрать