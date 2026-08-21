from solucion.prestamo import Prestamo

def probar(titulo, nombre_socio, dias_transcurridos):
    try:
        prestamo = Prestamo(titulo, nombre_socio, dias_transcurridos)
        print(prestamo.resumen())
    except ValueError as e:
        print("Préstamo inválido:", e)

if __name__ == "__main__":
    probar("El Quijote", "Juan Perez", 3)
    probar("1984", "Maria Garcia", 10)
    probar("Cien años de soledad", "Pedro Martinez", 7)
    probar("Dorian Gray", "Ana Lopez", "4")