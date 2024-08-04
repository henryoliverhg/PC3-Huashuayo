class RECTANGULO:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho

    def calcular_area(self):
        return self.largo * self.ancho

class Cuadrado(RECTANGULO):
    def __init__(self, lado):
        super().__init__(lado, lado)

rectangulo = RECTANGULO(4, 5)
print(f'Área del rectángulo: {rectangulo.calcular_area()}')

cuadrado = Cuadrado(4)
print(f'Área del cuadrado: {cuadrado.calcular_area()}')