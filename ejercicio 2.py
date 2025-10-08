import matplotlib.pyplot as plt


respuestas = ["1 taza", "2 tazas", "3 tazas", "No tomo café", "Una"]
cantidades = [2, 2, 4, 1, 1]

plt.figure(figsize=(8, 5))
plt.bar(respuestas, cantidades, color='purple')


plt.title("¿Cuántas tazas de café tomas al día?")
plt.xlabel("Respuestas")
plt.ylabel("Cantidad de personas")
plt.ylim(0, max(cantidades) + 1)


for i, valor in enumerate(cantidades):
    plt.text(i, valor + 0.1, str(valor), ha='center')
    
plt.tight_layout()
plt.show()