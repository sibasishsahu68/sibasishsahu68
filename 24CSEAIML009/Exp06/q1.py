fruits = ["apple", "banana", "mango", "orange"]

print("Fruits in reverse order with lengths:")
for fruit in reversed(fruits):
    print(fruit, "-> length:", len(fruit))

reversed_fruits = [fruit[::-1] for fruit in fruits]

print("\nList with reversed elements:", reversed_fruits)

