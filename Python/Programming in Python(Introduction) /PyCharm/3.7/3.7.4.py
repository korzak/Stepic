'''
Sample Input:
4
север 10
запад 20
юг 30
восток 40

Sample Output:
20 -20
'''
result = [0,0]
line = []
n = int(input())

for i in range(n):
    line = input().split()
    if line[0] == 'север':
        result[1] += int(line[1])
    elif line[0] == 'юг':
        result[1] -= int(line[1])
    if line[0] == 'восток':
        result[0] += int(line[1])
    elif line[0] == 'запад':
        result[0] -= int(line[1])


print(result[0], end=' ')
print(result[1], end='')