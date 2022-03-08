def pyramid():
    n = int (input ("Enter Number of Rows"))
    for i in range (1,n+1):
        print("\n")
        for j in range (1,i+1):
            print (i*j,end=" ")

pyramid()