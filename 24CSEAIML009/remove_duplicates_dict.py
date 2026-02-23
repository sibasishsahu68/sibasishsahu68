# Program to create a dictionary from user input and remove duplicate values (keeping the first occurrence)

# Get the number of entries from user
n = int(input("Enter the number of dictionary entries: "))

# Initialize an empty dictionary
my_dict = {}

# Loop to get key-value pairs
for i in range(n):
    key = input(f"Enter key {i+1}: ")
    value = input(f"Enter value for {key}: ")  # Keep as string for generality, or convert if needed
    my_dict[key] = value

# Remove duplicates based on values: keep only unique values, preserving the first key for each value
seen_values = set()
unique_dict = {}
for key, value in my_dict.items():
    if value not in seen_values:
        unique_dict[key] = value
        seen_values.add(value)

# Print the resulting dictionary
print("Dictionary after removing duplicates:")
print(unique_dict)
