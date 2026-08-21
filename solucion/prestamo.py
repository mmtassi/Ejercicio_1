

class Prestamo:
    def __init__(self, titulo, nombre_socio, dias_transcurridos):
        self.titulo = titulo
        self.nombre_socio = nombre_socio
        self.dias_transcurridos = dias_transcurridos

    def esta_vencido(self):
        return self.dias_transcurridos > 7

    def dias_de_retraso(self):
        if self.esta_vencido():
            return 7 - self.dias_transcurridos
        else:
            return 0

    def resumen(self):
        if self.esta_vencido():
            return  f"'{self.titulo}' - '{self.nombre_socio}' - vencido ('{self.dias_de_retraso()}' dias).\n"
        else:
            return f"'{self.titulo}' - '{self.nombre_socio}' - en termino.\n"

prestamo = Prestamo("El Quijote", "Juan Perez", 1)

print(prestamo.resumen())