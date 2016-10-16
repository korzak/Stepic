'''
Sample Input:
3
Зенит;3;Спартак;1
Спартак;1;ЦСКА;1
ЦСКА;0;Зенит;2
Sample Output:
Зенит:2 2 0 0 6
ЦСКА:2 0 1 1 1
Спартак:2 0 1 1 1
'''
teams = {} #Создает пустой словарь
n = int(input()) #cчитываем кол-во матчей
line_match = [input().split(';') for i in range(n)] #создаем список из списков матчей вида [['Zenit', '4', 'Spartak', '1'], ['Loko', '3', 'CSKA', '2']]
#print(line_match)

for i in range(n): #Перебираем все матчи
    if line_match[i][0] not in teams: #eсли ключа(названия команды 1) нет в списке, то создать такой ключ с пустым значением
        teams[line_match[i][0]] = []
    if line_match[i][2] not in teams:  #eсли ключа(названия команды 2) нет в списке, то создать такой ключ с пустым значением
        teams[line_match[i][2]] = []
    if line_match[i][1] > line_match[i][3]:
        teams[line_match[i][0]] += [1,1,0,0,3]
        teams[line_match[i][2]] += [1,0,0,1,0]
    elif line_match[i][1] < line_match[i][3]:
        teams[line_match[i][0]] += [1,0,0,1,0]
        teams[line_match[i][2]] += [1,1,0,0,3]
    else:
        teams[line_match[i][0]] += [1,0,1,0,1]
        teams[line_match[i][2]] += [1,0,1,0,1]
#print(teams)

for key in teams: #перебираем все ключи(команды)
    lst = teams[key] #lst присваем значение по ключу, то есть список
    lst_2 = [sum([lst[i + j] for j in range(0, len(lst), 5)]) for i in range(5)]
    print(key + ':' + str(lst_2[0]), lst_2[1], lst_2[2], lst_2[3], lst_2[4])