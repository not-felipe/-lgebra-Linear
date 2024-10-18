from lerMatriz import ler_matriz

# Leitura das matrizes a partir dos arquivos
matriz1, linhasMatriz1, colunasMatriz1 = ler_matriz('matriz1.txt')
matriz2, linhasMatriz2, colunasMatriz2 = ler_matriz('matriz2.txt')

# Função para multiplicar matrizes
def multiplicar_matriz(m1, l1, c1, m2, l2, c2):
    # Verifica se a multiplicação é possível
    if c1 != l2:
        print('Matrizes não podem ser multiplicadas. O número de colunas da primeira matriz deve ser igual ao número de linhas da segunda.')
        return None
    
    # Inicializa a matriz resultado com zeros
    resultado = [[0 for _ in range(c2)] for _ in range(l1)]
    
    # Realiza a multiplicação das matrizes
    for i in range(l1):
        for j in range(c2):
            for k in range(c1):
                resultado[i][j] += m1[i][k] * m2[k][j]
    
    return resultado

# Multiplica as matrizes
matriz_multiplicada = multiplicar_matriz(matriz1, linhasMatriz1, colunasMatriz1, matriz2, linhasMatriz2, colunasMatriz2)

# Verifica se a multiplicação foi possível e imprime o resultado
if matriz_multiplicada is not None:
    print("Resultado da multiplicação das matrizes:")
    for linha in matriz_multiplicada:
        print(linha)
