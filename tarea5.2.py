import numpy as np
import matplotlib.pyplot as plt

# Datos del ejercicio
x = np.array([0, 2, 4, 6, 8])  # Posición (cm)
y = np.array([100, 92, 85, 78, 71])  # Temperatura (°C)

# Cálculo de los coeficientes
n = len(x)
sum_x = np.sum(x)
sum_y = np.sum(y)
sum_xy = np.sum(x * y)
sum_x2 = np.sum(x**2)

# Fórmulas de regresión lineal
b = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x**2)
a = (sum_y - b * sum_x) / n

print(f"Coeficientes de la regresión:")
print(f"a (intercepto) = {a:.4f}")
print(f"b (pendiente) = {b:.4f}")

# Estimar la temperatura en x = 5 cm
x_new = 5
y_estimated = a + b * x_new
print(f"\nTemperatura estimada en x = {x_new} cm: {y_estimated:.2f} °C")

# Predicción usando el modelo
y_pred = a + b * x

# Gráfica
plt.figure(figsize=(8,6))
plt.plot(x, y, 'o', label='Datos experimentales')
plt.plot(x, y_pred, '-', label=f'Ajuste lineal: y = {a:.2f} + {b:.2f}x', color='red')
plt.xlabel('Posición (cm)')
plt.ylabel('Temperatura (°C)')
plt.title('Regresión Lineal - Transferencia de Calor')
plt.legend()
plt.grid(True)
plt.savefig('regresion_lineal_transferencia_calor.png', dpi=300)  # Guarda la figura
plt.show()
