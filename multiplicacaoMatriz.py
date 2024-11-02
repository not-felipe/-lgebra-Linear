from lerMatriz import ler_matriz

matriz1, linhasMatriz1, colunasMatriz1 = ler_matriz('matriz1.txt')
matriz2, linhasMatriz2, colunasMatriz2 = ler_matriz('matriz2.txt')

def multiplicar_matriz(m1, l1, c1, m2, l2, c2):
    if c1 != l2:
        print('Matrizes não podem ser multiplicadas. O número de colunas da primeira matriz deve ser igual ao número de linhas da segunda.')
        return None

    resultado = [[0 for _ in range(c2)] for _ in range(l1)]
    
    for i in range(l1):
        for j in range(c2):
            for k in range(c1):
                resultado[i][j] += m1[i][k] * m2[k][j]
    
    return resultado

matriz_multiplicada = multiplicar_matriz(matriz1, linhasMatriz1, colunasMatriz1, matriz2, linhasMatriz2, colunasMatriz2)

if matriz_multiplicada is not None:
    print("Resultado da multiplicação das matrizes:")
    for linha in matriz_multiplicada:
        print(linha)
