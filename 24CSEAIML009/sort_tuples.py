n = int(input("Enter the number of strings: "))

t = ()

for i in range(n):
    item = input(f"Enter string {i+1}: ")
    t = t + (item,)

single_string = ' '.join(t)  


print("Tuple:", t)
print("Single string:", single_string)
