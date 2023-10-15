#Python program to insert a number to any position in a list

my_list = [1, 2, 3, 4, 5]
number_to_insert = int(input("Enter number to insert"))
position = 2  

my_list.insert(position, number_to_insert)

# Print the updated list
print("Updated List:", my_list)
