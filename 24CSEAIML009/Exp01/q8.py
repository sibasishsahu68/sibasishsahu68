a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

sum = a + b + c
s = sum / 2

area = (s * (s - a) * (s - b) * (s - c))**0.5
print("Area is",area)
print ("Perimeter is ", sum)