with open('file.txt', 'r') as file:
    s = file.read().strip().lower()

listofs = s.split()
print(listofs)

count = 1
word = listofs[0]
for i in range(1,len(listofs)):
    if


