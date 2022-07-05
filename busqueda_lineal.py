import random
def busqueda(lista, objetivo):
    match= False
    for elemento in lista:
        if elemento == objetivo: 
            match = True
            break
    return match
        
        
        
if __name__ == '__main__':
    tamaño_lista= int(input('ingresa cual es tamaño de la lista '))
    objetivo = int(input('ingrese el numero que quiere encotrar '))
    
    lista= [random.randint(0,100) for i in range(tamaño_lista)]
    encontrado= busqueda(lista, objetivo)
    print(lista)
    print(f'el numero {objetivo} {" esta "  if encontrado  else " no esta "} en la lista')
    
    
