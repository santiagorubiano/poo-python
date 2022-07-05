import random
# import sys
contador = 0

def busqueda_binaria(objetivo, inicio, final, lista):
    global contador 
    contador += 1
    print(f'buscando {objetivo} entre {lista[inicio]} y {lista[final -1]}')
    
    if inicio > final:
        return False 
    mitad = (inicio + final )//2
    
    if lista[mitad] == objetivo:
        return True, contador
    
    elif lista[mitad] > objetivo:
        return busqueda_binaria(objetivo, inicio, mitad -1 , lista) 
    else:
        return busqueda_binaria(objetivo, mitad +1, final , lista) 

        
        
        
if __name__ == '__main__':
    tamaño_lista= int(input('ingresa cual es tamaño de la lista '))
    objetivo = int(input('ingrese el numero que quiere encotrar '))
    
    lista= sorted([random.randint(0,100) for i in range(tamaño_lista)]) 
    encontrado=  busqueda_binaria(objetivo, 0, len(lista),lista)
    print(f'{contador} fueron las iteraciones')
    print(lista)
    print(f'el numero {objetivo} {" esta "  if encontrado  else " no esta "} en la lista')
    
    