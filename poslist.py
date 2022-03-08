num = input("Enter Numbers ")
c = (num.split())
a = map(int,c)
b = [x for x in a if x>0]
print (b)