m = int(input("Enter starting number (m): "))
n = int(input("Enter ending number (n): "))
l = [x for x in range(m,n+1)]

print("Sum:", sum(l))
print("Average:", sum(l)/len(l))
print("Largest:", max(l))
print("Smallest:", min(l))

l2 = [x for x in l if x%3!=0]
print("List excluding numbers divisible by 3:", l2)