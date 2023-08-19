#valores por defecto
def potenciacion(base = 2, exponente = 2):
    """
    Comentario en python, aca podemos comentar que hace la funcion 
    y los paramentros que utiliza. Luego llamamos con help(nombreFuncion) 
    para que nos lo retorne
    """
    return base ** exponente

#funciones lamda

potenciacionLambda = lambda base, exponente: base ** exponente


print(potenciacion(2, 3))

print(potenciacionLambda(2, 2))

help(potenciacion)