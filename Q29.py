#Python program to print all the items in a dictionary

my_dict = {
    "name": "Raj",
    "age": 22,
    "city": "Delhi"
}

for key, value in my_dict.items():
    print(key, ":", value)
