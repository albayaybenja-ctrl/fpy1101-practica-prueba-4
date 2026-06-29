# Sistema de notas por estudiante

def validar_nota(mensaje):
    while True:
        try:
            nota = float(input(mensaje))

            if 1.0 <= nota <= 7.0:
                return nota
            else:
                print("La nota debe estar entre 1.0 y 7.0")

        except ValueError:
            print("Ingrese una nota válida.")


def calcular_promedio(n1, n2, n3):
    return (n1 + n2 + n3) / 3


def determinar_estado(promedio):
    if promedio >= 4.0:
        return "Aprobado"
    else:
        return "Reprobado"


def registrar_estudiante():
    nombre = input("Nombre del estudiante: ")

    nota1 = validar_nota("Nota 1: ")
    nota2 = validar_nota("Nota 2: ")
    nota3 = validar_nota("Nota 3: ")

    promedio = calcular_promedio(nota1, nota2, nota3)
    estado = determinar_estado(promedio)

    estudiante = {
        "nombre": nombre,
        "nota1": nota1,
        "nota2": nota2,
        "nota3": nota3,
        "promedio": round(promedio, 2),
        "estado": estado
    }

    return estudiante


def mostrar_resumen(estudiantes):
    print("\n=== RESUMEN DE ESTUDIANTES ===")

    for estudiante in estudiantes:
        print(f"Nombre: {estudiante['nombre']}")
        print(f"Promedio: {estudiante['promedio']}")
        print(f"Estado: {estudiante['estado']}")
        print("-" * 30)


estudiantes = []

while True:
    estudiantes.append(registrar_estudiante())

    continuar = input("¿Desea registrar otro estudiante? (s/n): ").lower()

    if continuar != "s":
        break

mostrar_resumen(estudiantes)
