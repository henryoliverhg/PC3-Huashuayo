def Obtener_calificaciones():
    calificaciones_str = input("Introduce una lista de calificaciones separadas por comas: ")
    calificaciones_lista = calificaciones_str.split(',')
    calificaciones = []

    for calificacion in calificaciones_lista:
        try:
            calificaciones.append(int(calificacion.strip()))
        except ValueError:
            print(f"Error: '{calificacion}' No es un número válido.")

    return calificaciones

calificaciones = Obtener_calificaciones()
print("Las calificaciones válidas son: ", calificaciones)