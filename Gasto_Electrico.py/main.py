from utils import pedir_datos_aparatos, mostrar_resultados
from calculos import calcular_costo, resumen

class SistemaElectrico:
    def __init__(self):
        self.aparatos = []
 
    def ejecutar(self):
        print("=== Sistema de Control de Gasto Eléctrico ===")
        print("Registra tus aparatos y conoce tu consumo mensual.\n")
        self.aparatos = pedir_datos_aparatos()
        mostrar_resultados(self.aparatos, calcular_costo)
        total_consumo, total_costo = resumen(self.aparatos)
        print("\n=== Resumen General ===")
        print(f"Consumo Total (kWh): {total_consumo:.2f}")
        print(f"Gasto Mensual ($): {total_costo:.2f}")

if __name__ == "__main__":
    sistema = SistemaElectrico()
    sistema.ejecutar()