with open("dataset_3380_5.txt", "r") as f:
    a = {str(i): [] for i in range(1, 12)}
    [a[i[0]].append(int(i[2])) for i in map(lambda x: x.split('\t'), f.read().split('\n'))]
    [print(i,sum(a[i])/len(a[i]) if len(a[i]) > 0 else '-' ) for i in map(str, range(1, 12))]