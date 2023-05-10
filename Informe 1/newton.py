import time
import math
import numpy as np
import matplotlib.pyplot as plt

xn = 4
x1 = 4
x2 = 2.525
x3 = 0

n_newton = 0
n_sec = 0
dif_n = 1000000
dif_s = 1000000

EPSILON = 0.001
print("-------------------------------------------------------------------------------------------")
print("-------------------------------------------------------------------------------------------\n")
print("Vamos a encontrar una raiz de la funcion (x**3) + (4*(x**2)) -10 usando los metodos de Newton y de la Secante")

#aca vamos a guardar los resultados 
resultados_newton = []
resultados_secante = []

difs_newton = []
difs_secante = []

def f(x):
    # return (x * x) - 2
    return (x**3) + (4*(x**2)) -10

def f1(x):
    # return x * 2
    return (3*(x**2)) + (8*x)

def newton(x):
    res = x - (f(x)/f1(x))
    resultados_newton.append(res)
    return res

def sec(f,x1,x2):
    res = x2 - (f(x2)*(x2-x1)/ (f(x2)-f(x1)))
    resultados_secante.append(res) 
    return res

# While Newton
while(dif_n > EPSILON) or (dif_s > EPSILON):

    if (dif_n > EPSILON):
        print("\nPaso de Newton:\n")
        xn = newton(xn)
        dif_n = abs(xn - newton(xn))
        difs_newton.append(dif_n)
        n_newton += 1
        print("xn :", xn)
        print("Error:", dif_n)
        print("n  :", n_newton, "\n")
        time.sleep(1)
        
    
    if (dif_s > EPSILON):
        print("\nPaso de Secante:\n")
        x3 = sec(f, x1, x2)
        x1 = x2
        x2 = x3
        dif_s = abs(f(x3))
        difs_secante.append(dif_s)
        n_sec += 1
        print("Error:",dif_s)
        print("valor x3:",x3)
        print("Valor n:",n_sec)
        print("\n")
        time.sleep(1)

print("---------------------------------\nRESULTADOS:")
print("\nRaiz encontrada por Newton: ", xn)
print("Numero de pasos de Newton: ", n_newton)
print("Resultados de Newton: ", resultados_newton)
print("Errores de Newton: ", difs_newton)

print("\nRaiz encontrada por Secante: ", x3)
print("Numero de pasos de Secante: ", n_sec)
print("Resultados de Secante: ", resultados_secante)
print("Errores de Secante: ", difs_secante)
time.sleep(1)




range_newton = []
range_sec = []

for i in range(n_newton):
    range_newton.append(i + 1)

for j in range(n_sec):
    range_sec.append(j + 1)



time.sleep(1)
print("\n---------------------------------------------")
print("CONCLUSIONES:")
print("\n---------------------------------------------")
time.sleep(1)
print("")
print("Probamos la precision de la raiz encontrada por Newton: ", xn)
print("haciendo f(xn) y esperando un resultado cercano a 0")
print("f(xn) = ", f(xn))
time.sleep(1)

print("Probamos la precision de la raiz encontrada por Secante: ", xn)
print("haciendo f(x3) y esperando un resultado cercano a 0")
print("f(x3) = ", f(x3))
time.sleep(1)



print("\n---------------------------------------------")
print("GRAFICOS:")
print("---------------------------------------------")
plt.plot(range_newton, difs_newton)
plt.plot(range_sec, difs_secante)

plt.legend(['Error Newton', 'Error Secante'])
plt.xlabel('Numero de pasos')
plt.ylabel('Error del metodo')
plt.title('Gráfico del error de Newton y Secante')
plt.show()


x= np.linspace(0, 2*np.pi, 10)
y = (x**3) + (4*(x**2)) -10
plt.plot([0,1,2,3,4,5,6,7,8,9,10], [0,0,0,0,0,0,0,0,0,0,0])
plt.plot(x , y)
plt.plot(xn, f(xn), 'ro')
plt.legend(['eje x', 'funcion', 'raiz'])
plt.xlabel('valores en x')
plt.ylabel('valores en y')
plt.title('Gráfico de la funcion')
plt.text(xn - 0.5, f(xn) + 1,  str(round(xn, 3)))
plt.show()