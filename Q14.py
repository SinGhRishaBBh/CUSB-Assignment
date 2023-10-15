#Python program to print the numbers from a given number n till 0 using recursion
def print_numbers(n):
    if n < 0:
        return
    print(n)
    print_numbers(n - 1)

# Input the number 'n'
n = int(input("Enter a number: "))

print("Numbers from", n, "to 0:")
print_numbers(n)
