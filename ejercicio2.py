# Buscar productos por código

def buscar_producto(productos, codigo):
    for producto in productos:
        if producto["codigo"] == codigo:
            return producto
    return None


def mostrar_producto(producto):
    print("\nProducto encontrado:")
    print(f"Código: {producto['codigo']}")
    print(f"Nombre: {producto['nombre']}")
    print(f"Precio: ${producto['precio']}")
    print(f"Stock: {producto['stock']}")


productos = [
    {"codigo": "P001", "nombre": "Teclado", "precio": 15000, "stock": 10},
    {"codigo": "P002", "nombre": "Mouse", "precio": 8000, "stock": 20},
    {"codigo": "P003", "nombre": "Monitor", "precio": 120000, "stock": 5},
    {"codigo": "P004", "nombre": "Impresora", "precio": 90000, "stock": 3}
]

codigo = input("Ingrese código del producto: ")

producto = buscar_producto(productos, codigo)

if producto:
    mostrar_producto(producto)
else:
    print("Producto no encontrado.")
