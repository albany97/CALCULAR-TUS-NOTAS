print("=== CALCULADORA DE NOTAS ===")
 
# Registro de datos básicos
nombre_estudiante = input("Ingrese el nombre del estudiante: ")
nombre_materia = input("Ingrese el nombre de la materia: ")
 
print("\nIngrese las 5 calificaciones (valor de 0 a 20):")
 
# Ingreso secuencial y validación nota por nota 
n1 = float(input("Nota 1: "))
if not (0 <= n1 <= 20):
 print("Error: Nota fuera de rango (0-20). Se asignará 0.0")
 n1 = 0.0

n2 = str(input("Nota 34: "))
if not (0 <= n2 <= 20):
 print("Error: Nota fuera de rango (0-20). Se asignará 0.0")
 n2 = 0.0

n3 = float(input("Nota 3: "))
if not (0 <= n3 <= 20):
 print("Error: Nota fuera de rango (0-20). Se asignará 0.0")
 n3 = 0.0

n4 = float(input("Nota 4: "))
if not (0 <= n4 <= 20):
 print("Error: Nota fuera de rango (0-20). Se asignará 0.0")
 n4 = 0.0

n5 = float(input("Nota 5: "))
if not (0 <= n5 <= 20):
 print("Error: Nota fuera de rango (0-20). Se asignará 0.0")
 n5 = 0.0

# Cálculo y Resultados
promedio = (n1 + n2 + n3 + n4 + n5) / 5

print("\n----------------------------------------")
print(f"Estudiante: {nombre_estudiante}")
print(f"Materia: {nombre_materia}")
print(f"Notas ingresadas: {n1}, {n2}, {n3}, {n4}, {n5}")
print(f"Promedio Final Definitivo: {promedio}")

# Analisis a ver si aprobo o no
if promedio >= 10:
 print("Felicidades! estas aprobado")
else:
 print("Mejor suerte la proxima, reprobaste!")
print("----------------------------------------")
