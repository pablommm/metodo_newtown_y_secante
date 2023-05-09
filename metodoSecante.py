import math
import time
#import funcionABuscarRaices as fbr

# funcion original
funcion = lambda x: x**3 + 4*(x**2) -10

# funcion deribada
dfx = lambda x: 3*(x**2)

#punto de partida
x0 = 2

x1 = 3

x2 = 5
#criterio de parada con margen de error
tolerancia = 0.0001

def secante (f,x1,x2,tolerancia):
    error =10000
    n = 0
    x3 = 0
    
    while error > tolerancia:
        x3 = x2 - (f(x2)*(x2-x1)/ (f(x2)-f(x1)))
        x1 = x2
        x2 = x3
        error = abs(f(x3))
        n += 1
        print("error:",error)
        print("valor x3:",x3)
        print("Valor n:",n)
        
        time.sleep(2)
    print("solucion aproxiamada : {: .4f}".format(x3))
    print("numero de iteracion : {:d}".format(n))
    
          
secante(funcion,x1,x2,tolerancia)
  