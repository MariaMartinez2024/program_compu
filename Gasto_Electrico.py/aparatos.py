class Aparato:
    def __init__(self, nombre, potencia, horas):
        # nombre: nombre del aparato
        # potencia: potencia en watts
        # horas: horas de uso diario
        self.nombre = nombre
        self.potencia = potencia
        self.horas = horas

    def consumo_mensual(self):
        """
        Calcula el consumo mensual en kWh.
        Fórmula: (potencia en watts * horas * 30 días) / 1000
        """
        return (self.potencia * self.horas * 30) / 1000