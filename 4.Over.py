a = input ("Enter Some Integers ")
b = map (int, a.split (' '))
for i in b:
    if (i>100):
        print ('over')
    else:
         print (i)
