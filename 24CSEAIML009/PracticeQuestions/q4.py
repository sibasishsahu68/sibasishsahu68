#wap to check weather a number  is perfect or not
def is_perfect(num):
    if num < 2:
        return False
    divisors_sum = 0
    for i in range(1, num):
        if num % i == 0:
            divisors_sum += i
    return divisors_sum == num

def main():
    n = int(input("Enter a number: "))
    if is_perfect(n):
        print(n, "is a perfect number.")
    else:
        print(n, "is not a perfect number.")

main()