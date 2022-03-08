a = input ("Enter a String ")

x = a[0]
print(x)

for i in range(1,len(a)):
    if a[i] == x:
        a = a.replace(a[0],'$')
    
        

print (a)