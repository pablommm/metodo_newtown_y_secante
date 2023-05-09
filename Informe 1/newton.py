xn = 4
n = 0
dif  = 1000000
epsilon = 0.001

def f(x):
    return (x * x) - 2

def f1(x):
    return x * 2

def newton(x):
    return x - (f(x)/f1(x))

while (dif > epsilon):
    xn = newton(xn)
    dif = abs(xn - newton(xn))
    n += 1
    print("xn :", xn)
    print("dif:", dif)
    print("n  :", n, "\n")

print("---------------------------------\nresult:")
print(xn)