import matplotlib.pyplot as plt

horas = [3, 4, 5, 6, 7, 8, 9]
respuestas = [1, 1, 2, 1, 2, 2, 1]


plt.plot(horas, respuestas, marker='o', color='purple', linewidth=2)


plt.title('Horas de sueño de los encuestados')
plt.xlabel('Horas dormidas')
plt.ylabel('Número de respuestas')


for i, valor in enumerate(respuestas):
    plt.text(horas[i], respuestas[i] + 0.05, str(valor), ha='center', fontsize=9)

plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()