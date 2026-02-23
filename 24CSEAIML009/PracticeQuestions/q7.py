#wap to enter a string and check wheather it is palindrome or not in simple python without function
s = input("Enter a string: ")
rev = s[::-1]

if s == rev:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")