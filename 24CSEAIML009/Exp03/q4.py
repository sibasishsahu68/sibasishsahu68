digit = int(input("Enter a digit (0-6): "))

weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

if 0 <= digit <= 6:
    print("The weekday is:", weekdays[digit])
else:
    print("Invalid input! Please enter a digit between 0 and 6.")