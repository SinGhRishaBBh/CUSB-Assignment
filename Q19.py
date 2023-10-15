#Python program to find the odd numbers in an array
def find_odd_numbers(arr):
    
    odd_numbers = []
    for number in arr:
        if number % 2 != 0:
            odd_numbers.append(number)
    return odd_numbers

my_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
odd_numbers = find_odd_numbers(my_array)

print("Odd numbers in the array:", odd_numbers)