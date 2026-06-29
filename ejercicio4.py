# CRUD simple de cursos

def buscar_curso(cursos, codigo):
    for curso in cursos:
        if curso["codigo"] == codigo:
            return curso
    return None


def agregar_curso(cursos):
    codigo = input("Código del curso: ")

    if buscar_curso(cursos, codigo):
        print("El código ya existe.")
        return

    nombre = input("Nombre del curso: ")
    docente = input("Docente: ")

    while True:
        try:
            cantidad = int(input("Cantidad de estudiantes: "))
            if cantidad > 0:
                break
            else:
                print("Debe ser mayor que 0.")
        except ValueError:
            print("Ingrese un número válido.")

    curso = {
        "codigo": codigo,
        "nombre": nombre,
        "docente": docente,
        "cantidad_estudiantes": cantidad
    }

    cursos.append(curso)
    print("Curso agregado correctamente.")


def listar_cursos(cursos):
    if len(cursos) == 0:
        print("No existen cursos registrados.")
        return

    print("\n=== CURSOS ===")
    for curso in cursos:
        print(curso)


def eliminar_curso(cursos, codigo):
    curso = buscar_curso(cursos, codigo)

    if curso:
        cursos.remove(curso)
        print("Curso eliminado.")
    else:
        print("Curso no encontrado.")


cursos = []

while True:
    print("\n=== MENÚ ===")
    print("1. Agregar curso")
    print("2. Listar cursos")
    print("3. Buscar curso")
    print("4. Eliminar curso")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_curso(cursos)

    elif opcion == "2":
        listar_cursos(cursos)

    elif opcion == "3":
        codigo = input("Ingrese código del curso: ")
        curso = buscar_curso(cursos, codigo)

        if curso:
            print(curso)
        else:
            print("Curso no encontrado.")

    elif opcion == "4":
        codigo = input("Ingrese código del curso a eliminar: ")
        eliminar_curso(cursos, codigo)

    elif opcion == "5":
        print("Programa finalizado.")
        break

    else:
        print("Opción inválida.")
