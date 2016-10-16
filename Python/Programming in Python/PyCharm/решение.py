n = int(input())
sar = [input().split(';') for i in range(n)]
teams ={}
for i in range(n):
    if sar[i][0] not in teams:
        teams[sar[i][0]]=[]
    if sar[i][2] not in teams:
        teams[sar[i][2]]=[]

    if sar[i][1]>sar[i][3]:
        teams[sar[i][0]]+=[1,1,0,0,3]
        teams[sar[i][2]]+=[1,0,0,1,0]
    elif sar[i][1]==sar[i][3]:
        teams[sar[i][0]]+=[1,0,1,0,1]
        teams[sar[i][2]]+=[1,0,1,0,1]
    else:
        teams[sar[i][2]]+=[1,1,0,0,3]
        teams[sar[i][0]]+=[1,0,0,1,0]
for key in teams:
    lst = teams[key]
    lst_2 = [sum([lst[i+j] for j in range(0,len(lst),5)]) for i in range(5)]
    print(key+':'+str(lst_2[0]),lst_2[1],lst_2[2],lst_2[3],lst_2[4])