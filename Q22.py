#Python program to delete an element from a list by index

my_list = [1, 2, 3, 4, 5]
index_to_delete = int(input("Enter the number you want to delete "))
del my_list[index_to_delete]


print("Updated List:", my_list)

