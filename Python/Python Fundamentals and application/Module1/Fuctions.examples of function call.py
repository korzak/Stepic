def printab(a,b):
    print(a)
    print(b)
    print("---------------------------")

printab(10,20)
printab(b = 101, a = 12)
printab(9,b=15) #Keywords arguments always after non-keyword arguments

lst = [16, 34]
printab(*lst)

args = {'a': 11, 'b': 71}
printab(**args)