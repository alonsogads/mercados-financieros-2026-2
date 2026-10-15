import numpy as np
import matplotlib.pyplot as plt

# 1. Definir los plazos (maduración en años)
plazos = np.arange(1, 21)

# 2. Simular la Estructura Temporal (Tasas Spot / Curva Cero)
# Usamos una función logarítmica para simular una curva normal ascendente.
# Estas son las tasas PURAS teóricas para cada año exacto.
tasas_spot = 0.04 + 0.02 * np.log(1 + plazos / 5)

# 3. Calcular la Curva de Tasas Comercial (Par Yield Curve)
# Vamos a calcular el Yield to Maturity (YTM) de bonos que pagan cupones.
tasas_yield = []

for T in plazos:
    # Vector de tiempo para descontar los cupones desde el año 1 hasta T
    t_array = np.arange(1, T + 1)
    
    # Calculamos los factores de descuento usando las tasas SPOT exactas
    factores_descuento = 1 / ((1 + tasas_spot[:T])**t_array)
    
    # Suma de todos los factores de descuento
    suma_fd = np.sum(factores_descuento)
    
    # Factor de descuento del último pago (el principal)
    fd_final = factores_descuento[-1]
    
    # Cálculo algebraico del Yield (Cupón) que hace que el bono cotice a la par (Precio = 100)
    # Fórmula: C = (1 - Factor de Descuento Final) / Suma de Factores de Descuento
    ytm = (1 - fd_final) / suma_fd
    tasas_yield.append(ytm)

tasas_yield = np.array(tasas_yield)

# 4. Graficar los resultados
plt.figure(figsize=(10, 6))
plt.plot(plazos, tasas_spot * 100, label='Estructura Temporal (Tasas Spot Puras)', color='red', linewidth=2, marker='o')
plt.plot(plazos, tasas_yield * 100, label='Curva de Tasas Comercial (Yield to Maturity)', color='blue', linewidth=2, linestyle='--')

plt.title('Estructura Temporal vs Curva de Tasas Comercial', fontsize=14)
plt.xlabel('Maduración (Años)', fontsize=12)
plt.ylabel('Tasa de Interés (%)', fontsize=12)
plt.xticks(plazos)
plt.grid(True, linestyle=':', alpha=0.7)
plt.legend(fontsize=12)
plt.tight_layout()
plt.show()