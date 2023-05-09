import math
import funcionABuscarRaices

def secante (f,x1,x2,tolerancia):
    error =1e3
    n = 0
    x3 = 0
    while error > tolerancia:
        x3 = x1 - ((x2-x1)/ (f(x2)-f(x1))) * f(x1)
        error = abs(f(x3))
        n += 1
    print("solucion aproxiamada : {: .4f}".format(x3))
    print("numero de iteracion : {:d}".format(n))