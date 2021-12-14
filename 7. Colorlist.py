l1 = input ("Enter colorlist1 Entries \n")
l2 = input ("Enter colorlist2 Entries \n")

a = l1.split (' ')
b = l2.split (' ')

for i in a:
    v = False
    for j in b:
        if (i == j):
            v = True
            break
    if not v:
        print  (i)



"""
    1. [x for x in a if x not in b]

    2.
        list_ = []
        for i in a: 
            if  not i in b:
                list_.append(i)

        print(list_)



"""
