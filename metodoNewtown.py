import math
import funcionABuscarRaices


# formula de newton- raphson
def newton_method(f, dfx, x0, tolerancia):
    xi = x0
    tramo = abs(2*tolerancia)
    while not (tramo<=tolerancia):
        xnuevo = xi - f(xi)/dfx(xi)
        tramo = abs (xnuevo - xi)
        xi = xnuevo
        
        print ('valor xnuevo : ')
        print (xnuevo)
        print ('valor tramo : ')
        print (tramo)
    return xi
