def Suma(a, b):
    try:
        return a + b
    except TypeError:
        return "Error: Tipo de dato no válido."

def Resta(a, b):
    try:
        return a - b
    except TypeError:
        return "Error: Tipo de dato no válido."

def Producto(a, b):
    try:
        return a * b
    except TypeError:
        return "Error: Tipo de dato no válido."

def Division(a, b):
    try:
        if b == 0:
            return "Error: No es posible dividir entre cero."
        return a / b
    except TypeError:
        return "Error: Tipo de dato no válido."
