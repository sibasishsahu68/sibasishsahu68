para = input("Enter a paragraph: ")
words = para.split()

count = 0
for w in words:
    count += 1

print("Total words:", count)

palindrome_count = 0
for w in words:
    rev = ""
    for ch in w:
        rev = ch + rev
    if w.lower() == rev.lower():
        palindrome_count += 1

print("Number of palindromes:", palindrome_count)

print("Words in reverse order:")
for w in words:
    rev = ""
    for ch in w:
        rev = ch + rev
    print(rev) 