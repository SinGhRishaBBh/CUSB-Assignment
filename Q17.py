# Python program to implement linear search
def linear_search(arr, target):
    
    for i in range(len(arr)):
        if arr[i] == target:
            return i  
    return -1  

my_list = [4, 2, 9, 7, 1, 5, 8]
target_value = 17
result = linear_search(my_list, target_value)

if result != -1:
    print(f"Found {target_value} at index {result}")
else:
    print(f"{target_value} not found in the list.")
