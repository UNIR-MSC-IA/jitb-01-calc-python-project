"""
Calculadora de promedios escolares
Autor: Ing. Javier Toquica
"""

def ingresar_calificaciones():
    nombres = []
    calificaciones = []
    while True:
        nombre = input("Ingrese el nombre de la materia: ").strip()
        if not nombre:
            print("El nombre no puede estar vacío.")
            continue
        while True:
            try:
                calif = float(input(f"Ingrese la calificación para {nombre} (0-10): "))
                if 0 <= calif <= 10:
                    break
                else:
                    print("La calificación debe estar entre 0 y 10.")
            except ValueError:
                print("Por favor, ingrese un número válido.")
        nombres.append(nombre)
        calificaciones.append(calif)
        continuar = input("¿Desea ingresar otra materia? (s/n): ").strip().lower()
        if continuar != 's':
            break
    return nombres, calificaciones

def calcular_promedio(calificaciones):
    if not calificaciones:
        return 0
    return sum(calificaciones) / len(calificaciones)

def determinar_estado(calificaciones, umbral=5.0):
    aprobadas = [i for i, c in enumerate(calificaciones) if c >= umbral]
    reprobadas = [i for i, c in enumerate(calificaciones) if c < umbral]
    return aprobadas, reprobadas

def encontrar_extremos(calificaciones):
    if not calificaciones:
        return None, None
    max_idx = calificaciones.index(max(calificaciones))
    min_idx = calificaciones.index(min(calificaciones))
    return max_idx, min_idx

def main():
    print("Bienvenido a la calculadora de promedios escolares de la UNIR\n")
    nombres, calificaciones = ingresar_calificaciones()
    if not nombres:
        print("No se ingresaron materias. Programa finalizado.")
        return
    promedio = calcular_promedio(calificaciones)
    aprobadas, reprobadas = determinar_estado(calificaciones)
    max_idx, min_idx = encontrar_extremos(calificaciones)

    print("\nResumen de calificaciones:")
    for i, (n, c) in enumerate(zip(nombres, calificaciones)):
        print(f"{i+1}. {n}: {c}")
    print(f"\nPromedio general: {promedio:.2f}")
    print("\nMaterias aprobadas:")
    if aprobadas:
        for i in aprobadas:
            print(f"- {nombres[i]} ({calificaciones[i]})")
    else:
        print("Ninguna")
    print("\nMaterias reprobadas:")
    if reprobadas:
        for i in reprobadas:
            print(f"- {nombres[i]} ({calificaciones[i]})")
    else:
        print("Ninguna")
    if max_idx is not None:
        print(f"\nMateria con mejor calificación: {nombres[max_idx]} ({calificaciones[max_idx]})")
    if min_idx is not None:
        print(f"Materia con peor calificación: {nombres[min_idx]} ({calificaciones[min_idx]})")
    print("\n¡Gracias por usar la calculadora de promedios!\n")

if __name__ == "__main__":
    main()
