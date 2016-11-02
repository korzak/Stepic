#Вариант 1
s = 0
n = int(input())
for i in range(n):
    s = s+int(input())
print(s)

#Вариант 2
n = int(input())
result = sum(int(input()) for i in range(n))
print(result)