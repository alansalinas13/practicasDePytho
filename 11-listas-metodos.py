lenguajes = ["Python","Ruby","PHP","JavaScript","Java"]
#agregar elementos al array, como primer parametro va el indice, lo inserta ahi, pero no elimina del array el dato que se encontraba en esa posicion, sino que mueve todos los registros desde el que le pasamos una posicion mas
lenguajes.insert(2,"Go")
lenguajes.insert(0,"C")
#eliminar registros de un array: no se le pasa el indice, sino el valor
lenguajes.remove("Ruby")
#verificar si exite en un arraya
print("c++" in lenguajes)
#limpiar el array
#lenguajes.clear()
#ver cuantos elementos tiene el array
print(len(lenguajes))
print(lenguajes)