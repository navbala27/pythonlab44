from tarfile import LENGTH_LINK


a = int (input ("Enter a Number "))
b = int ((a/2))

for i in range (2,b):
    if a % i == 0:
        print ("Not Prime")
    else:
        print ("Prime")