import numpy as np
import matplotlib.pyplot as plt

# Datos del ejercicio
x = np.array([50, 70, 90, 110, 130])  # Presión (kPa)
y = np.array([15, 21, 27, 33, 39])    # Caudal (L/min)

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

# Estimar el caudal para 100 kPa
x_new = 100
y_estimated = a + b * x_new
print(f"\nCaudal estimado para {x_new} kPa: {y_estimated:.2f} L/min")

# Calcular R^2 (opcional)
y_pred = a + b * x
ss_res = np.sum((y - y_pred) ** 2)
ss_tot = np.sum((y - np.mean(y)) ** 2)
r_squared = 1 - (ss_res / ss_tot)
print(f"\nCoeficiente de determinación R^2 = {r_squared:.4f}")

# Gráfica
plt.figure(figsize=(8,6))
plt.plot(x, y, 'o', label='Datos experimentales')
plt.plot(x, y_pred, '-', label=f'Ajuste lineal: y = {a:.2f} + {b:.2f}x', color='red')
plt.xlabel('Presión (kPa)')
plt.ylabel('Caudal (L/min)')
plt.title('Regresión Lineal - Caudal en Tuberías')
plt.legend()
plt.grid(True)
plt.savefig('regresion_lineal_caudal.png', dpi=300)  # Guarda la figura
plt.show()
