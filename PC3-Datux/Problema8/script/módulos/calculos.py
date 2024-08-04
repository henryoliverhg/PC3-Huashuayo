import operaciones

print("Suma (3 + 5):", operaciones.Suma(3, 5))
print("Resta (10 - 4):", operaciones.Resta(10, 4))
print("Producto (6 * 7):", operaciones.Producto(6, 7))
print("División (8 / 2):", operaciones.Division(8, 2))

print("Suma ('a' + 5):", operaciones.Suma('a', 5))
print("Resta (10 - 'b'):", operaciones.Resta(10, 'b'))
print("Producto (6 * 'c'):", operaciones.Producto(6, 'c'))
print("División (8 / 0):", operaciones.Division(8, 0))
print("División ('d' / 2):", operaciones.Division('d', 2))
