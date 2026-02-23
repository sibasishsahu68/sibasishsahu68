#write a program to enter a string and print it in reverse and also print the no. of vowels and consonants in it
s = input("Enter a string: ")
rev = s[::-1]
vowels = "aeiouAEIOU"
v = c = 0
for ch in s:
    if ch.isalpha():
        if ch in vowels:
            v += 1
        else:
            c += 1
print("Reversed string:", rev)
print("Number of vowels:", v)
print("Number of consonants:", c)