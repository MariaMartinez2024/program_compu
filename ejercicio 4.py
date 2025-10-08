import matplotlib.pyplot as plt


tiempos = [100, 120, 15, 90, 220, 150, 30, 35, 150, 90]

plt.hist(tiempos, bins=8, color="orange", edgecolor="black")


plt.title("Histograma de tiempo para llegar a la U")
plt.xlabel("Minutos")
plt.ylabel("Frecuencia")


plt.show()