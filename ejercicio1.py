# Registro de estudiantes

def registrar_estudiante():
    estudiante = {
        "rut": input("Ingrese RUT: "),
        "nombre": input("Ingrese nombre: "),
        "edad": int(input("Ingrese edad: ")),
        "carrera": input("Ingrese carrera: ")
    }
    return estudiante


def mostrar_estudiantes(estudiantes):
    print("\n=== ESTUDIANTES REGISTRADOS ===")
    for estudiante in estudiantes:
        print(f"RUT: {estudiante['rut']}")
        print(f"Nombre: {estudiante['nombre']}")
        print(f"Edad: {estudiante['edad']}")
        print(f"Carrera: {estudiante['carrera']}")
        print("-" * 30)


estudiantes = []

for i in range(3):
    print(f"\nRegistro estudiante {i + 1}")
    estudiantes.append(registrar_estudiante())

mostrar_estudiantes(estudiantes)
