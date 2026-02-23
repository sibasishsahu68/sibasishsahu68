int_val = int(input("Enter an integer: "))
str_val = input("Enter a string: ")
float_val = float(input("Enter a float: "))
bool_input = input("Enter a boolean (True/False): ")
complex_val = complex(input("Enter a complex number (e.g., 2+3j): "))

if bool_input.lower() == "true":
    bool_val = True
elif bool_input.lower() == "false":
    bool_val = False
else:
    bool_val = None   
print("\nDisplaying Values and Data Types ")
print("Integer:", int_val, "Type:", type(int_val))
print("String:", str_val, "Type:", type(str_val))
print("Float:", float_val, "Type:", type(float_val))
print("Boolean:", bool_val, "Type:", type(bool_val))
print("Complex:", complex_val, "Type:", type(complex_val))
