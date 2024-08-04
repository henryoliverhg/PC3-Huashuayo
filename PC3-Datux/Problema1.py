def Combustible():
    try:
      
        fraccion = input("Introduce una fracción (formato X/Y): ")
        
        x_str, y_str = fraccion.split('/')
        x = int(x_str)
        y = int(y_str)
        
        if not (isinstance(x, int) and isinstance(y, int)):
            raise ValueError("Ambos valores deben ser números enteros.")
        
        if y == 0:
            raise ZeroDivisionError("El denominador no puede ser cero.")
        
        porcentaje = (x / y) * 100
        
        if porcentaje <= 1:
            print("En caso X/Y sea menor a 1% del total: Vacío")
        elif porcentaje >= 99:
            print("En caso X/Y sea mayor a 99% del total: Lleno")
        else:
            print(f"El nivel de combustible es: {porcentaje:.0f}%")

    except ValueError as ve:
        print("Error:", ve)
    except ZeroDivisionError as zde:
        print("Error:", zde)
    except Exception as e:
        print("Error inesperado:", e)

if __name__== "__main__":
    Combustible()
