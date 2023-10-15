#Python program to display the sum of n numbers using a list
input = int(input("Enter a number: "))  
if input < 0:  
   print("Enter a positive number")  
else:  
   sum = 0  
   while(input > 0):  
       sum += input  
       input -= 1  
   print("The result is",sum)  