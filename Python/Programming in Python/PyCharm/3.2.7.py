def f(x):
    r = x*2
    return (r)


n = int(input())
dictionary = {}
for i in range(n):
    x = int(input())
    if x not in dictionary:
        dictionary[x] = f(x)
    print(dictionary[x])