class CIRCULO:
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 3.14159 * self.radio ** 2

class RECTANGULO:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho

    def area(self):
        return self.largo * self.ancho

class CUADRADO:
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado * self.lado
    
def validar_entrada(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor <= 0:
                raise ValueError("El número debe ser positivo.")
            return valor
        except ValueError as e:
            print(f"Entrada inválida: {e}. Inténtelo de nuevo.")


def mostrar_menu():
    print("Menú de opciones:")
    print("1. Calcular el área de un círculo")
    print("2. Calcular el área de un rectángulo")
    print("3. Calcular el área de un cuadrado")
    print("4. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-4): ")
        
        if opcion == '1':
            radio = validar_entrada("Ingrese el radio del círculo: ")
            circulo = CIRCULO(radio)
            print(f"El área del círculo es: {circulo.area()}")
        
        elif opcion == '2':
            largo = validar_entrada("Ingrese el largo del rectángulo: ")
            ancho = validar_entrada("Ingrese el ancho del rectángulo: ")
            rectangulo = RECTANGULO(largo, ancho)
            print(f"El área del rectángulo es: {rectangulo.area()}")
        
        elif opcion == '3':
            lado = validar_entrada("Ingrese el lado del cuadrado: ")
            cuadrado = CUADRADO(lado)
            print(f"El área del cuadrado es: {cuadrado.area()}")
        
        elif opcion == '4':
            print("Saliendo del programa.")
            break
        
        else:
            print("Opción no válida. Por favor, seleccione una opción entre 1 y 4.")

if __name__ == "__main__":
    main()