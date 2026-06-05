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

# Departamento -> canal Discord onde a oferta e publicada.
canais = {
    'Eletronicos': '#eletronicos', 'Fones de Ouvido': '#eletronicos', 'Audio': '#eletronicos',
    'Moda': '#moda', 'Relogios': '#moda', 'Bolsas': '#moda', 'Tenis': '#moda',
    'Casa e Cozinha': '#casa-cozinha', 'Moveis': '#casa-cozinha', 'Eletrodomesticos': '#casa-cozinha',
    'Games': '#games', 'Beleza': '#beleza',
}

from collections import deque

def busca_bfs(arvore, inicio, objetivo):
    caminho_percorrido = [inicio]
    visitados = {inicio}
    nivel_acumulado = 0
    fila = deque([(inicio, caminho_percorrido, nivel_acumulado)])

    while fila:
        departamento, caminho, nivel = fila.popleft()
        if departamento == objetivo:
            return caminho, nivel
        for filho, passo in arvore[departamento]:
            if filho not in visitados:
                visitados.add(filho)
                fila.append((filho, [*caminho, filho], nivel + passo))
    return None, 0


# Teste da BFS
alvo = 'Fones de Ouvido'
caminho_bfs, nivel_bfs = busca_bfs(arvore, 'Loja', alvo)
print("--- BFS departamentos Amazon ---")
print(f"Caminho: {' -> '.join(caminho_bfs)}" if caminho_bfs else "Departamento nao encontrado")
print(f"Profundidade: {nivel_bfs}")
print(f"Canal Discord: {canais.get(alvo, '#ofertas')}")
