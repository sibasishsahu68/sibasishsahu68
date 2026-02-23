m = int(input("Enter starting number (m): "))
n = int(input("Enter ending number (n): "))
print("the prime no.s are :",end ="")
for i in range(m, n+1):
    for j in range(2,i):
        if i%j == 0:
            break
    else:
        print(i,end =", ")