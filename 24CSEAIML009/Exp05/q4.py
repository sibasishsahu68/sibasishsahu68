numbers = []

nums = int(input("Enter numbers : "))

for n in range(nums):
    numbers.append(int(input()))

numbers = list(set(numbers))
numbers.sort()

print("Final list:", numbers)