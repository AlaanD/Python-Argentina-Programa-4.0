#lista
#Las listas son una estructura de datos que permiten 
#almacenar elementos de distintos tipos

lista = list([1, 2, 3])
lista2 = []

lista2 = [4, 7, 3, "hola"]

for i in lista:
    print(i)

#agregar un elemento a la lista

#lo agrega al final
lista2.append("final")

#inserta el elemento en la posicion que elegimos con el primer parametro
lista2.insert(2, "donde")

lista[1] = 5

#elimina el elemento pasado por parametro
#si esta repetido solo elimina el primero que encuentra
lista2.remove("final")

#eliminamos el elemento en la posicion que le pasamos
lista2.pop(1)

for i in lista2:
    print(i)

#contateno listas
lista3 = lista2 + lista

print("Lista concatenada: " + str(lista3))

#para invertir el orden
lista_invertida = lista2[::-1]
print("Lista2 invertida: " + str(lista_invertida))

#ordenar lista
lista4 = [5, 2, 3, 8, 1]
lista4.sort()
print("Lista4 ordenada: " + str(lista4))

#vaciar la lista
lista4.clear()
print("Vaciamos la lista4: " + str(lista4))
