x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))

gcd = 1
i = 1

while i <= min(x, y, z):
    if x % i == 0 and y % i == 0 and z % i == 0:
        gcd = i
    i += 1

print("GCD of", x, ",", y, "and", z, "is", gcd)