f1 = open("word.txt", "r")
f2 = open("store.txt", "w")

cont = f1.readlines()

type(cont)

for i in range (0,len(cont)):
    if (i+1)%2 != 0:
        f2.write(cont[i])
        
f2.close()
f2 = open("store.txt")

a = f2.read()

print (a)