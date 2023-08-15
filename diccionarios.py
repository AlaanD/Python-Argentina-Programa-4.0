
#diccionarios

dic = dict({
    1: "alan",
    2: "dri"           
})

dic2 = {}

#primer elemento clave, segundo valor
dic2 = {
    "clave": True,
    "dic": "valor",
    5: 6
}

print(dic2)

#para acceder al valor lo hacemos desde la clave
print(dic2["clave"])

print("Imprimimos las claves")
for key in dic2.keys():
    print(key)

print("Imprimimos los valores")
for value in dic2.values():
    print(value)

print("Imprimimos las claves y los valores")
for key, value in dic2.items():
    print(f'key {key}, value {value}')

#para vaciar un diccionario

print("Diciconario antes de vaciarlo: " + str(dic))
dic.clear()
print("Diciconario despues de vaciarlo: " + str(dic))

#para obtener del valor de una clave usamos get
print(dic2.get("clave"))

#si no la encuentra devuelve none
print(dic2.get("alan"))

#tambien podemos setearle un valor por defecto si no encuentra el valor
print(dic2.get("alan", "dri"))

#la funcion len devuelve la cantidad de elementos dentro de un diccionario
print("La cantidad de elementos en el dic2 es: " + str(len(dic2)))

#retorna si un elemento se encuentra en un diccionario
result = "alan" in dic2
print(result)

#negacion de lo anterior
result = "alan" not in dic2
print(result)
