import time, os

os.system('cls')
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

print("\n-------------------------------------------------------------------------------------------------------\n")
print("STARTING:....................\n")
print("xn :", xn)
print("dif: undefined")
print("n  :", n, "\n")

while (dif > epsilon):
    xn = newton(xn)
    dif = abs(xn - newton(xn))
    n += 1
    print("xn :", xn)
    print("dif:", dif)
    print("n  :", n, "\n")
    time.sleep(1)

print("\n-------------------------------------------------------------------------------------------------------\n\nRESULT: ", xn)
print("\n-------------------------------------------------------------------------------------------------------\n")