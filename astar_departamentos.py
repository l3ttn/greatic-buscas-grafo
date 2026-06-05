# A* na arvore de departamentos. Escolhe o menor f = g + h:
# g = custo real ja percorrido, h = estimativa (niveis que faltam).
# Aqui as arestas tem pesos diferentes pra o custo fazer diferenca.

import heapq

arvore = {
    'Loja': [
        ('Eletronicos', 2),
        ('Moda', 1),
        ('Casa e Cozinha', 3),
        ('Games', 1),
        ('Beleza', 2)
        ],
    'Eletronicos': [('Fones de Ouvido', 1), ('Audio', 4)],
    'Fones de Ouvido': [],
    'Audio': [],
    'Moda': [('Relogios', 2), ('Bolsas', 1), ('Tenis', 1)],
    'Relogios': [],
    'Bolsas': [],
    'Tenis': [],
    'Casa e Cozinha': [('Moveis', 1), ('Eletrodomesticos', 2)],
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

# Nivel de cada departamento na arvore (usado pela heuristica)
profundidade = {
    'Loja': 0,
    'Eletronicos': 1, 'Moda': 1, 'Casa e Cozinha': 1, 'Games': 1, 'Beleza': 1,
    'Fones de Ouvido': 2, 'Audio': 2, 'Relogios': 2, 'Bolsas': 2, 'Tenis': 2,
    'Moveis': 2, 'Eletrodomesticos': 2,
}


def heuristica(no, objetivo):
    return abs(profundidade[objetivo] - profundidade[no])   # niveis que faltam


def busca_astar(arvore, inicio, objetivo):
    visitados = set()
    fila = [(heuristica(inicio, objetivo), 0, inicio, [inicio])]   # (f, g, no, caminho)

    while fila:
        f, g, departamento, caminho = heapq.heappop(fila)   # menor f primeiro
        if departamento == objetivo:
            return caminho, g
        if departamento in visitados:
            continue
        visitados.add(departamento)
        for filho, peso in arvore[departamento]:
            if filho not in visitados:
                g_novo = g + peso
                f_novo = g_novo + heuristica(filho, objetivo)
                heapq.heappush(fila, (f_novo, g_novo, filho, [*caminho, filho]))
    return None, 0


# Teste do A*
alvo = 'Tenis'
caminho_astar, custo_astar = busca_astar(arvore, 'Loja', alvo)
print("--- A* departamentos Amazon ---")
print(f"Caminho: {' -> '.join(caminho_astar)}" if caminho_astar else "Departamento nao encontrado")
print(f"Custo real (g): {custo_astar}")
print(f"Canal Discord: {canais.get(alvo, '#ofertas')}")
