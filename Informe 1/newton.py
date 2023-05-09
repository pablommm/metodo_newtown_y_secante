

xn = 4
xa = 2
xb = 32
n = 0
dif  = 1000000
epsilon = 0.001

#aca vamos a guardar los resultados 
resultados = [ ]

def f(x):
    return (x * x) - 2

def f1(x):
    return x * 2

def newton(x):
    return x - (f(x)/f1(x))

def sec(x):
    resultados.append(f(x))
    resultado = xb - ((f(xb)*( xb - xa )) / ((f(xb)) - f(xa)))
    xa = xb 
    xb = resultado


while (dif > epsilon):
    xn = newton(xn)
    dif = abs(xn - newton(xn))
    n += 1
    print("xn :", xn)
    print("dif:", dif)
    print("n  :", n, "\n")

print("---------------------------------\nresult:")
print(xn)