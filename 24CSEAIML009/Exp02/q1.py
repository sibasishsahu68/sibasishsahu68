principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest in %: "))
time = float(input("Enter the time in years: "))

simple_interest = (principal * rate * time) 
compound_interest = principal * ((1 + rate / 100) ** time) - principal

print(f"Simple Interest = {simple_interest:.2f}")
print(f"Compound Interest = {compound_interest:.2f}")