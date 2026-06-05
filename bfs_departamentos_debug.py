# BFS de departamentos com print rodada a rodada (mostra a fila e os filhos).
from collections import deque

arvore = {
    'Loja': [('Eletronicos', 1), ('Moda', 1), ('Casa e Cozinha', 1), ('Games', 1), ('Beleza', 1)],
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


def busca_bfs(arvore, inicio, objetivo):
    visitados = {inicio}
    fila = deque([(inicio, [inicio], 0)])

    rodada = 0
    while fila:
        rodada += 1
        departamento, caminho, nivel = fila.popleft()

        print("\n" + "=" * 64)
        print(f"RODADA {rodada}   ->   no expandido: {departamento}")
        print(f"   caminho ate aqui: {caminho}")

        if departamento == objetivo:
            print(f"   >>> {departamento} e o OBJETIVO. return encerra. FIM.")
            return caminho, nivel

        nomes_filhos = [f for f, p in arvore[departamento]]
        print(f"   sub-departamentos de {departamento}: {nomes_filhos}")

        gerou = 0
        for filho, passo in arvore[departamento]:
            if filho in visitados:
                print(f"   [x] {filho:<18} JA VISITADO  -> barrado")
            else:
                visitados.add(filho)
                caminho_filho = [*caminho, filho]
                fila.append((filho, caminho_filho, nivel + passo))
                gerou += 1
                print(f"   [+] {filho:<18} NOVO  -> entra na fila, caminho = {caminho_filho}")

        print(f"   >> {departamento} gerou {gerou} filho(s) nesta rodada.")
        print(f"   >> FILA agora (frente -> tras): {[x[0] for x in fila]}")

    return None, 0


print("LEGENDA:  [+] = no novo, entra na fila   |   [x] = ja visitado, barrado\n")
alvo = 'Tenis'
caminho_bfs, nivel_bfs = busca_bfs(arvore, 'Loja', alvo)
print("\n" + "=" * 64)
print("--- RESULTADO FINAL ---")
print(f"Caminho: {' -> '.join(caminho_bfs)}" if caminho_bfs else "Departamento nao encontrado")
print(f"Profundidade: {nivel_bfs}")
print(f"Canal Discord: {canais.get(alvo, '#ofertas')}")
