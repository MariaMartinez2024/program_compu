PRECIO_KWH = 0.20  # Precio por kWh en dólares

def calcular_costo(consumo_kwh):
    """Devuelve el costo en dólares según el consumo en kWh."""
    return consumo_kwh * PRECIO_KWH

def resumen(aparatos):
    """Calcula consumo total y costo total de todos los aparatos."""
    total_consumo = sum(a.consumo_mensual() for a in aparatos)
    total_costo = sum(calcular_costo(a.consumo_mensual()) for a in aparatos)
    return total_consumo, total_costo