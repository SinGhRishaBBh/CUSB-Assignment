# Python program to implement binary search
def binary_search(arr, target):
    
    left, right = 0, len(arr) - 1  
    while left <= right:
        mid = left + (right - left) // 2  

        if arr[mid] == target:
            return mid  
        elif arr[mid] < target:
            left = mid + 1  
        else:
            right = mid - 1  

    return -1 


my_list = [1, 2, 4, 5, 7, 8, 9]
target_value = 9
result = binary_search(my_list, target_value)

if result != -1:
    print("Found",target_value, "at index", result)
else:
    print(f"{target_value} not found in the list.")
