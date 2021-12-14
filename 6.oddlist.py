a = input  ("Enter the Numbers ")
z = map ( int , a.split (' ') )
b = list (z)
##b = a.split (',')
##b = a.split ('\n')

print (b)
c = len (b)
print ("No. of Elements are ", c)

for i in b:
 ##print (i)
 if ( i%2 == 0):
  continue
 print (i)
