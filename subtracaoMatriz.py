from lerMatriz import ler_matriz

matriz1, linhasMatriz1, colunasMatriz1 = ler_matriz('matriz1.txt')
matriz2, linhasMatriz2, colunasMatriz2 = ler_matriz('matriz2.txt')

def subtracao_matriz(m1, l1, c1, m2, l2, c2):
  if(l1 != l2 or c1 != c2):
    print('Matrizes de ordens diferentes não podem ser subtraidas')
    return None
  
  resultado = []
  for i in range(l1):
    linha = []
    for j in range(c1):
      linha.append(m1[i][j] - m2[i][j])
    resultado.append(linha)
    
  return resultado

matriz_subtraida = subtracao_matriz(matriz1, linhasMatriz1, colunasMatriz1, matriz2, linhasMatriz2, colunasMatriz2)

if matriz_subtraida is not None:
    print("Resultado da subtração das matrizes:")
    for linha in matriz_subtraida:
        print(linha)
