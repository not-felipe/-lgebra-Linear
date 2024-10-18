def ler_matriz(arquivo):
    with open(arquivo, 'r') as f:
        linhas = int(f.readline())  # Número de linhas
        colunas = int(f.readline())  # Número de colunas
        
        matriz = []
        for _ in range(linhas):
            linha = list(map(float, f.readline().split()))  # Lê uma linha da matriz e converte para inteiros
            matriz.append(linha)  # Adiciona a linha à matriz
            
    return matriz, int(linhas), int(colunas)
