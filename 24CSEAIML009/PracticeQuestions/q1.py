#write a python program to enter 5 digits and print the digits present at odd places
num = input("Enter a 5-digit number: ")

if len(num) == 5 and num.isdigit():
    print("Digits at odd places are:")
    print(num[0], num[2], num[4])
else:
    print("Please enter exactly 5 digits.")