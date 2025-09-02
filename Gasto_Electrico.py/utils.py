from aparatos import Aparato

def pedir_datos_aparatos():
    """Pide al usuario los datos de los aparatos eléctricos."""
    aparatos = []
    while True:
        nombre = input("Nombre del aparato (o 'fin' para terminar): ")
        if nombre.lower() == 'fin':
            break
        potencia = float(input(f"Potencia de {nombre} (Watts): "))
        horas = float(input(f"Horas de uso diario de {nombre}: "))
        aparatos.append(Aparato(nombre, potencia, horas))
    return aparatos

def mostrar_resultados(aparatos, calcular_costo):
    """Muestra el consumo y costo de cada aparato."""
    print("\n Resumen de Aparatos ")
    print(f"{'Aparato':<20}{'Consumo (kWh)':<20}{'Costo ($)':<15}")
    print("-" * 55)
    for a in aparatos:
        consumo = a.consumo_mensual()
        costo = calcular_costo(consumo)
        print(f"{a.nombre:<20}{consumo:<20.2f}{costo:<15.2f}")