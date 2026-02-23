#write a python program to enter a number and check wheather the no. ois palindrome or not
num = input("Enter a number: ")

rev_num = num[::-1]
if num == rev_num:
    print("The number is a palindrome number.")
else:
    print("The number is not a palindrome number.")