from lerMatriz import ler_matriz

# Função para exibir a matriz
def exibir_matriz(matriz):
    for linha in matriz:
        print(" ".join(f"{elem:.2f}" for elem in linha))
    print("\n")

# Função para escalonar a matriz e exibir cada passo
def escalonar_matriz(matriz, linhas, colunas):
    for i in range(min(linhas, colunas)):
        # Seleção do pivô
        if matriz[i][i] == 0:  # Se o pivô for zero, trocamos de linha
            for j in range(i + 1, linhas):
                if matriz[j][i] != 0:
                    matriz[i], matriz[j] = matriz[j], matriz[i]
                    print(f"Trocando linha {i+1} com linha {j+1}:")
                    exibir_matriz(matriz)
                    break
        
        # Normalização do pivô
        pivô = matriz[i][i]
        if pivô != 0:
            matriz[i] = [x / pivô for x in matriz[i]]
            print(f"Dividindo linha {i+1} pelo pivô {pivô:.2f}:")
            exibir_matriz(matriz)
        
        # Eliminação abaixo do pivô
        for j in range(i + 1, linhas):
            fator = matriz[j][i]
            matriz[j] = [matriz[j][k] - fator * matriz[i][k] for k in range(colunas)]
            print(f"Subtraindo {fator:.2f} * linha {i+1} da linha {j+1}:")
            exibir_matriz(matriz)

# Exemplo de uso
matriz, linhas, colunas = ler_matriz('matriz1.txt')
print("Matriz original:")
exibir_matriz(matriz)
escalonar_matriz(matriz, linhas, colunas)
