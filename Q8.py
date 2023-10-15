#Python program to find the sum of the digits of an integer using a while loop

def sum_of_digits(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum


n = int(input("Enter a number: "))
print("The sum of the digits of", n, "is", sum_of_digits(n))