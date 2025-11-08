x = float(input("Enter x: "))
fx_str = input("Enter function in terms of x (e.g., 2*x**2+1): ")

# Here limiting eval command to x so it only sees x nothing else.
# Eval is used to make function(fx) user input as you cant write operational symbols with input command.
fx = eval(fx_str, {"x": x})

# Smaller the h is the more precise the answer will be.
h = 0.01
for i in range(1, 10):
    derivative = (eval(fx_str, {"x": x + h}) - fx) / h
    h = h / 10

print("Approximate derivative at x =", x, "is", derivative)