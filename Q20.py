# Find the largest number in a list without using built in function

def find_largest_number(arr):
    
    
    if len(arr) == 0:
        return None  

    largest = arr[0] 

    for number in arr:
        if number > largest:
            largest = number

    return largest


my_list = [5, 3, 9, 1, 8, 2, 7]
largest_number = find_largest_number(my_list)

if largest_number is not None:
    print("The largest number in the list is:", largest_number)
else:
    print("The list is empty.")
