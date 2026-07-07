import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

"""
Visualização de Dados com Matplotlib

Tópicos Abordados:
- API Global: Interface estilo MATLAB (plt.plot, plt.figure, etc)
- API OOP: Trabalhar com Figure e Axes (fig, axes)
- Subplots: Criar múltiplos gráficos em uma figura
- Scatter Plot: Gráficos de dispersão com cores e tamanhos variados
- Histogramas: Distribuição de frequências
- KDE (Kernel Density Estimation): Estimativa de densidade de probabilidade

Aprenderemos a:
✓ Criar diferentes tipos de gráficos
✓ Personalizar cores, linhas, marcadores
✓ Organizar múltiplos subplots
✓ Adicionar legendas, títulos e rótulos
✓ Usar mapas de cores (colormaps)
"""

# ===== EXEMPLO 1: API Global =====
x = np.arange(-10, 11)

plt.figure(figsize=(12, 16))
plt.title("My nice plot")
plt.plot(x, x**2)
plt.plot(x, -1 * (x**2))
plt.show()

# ===== EXEMPLO 2: Subplots Global =====
plt.figure(figsize=(12, 6))
plt.title("My Nice Plot")

plt.subplot(1, 2, 1)
plt.plot(x, x**2)
plt.plot([0, 0, 0], [-10, 0, 100])
plt.legend(["X^2", "Vertical Line"])
plt.xlabel("X")
plt.ylabel("X Squared")

plt.subplot(1, 2, 2)
plt.plot(x, -1 * (x**2))
plt.plot([-10, 0, 10], [-50, -50, -50])
plt.legend(["-X^2", "Horizontal Line"])
plt.xlabel("X")
plt.ylabel("X Squared")
plt.show()

# ===== EXEMPLO 3: API OOP (Recomendado) =====
fig, axes = plt.subplots(figsize=(12, 6))
axes.plot(x, x**2, color="red", linewidth=3, marker="o", markersize=8, label="X^2")
axes.plot(x, -1 * (x**2), "b--", label="-X^2")
axes.set_xlabel("X")
axes.set_ylabel("X Squared")
axes.set_title("My Nice Plot")
axes.legend()
plt.show()

# ===== EXEMPLO 4: Múltiplos Subplots =====
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2, figsize=(14, 6))
ax1.plot(np.random.randn(50), c="red", linestyle="--")
ax2.plot(np.random.randn(50), c="green", linestyle=":")
ax3.plot(np.random.randn(50), c="blue", marker="o", linewidth=3)
ax4.plot(np.random.randn(50), c="yellow")
plt.show()

# ===== EXEMPLO 5: Scatter Plot =====
N = 50
x_scatter = np.random.rand(N)
y_scatter = np.random.rand(N)
colors = np.random.rand(N)
area = np.pi * (20 * np.random.rand(N)) ** 2

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
ax1.scatter(x_scatter, y_scatter, s=area, c=colors, alpha=0.5, cmap="Pastel1")
ax1.colorbar = plt.colorbar(ax1.collections[0], ax=ax1)
ax2.scatter(x_scatter, y_scatter, s=area, c=colors, alpha=0.5, cmap="Pastel2")
plt.colorbar(ax2.collections[0], ax=ax2)
plt.show()

# ===== EXEMPLO 6: Histogramas e KDE =====
values = np.random.randn(1000)

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Histograma
axes[0].hist(values, bins=100, alpha=0.8, color="steelblue", edgecolor="green")
axes[0].set_xlim(-5, 5)
axes[0].set_title("Histogram")

# KDE
density = stats.gaussian_kde(values)
values2 = np.linspace(min(values) - 10, max(values) + 10, 100)
axes[1].plot(values2, density(values2), color="#FF7F00", linewidth=3)
axes[1].fill_between(values2, 0, density(values2), alpha=0.5, color="#FF7F00")
axes[1].set_xlim(-5, 5)
axes[1].set_title("KDE")

plt.show()

# ===== EXEMPLO 7: Bar plots =====

Y = np.random.rand(1, 5)[0]
Y2 = np.random.rand(1, 5)[0]
plt.figure(figsize=(12, 4))

barWidth = 0.5
plt.bar(np.arange(len(Y)), Y, width=barWidth, color='#00b894')

" Também é possível usar barras empilhadas e adicionar uma legenda ao gráfico: "

plt.figure(figsize=(12, 4))
barWidth = 0.5
plt.bar(np.arange(len(Y)), Y, width=barWidth, color='#00b894', label='Label Y')
plt.bar(np.arange(len(Y2)), Y2, width=barWidth, color='#e17055', bottom=Y, label='Label Y2')

plt.legend()
plt.show()