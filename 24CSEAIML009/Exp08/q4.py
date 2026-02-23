def factorial(num):
    result = 1
    for i in range(1, num+1):
        result *= i
    return result

n = int(input("Enter a number: "))
print("Factorial of", n, "is:", factorial(n))