grado = float(input("Ingrese temperatura a convertir: "))
tipo = input("Es Fahrenheit (F) o Celsius (C)?: ")
if tipo == "C" or tipo == "c":
    resul = (grado * 9/5) + 32
    print("la temperatura en celsius es: ", resul)
elif tipo == "F" or tipo =="f":
    resul = (grado - 32) * 5/9
    print("la temperatura en Fahrenheit es: ", resul)
else:
    print("Escala incorrecta")
