import random
def ordenamiento_por_insercion(lista):

    for indice in range(1, len(lista)):
        valor_actual = lista[indice]
        posicion_actual = indice

        while posicion_actual > 0 and lista[posicion_actual - 1] > valor_actual:
            lista[posicion_actual] = lista[posicion_actual - 1]
            posicion_actual -= 1

        lista[posicion_actual] = valor_actual
    return lista
if __name__ == '__main__':
    tamaño_lista= int(input('ingresa cual es tamaño de la lista '))
    
    lista= [random.randint(0,100) for i in range(tamaño_lista)]
    print(lista)
    lista_ordenada = ordenamiento_por_insercion(lista)    

    print(lista_ordenada)
    