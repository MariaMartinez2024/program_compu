a. Describe brevemente de qué trata el dataset utilizado
El dataset Iris contiene 150 registros de flores de tres especies distintas (Iris-setosa, Iris-versicolor e Iris-virginica). Cada fila representa una flor y las columnas muestran mediciones de sépalos y pétalos (longitud y ancho en centímetros), además de un identificador.

b. b. ¿Qué información permite ver el resumen estadístico?
El método describe() muestra estadísticas generales como:

count → número de registros válidos por columna.

mean → promedio de las medidas.

std → desviación estándar, es decir, qué tanto varían los datos respecto al promedio.

min / max → valores mínimo y máximo registrados.

25%, 50%, 75% → los cuartiles, que dividen los datos en segmentos para ver su distribución.

Esto permite identificar el rango de valores y la dispersión de las medidas.

c) ¿Qué cambios o tendencias se detectan en la información del dataset?
Se observa que la especie Setosa tiene pétalos mucho más pequeños que Versicolor y Virginica. Además, las longitudes de sépalos y pétalos aumentan progresivamente al pasar de Setosa → Versicolor → Virginica.

d) ¿Qué categorías sobresalen en la comparación y por qué crees que será?
Sobresale Iris-setosa, porque sus medidas son claramente más bajas (sépalos y pétalos cortos). Esto facilita diferenciarla de las otras especies sin necesidad de un análisis profundo. Virginica también resalta porque tiene los valores más altos en casi todas las mediciones.

e) ¿Qué diferencias se observan entre los primeros y últimos registros?

Los primeros registros (head()) corresponden a la especie Setosa.

Los últimos registros (tail()) corresponden a la especie Virginica.
Esto indica que el dataset está ordenado por especie, lo cual ayuda a ver la evolución de las medidas entre las diferentes clases.

f) ¿Qué aportan las medidas estadísticas al análisis del dataset?

Media (5.84 cm en SepalLengthCm aprox.) → representa el tamaño promedio de los sépalos.

Mediana (5.8 cm) → muestra el valor central, eliminando el efecto de posibles valores extremos.

Desviación estándar (~0.82) → indica que los sépalos no son todos iguales, sino que varían en torno a ±0.8 cm respecto al promedio.

Estas medidas son útiles para comparar especies, identificar patrones y comprender la variabilidad de los datos.
