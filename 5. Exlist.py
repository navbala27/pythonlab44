l1 = input ("Enter List1 Entries \n")
l2 = input ("Enter List2 Entries \n")
S = 0
a = list (map (int  ,  l1.split (' ')))
b = list(map (int  ,  l2.split (' ')))

if len (a) == len (b):
    print ("The Lists are  of Same Length \n")

if sum (a) == sum (b):
    print ("The Sums of the Lists are  of Same  \n")
else:
     print ("The Sums of the Lists are not Same  \n")

for i in  range (0 , len (a)):
     for j in range (0 , len (b)):
         if a[i] == b[j]:
             print ( a[i] )
             v = True
         else:
            v = False

if v:
    print  (" is found in both lists")
        
print ("No Elements are Found Same")
