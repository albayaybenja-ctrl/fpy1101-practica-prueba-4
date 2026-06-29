# Actualizar stock de productos

def buscar_producto(productos, codigo):
    for producto in productos:
        if producto["codigo"] == codigo:
            return producto
    return None


def actualizar_stock(productos, codigo, nuevo_stock):
    producto = buscar_producto(productos, codigo)
    if producto:
        producto["stock"] = nuevo_stock
        return True
    return False


def mostrar_productos(productos):
    print("\n=== LISTA DE PRODUCTOS ===")
    for producto in productos:
        print(producto)


productos = [
    {"codigo": "P001", "nombre": "Teclado", "precio": 15000, "stock": 10},
    {"codigo": "P002", "nombre": "Mouse", "precio": 8000, "stock": 20},
    {"codigo": "P003", "nombre": "Monitor", "precio": 120000, "stock": 5}
]

codigo = input("Ingrese código del producto: ")

producto = buscar_producto(productos, codigo)

if producto:
    while True:
        try:
            nuevo_stock = int(input("Ingrese nuevo stock: "))
            if nuevo_stock >= 0:
                break
            else:
                print("El stock no puede ser negativo.")
        except ValueError:
            print("Debe ingresar un número entero.")

    actualizar_stock(productos, codigo, nuevo_stock)
    print("Stock actualizado correctamente.")
else:
    print("Producto no encontrado.")

mostrar_productos(productos)
