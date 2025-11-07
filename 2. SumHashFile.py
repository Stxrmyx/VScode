PATH1, PATH2 = input("Укажите путь к файлу 1: ") , input("Укажите путь к файлу 2: ")

P1 = open(PATH1 , 'r')
for i in P1:
    i
print( hash(i))

P2 = open(PATH2 , 'r')
for j in P2:
    j
print( hash(j))

if i == j:
    print("Hash-сумма одинаковая")
else:
    print("Hash-сумма разная")


#/home/stxrmyq/Downloads/2.txt
#/home/stxrmyq/Downloads/1.txt