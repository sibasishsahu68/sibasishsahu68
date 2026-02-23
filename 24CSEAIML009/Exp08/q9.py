def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

p = float(input("Enter Principal amount: "))
r = float(input("Enter Rate of Interest: "))
t = float(input("Enter Time (in years): "))

print("Simple Interest is:", simple_interest(p, r, t))