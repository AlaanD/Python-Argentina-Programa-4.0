#similares a las listas pero no admiten elementos repetidos

#creamos uno
mi_set = set([1, 2, 3])

#anadir un elemento
mi_set.add(11)
print(mi_set)

#eliminar, lanza excepcion si el elemento no se encuentra en el conjunto
mi_set.remove(2)

#lo mismo que remove pero no lanza excepcion si no se encuentra el elemento
mi_set.discard(1)

print(mi_set)

#para vaciar el conjunto
mi_set.clear()

#para unir dos conjuntos
mi_set2 = set([4, 5, 6])

mi_set3 = mi_set.union(mi_set2)

print(mi_set3)

#interseccion
mi_set.clear()
mi_set2.clear()
mi_set3.clear()

mi_set = set([1, 2, 3])
mi_set2 = set([3, 4, 5])

mi_set3 = mi_set.intersection(mi_set2)

print(mi_set3)

#diferencia

mi_set3 = mi_set.difference(mi_set2)

print(mi_set3)

mi_set3 = mi_set2.difference(mi_set)
print(mi_set3)