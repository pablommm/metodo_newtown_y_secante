import matplotlib.pyplot as plt
import numpy as np

# Crea un conjunto de datos x
x = np.linspace(-10, 2*np.pi, 100)

# Crea un conjunto de datos y correspondiente para la función seno
#y = np.sin(x)
#y = (x * x) - 2
y = x**3 + 4*(x**2) -10
# Crea la gráfica usando Matplotlib
plt.plot(x, y)

# Agrega etiquetas a los ejes y título
plt.xlabel('x')
plt.ylabel('y')
#plt.title('Gráfico de la función')

# Muestra la gráfica
plt.show()