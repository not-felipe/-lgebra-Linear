from lerMatriz import ler_matriz

matriz1, linhasMatriz1, colunasMatriz1 = ler_matriz('matriz1.txt')
escalar = float(input("Digite o número para multiplicar a matriz: "))

def multiplicar_escalar(m1, l1, c1, escalar):
  resultado = []
  for i in range(l1):
    linha = []
    for j in range(c1):
      linha.append(m1[i][j] * escalar)
    resultado.append(linha)
    
  return resultado

matriz_multiplicada = multiplicar_escalar(matriz1, linhasMatriz1, colunasMatriz1, escalar)


for linha in matriz_multiplicada:
  print(linha)