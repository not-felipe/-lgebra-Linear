def ler_matriz(arquivo):
    with open(arquivo, 'r') as f:
        linhas = int(f.readline())  
        colunas = int(f.readline())  
        
        matriz = []
        for _ in range(linhas):
            linha = list(map(float, f.readline().split()))  
            matriz.append(linha)
            
    return matriz, int(linhas), int(colunas)
