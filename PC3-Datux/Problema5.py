class Alumno:
    def __init__(self, nombre, numero_registro):
        self.nombre = nombre
        self.numero_registro = numero_registro
        self.edad = None
        self.nota = None

    def display(self):
        print(f"Nombre: {self.nombre}")
        print(f"Número de registro: {self.numero_registro}")
        if self.edad is not None:
            print(f"Edad: {self.edad}")
        if self.nota is not None:
            print(f"Nota: {self.nota}")

    def set_age(self, edad):
        self.edad = edad

    def set_nota(self, nota):
        self.nota = nota

#Ejemplo

alumno1 = Alumno("Henry Huashuayo", "20152364")
alumno1.display()
alumno1.set_age(25)
alumno1.set_nota(95)
alumno1.display()