a = int ( input ("Enter a Year "))
if a % 400 == 0:
    print (a," is a leap year")

elif a % 4 == 0 and not a % 100 == 0:
    print (a," is not a leap year")
else:
    print (a," is not a leap year")