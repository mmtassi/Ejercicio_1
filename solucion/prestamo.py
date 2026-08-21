class Prestamo:
    def __init__(self, titulo, nombre_socio, dias_transcurridos):
        if titulo == "" or nombre_socio == "" or not isinstance(dias_transcurridos, int) or dias_transcurridos < 0:
            raise ValueError("Datos inválidos")

        self.titulo = titulo
        self.nombre_socio = nombre_socio
        self.dias_transcurridos = dias_transcurridos

    def esta_vencido(self):
        return self.dias_transcurridos > 7

    def dias_de_retraso(self):
        if self.esta_vencido():
            return self.dias_transcurridos - 7
        return 0

    def resumen(self):
        if self.esta_vencido():
            return f"{self.titulo} - {self.nombre_socio} - vencido ({self.dias_de_retraso()} días)"
        return f"{self.titulo} - {self.nombre_socio} - en término"
