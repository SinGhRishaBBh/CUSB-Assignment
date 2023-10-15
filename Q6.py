# Python program to display the given integer in a reverse manner

num = int(input("Enter a number "))
reversed_num = 0
while num !=0: 
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10
print("The reversed number is ", reversed_num)