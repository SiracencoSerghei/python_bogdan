my_dict = {}

while len(my_dict) < 3:
    key_of_dict = input("Enter the name of key for your dict: ")
    value_of_key = input("Enter the value for entering key: ")
    my_dict[key_of_dict] = value_of_key

print(f"Dictionary is {my_dict}")
