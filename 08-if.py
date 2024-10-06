puntaje = input("Ingrese su puntaje")
puntaje = int(puntaje)
if puntaje >= 95:
    print("aprobado con honores")
elif puntaje >=50:
    print("Alumno aprobado")
else:
    print("reprobado")

print("fuera del if")