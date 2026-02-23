text = input("Enter a string: ")

reversed_text = text[::-1]

words = reversed_text.split()

print("\nOriginal String:", text)
print("Reversed String:", reversed_text)
print("Words after splitting:", words)