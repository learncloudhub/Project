# A super simple 1-line calculation tool
expr = input("Enter math expression (e.g., 2+3*5): ")
try:
    print("Result:", eval(expr))
except:
    print("Invalid math expression.")

