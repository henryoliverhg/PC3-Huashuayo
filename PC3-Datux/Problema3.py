import math

class CIRCULO:
    def __init__(self, radio):
        self.radio = radio
    
    def CalcularArea(self):
        return math.pi * self.radio ** 2

Circulo1 = CIRCULO(3)
Circulo2 = CIRCULO(5)

area1 = Circulo1.CalcularArea()
area2 = Circulo2.CalcularArea()

print(f"El área del círculo con radio 3 es: {area1}")
print(f"El área del círculo con radio 5 es: {area2}")