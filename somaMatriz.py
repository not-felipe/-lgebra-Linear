from lerMatriz import ler_matriz

matriz1, linhasMatriz1, colunasMatriz1 = ler_matriz('matriz1.txt')
matriz2, linhasMatriz2, colunasMatriz2 = ler_matriz('matriz2.txt')

def soma_matriz(m1, l1, c1, m2, l2, c2):
  if(l1 != l2 or c1 != c2):
    print('Matrizes de ordens diferentes não podem ser somadas')
    return None
  
  resultado = []
  for i in range(l1):
    linha = []
    for j in range(c1):
      linha.append(m1[i][j] + m2[i][j])
    resultado.append(linha)
    
  return resultado

matriz_somada = soma_matriz(matriz1, linhasMatriz1, colunasMatriz1, matriz2, linhasMatriz2, colunasMatriz2)

if matriz_somada is not None:
    print("Resultado da soma das matrizes:")
    for linha in matriz_somada:
        print(linha)

