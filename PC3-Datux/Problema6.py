class Producto:
    def __init__(self, id_producto, nombre, marca, año, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.marca = marca
        self.año = año
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Marca: {self.marca}, Año: {self.año}, Precio: ${self.precio}"


class Catalogo:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        for producto in self.productos:
            print(producto)

    def filtrar_por_año(self, año):
        return [producto for producto in self.productos if producto.año == año]

    def filtrar_por_marca(self, marca):
        return [producto for producto in self.productos if producto.marca.lower() == marca.lower()]


producto1 = Producto(1, "Filtro de aceite", "Ford", 2022, 20)
producto2 = Producto(2, "Bujía", "Nissan", 2021, 7)
producto3 = Producto(3, "Batería", "Toyota", 2020, 100)

catalogo = Catalogo()

catalogo.agregar_producto(producto1)
catalogo.agregar_producto(producto2)
catalogo.agregar_producto(producto3)

print("Lista de productos en el catálogo:")
catalogo.mostrar_productos()

año_filtrado = 2021
productos_filtrados_año = catalogo.filtrar_por_año(año_filtrado)
print(f"\nProductos del año {año_filtrado}:")
for producto in productos_filtrados_año:
    print(producto)

marca_filtrada = "Toyota"
productos_filtrados_marca = catalogo.filtrar_por_marca(marca_filtrada)
print(f"\nProductos de la marca {marca_filtrada}:")
for producto in productos_filtrados_marca:
    print(producto)