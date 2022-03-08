str1 = input("Enter a String ")
str2 = input("Enter anothe String ")

new1 = str1.replace(str1[0],str2[0])
new2 = str2.replace(str2[0],str1[0])

print (new1 + " " + new2)           