#Python program to display all integers within the range 100 -200 whose sum of digits is an even number.

for number in range(100, 201):
    
    number_str = str(number)
    
    digit_sum = sum(int(digit) for digit in number_str)
    if digit_sum % 2 == 0:
        print(number)
