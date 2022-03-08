def fact(n):
    fact = 1
    if n == 1 or n == 0:
        return 1
    else:
        for i in range (2,n+1):
            fact = fact * i
    return fact



a = int (input ("Enter a Positive Number "))
result = fact(a)
print ("The Factorial of ",a," is ",result)
    