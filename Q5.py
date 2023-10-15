# Python program to check whether the given integer is a multiple of both 5 and 7

num = int(input("Enter any number "))
if((num%5==0)and(num%7==0)):
    print(num, "is a multiple of both 5 and 7")
else:
    print(num, "is not a multiple of both 5 and 7")