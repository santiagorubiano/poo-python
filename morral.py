def morral(tamano_morral, pesos, valores, n):

    if n == 0 or tamano_morral == 0:
        return 0

    if pesos[n - 1] > tamano_morral:
        return morral(tamano_morral, pesos, valores, n - 1)

    return max(valores[n - 1] + morral(tamano_morral - pesos[n - 1], pesos, valores, n - 1),
                morral(tamano_morral, pesos, valores, n - 1))
        

if __name__ == '__main__':
    valores = [60, 100, 120]
    pesos = [10, 20, 30]
    tamano_morral = 25
    n = len(valores)

    resultado = morral(tamano_morral, pesos, valores, n)
    print(resultado)
    print(f'El valor maximo que podemos robar es {resultado}')
    print('La complejidad del algoritmo es O(nW) donde n es el numero de elementos y W el tamano del morral')
