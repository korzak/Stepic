average, math, physics, russian, count = 0, 0, 0, 0, 0
with open('dataset_3363_4.txt','r') as file:
    for line in file:
        count+=1
        lst = line.strip().split(';')
        math += int(lst[1])
        physics += int(lst[2])
        russian += int(lst[3])
        for i in range(1,len(lst)):
            average += int(lst[i])
        out = open('out.txt', 'a')
        out.write(lst[0]+" средний бал: ")
        out.write(str(round(average/3))+'\n')
        out.close()
        average = 0
#print(str(math/count)+" "+str(physics/count)+" "+str(russian/count))
out = open('out.txt', 'a')
out.write('\n')
out.write("Средний балл Математика: "+str(round(math/count,2))+'\n')
out.write("Средний балл Физика: "+str(round(physics/count,2))+'\n')
out.write("Средний балл Русский: "+str(round(russian/count,2))+'\n')
out.close()