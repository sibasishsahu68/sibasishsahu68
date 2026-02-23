n = int(input("Enter the number of items: "))
dict1 = {}
for i in range(n):
    key = input(f"Enter key {i+1}: ")
    value = input(f"Enter value for {key}: ")
    dict1[key] = value

dict2 = {}
for key, value in dict1.items():
    dict2[value] = key

print("First Dictionary:", dict1)
print("Second Dictionary:", dict2)
                                             