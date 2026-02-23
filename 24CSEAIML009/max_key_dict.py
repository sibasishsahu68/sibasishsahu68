
n = int(input("Enter the number of dictionary entries: "))

my_dict = {}
for i in range(n):
    key = input(f"Enter key {i+1}: ")
    value = int(input(f"Enter value for {key}: "))
    my_dict[key] = value

if my_dict:
    max_key = max(my_dict, key=my_dict.get)
    print(f"The key with the maximum value is: {max_key}")
else:
    print("The dictionary is empty.")
