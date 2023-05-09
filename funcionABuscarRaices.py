import math
import metodoNewtown
import metodoSecante

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