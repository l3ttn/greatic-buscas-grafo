# DFS na arvore de departamentos. Mesma arvore da BFS, mas usa pilha (LIFO)
# em vez de fila: desce fundo num ramo antes de voltar.

arvore = {
    'Loja': [
        ('Eletronicos', 1),
        ('Moda', 1),
        ('Casa e Cozinha', 1),
        ('Games', 1),
        ('Beleza', 1)
        ],
    'Eletronicos': [('Fones de Ouvido', 1), ('Audio', 1)],
    'Fones de Ouvido': [],
    'Audio': [],
    'Moda': [('Relogios', 1), ('Bolsas', 1), ('Tenis', 1)],
    'Relogios': [],
    'Bolsas': [],
    'Tenis': [],
    'Casa e Cozinha': [('Moveis', 1), ('Eletrodomesticos', 1)],
    'Moveis': [],
    'Eletrodomesticos': [],
    'Games': [],
    'Beleza': [],
}

canais = {
    'Eletronicos': '#eletronicos', 'Fones de Ouvido': '#eletronicos', 'Audio': '#eletronicos',
    'Moda': '#moda', 'Relogios': '#moda', 'Bolsas': '#moda', 'Tenis': '#moda',
    'Casa e Cozinha': '#casa-cozinha', 'Moveis': '#casa-cozinha', 'Eletrodomesticos': '#casa-cozinha',
    'Games': '#games', 'Beleza': '#beleza',
}


def busca_dfs(arvore, inicio, objetivo):
    visitados = {inicio}
    pilha = [(inicio, [inicio], 0)]   # pilha = lista comum

    while pilha:
        departamento, caminho, nivel = pilha.pop()   # pop() tira o ultimo
        if departamento == objetivo:
            return caminho, nivel
        for filho, passo in arvore[departamento]:
            if filho not in visitados:
                visitados.add(filho)
                pilha.append((filho, [*caminho, filho], nivel + passo))
    return None, 0


# Teste da DFS
alvo = 'Tenis'
caminho_dfs, nivel_dfs = busca_dfs(arvore, 'Loja', alvo)
print("--- DFS departamentos Amazon ---")
print(f"Caminho: {' -> '.join(caminho_dfs)}" if caminho_dfs else "Departamento nao encontrado")
print(f"Profundidade: {nivel_dfs}")
print(f"Canal Discord: {canais.get(alvo, '#ofertas')}")
