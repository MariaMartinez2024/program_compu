import matplotlib.pyplot as plt


redes = ['WhatsApp', 'Instagram', 'TikTok', 'Threads', 'Facebook']
porcentajes = [20, 30, 50, 0, 0]
colores = ['#3366CC', '#FF5733', '#FFA500', '#00FF00', '#FF00FF']



plt.figure(figsize=(6,6))
plt.pie(porcentajes, labels=redes, autopct='%1.0f%%', colors=colores, startangle=90)
plt.title('¿Qué red social usas más?')
plt.axis('equal')  


plt.show()