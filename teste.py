import heapq
import view_map as vw

# Representação dos tipos de células e custos
CUSTO_VAZIO = 1
CUSTO_LAMA = 5
OBSTACULO = '#'
TESOURO = 'T'

# Define os movimentos possíveis: (linha, coluna)
MOVIMENTOS = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Cima, baixo, esquerda, direita

def busca_custo_uniforme(mapa, inicio, tesouro):
    # Fila de prioridade para armazenar (custo acumulado, posição, caminho até aqui)
    fila = [(0, inicio, [inicio])]  # (custo, (linha, coluna), caminho percorrido)
    visitados = set()  # Conjunto de posições já visitadas para evitar ciclos

    while fila:
        # Retira da fila a posição com menor custo acumulado
        custo_atual, (linha, coluna), caminho = heapq.heappop(fila)
        
        # Verifica se encontrou o tesouro
        if (linha, coluna) == tesouro:
            return caminho  # Retorna o caminho percorrido até o tesouro

        # Marca a posição atual como visitada
        if (linha, coluna) in visitados:
            continue
        visitados.add((linha, coluna))

        # Explora vizinhos
        for movimento in MOVIMENTOS:
            nova_linha = linha + movimento[0]
            nova_coluna = coluna + movimento[1]

            # Verifica se está dentro dos limites do mapa
            if 0 <= nova_linha < len(mapa) and 0 <= nova_coluna < len(mapa[0]):
                tipo_celula = mapa[nova_linha][nova_coluna]

                # Ignora obstáculos
                if tipo_celula == OBSTACULO:
                    continue

                # Calcula o custo do movimento para a célula
                novo_custo = custo_atual
                if tipo_celula == '.':
                    novo_custo += CUSTO_VAZIO
                elif tipo_celula == 'L':
                    novo_custo += CUSTO_LAMA

                # Adiciona a nova posição à fila com o custo atualizado e o caminho estendido
                novo_caminho = caminho + [(nova_linha, nova_coluna)]
                heapq.heappush(fila, (novo_custo, (nova_linha, nova_coluna), novo_caminho))

    # Retorna um array vazio se não houver caminho possível
    return []


def heuristica_manhattan(posicao_atual, tesouro):
    """Calcula a heurística de Manhattan entre a posição atual e o tesouro."""
    return abs(posicao_atual[0] - tesouro[0]) + abs(posicao_atual[1] - tesouro[1])

def busca_gulosa(mapa, inicio, tesouro):
    # Fila de prioridade para armazenar (heurística, posição, caminho até aqui)
    fila = [(heuristica_manhattan(inicio, tesouro), inicio, [inicio])]
    visitados = set()  # Conjunto de posições já visitadas para evitar ciclos

    while fila:
        # Retira da fila a posição com menor valor de heurística
        _, (linha, coluna), caminho = heapq.heappop(fila)
        
        # Verifica se encontrou o tesouro
        if (linha, coluna) == tesouro:
            return caminho  # Retorna o caminho percorrido até o tesouro

        # Marca a posição atual como visitada
        if (linha, coluna) in visitados:
            continue
        visitados.add((linha, coluna))

        # Explora vizinhos
        for movimento in MOVIMENTOS:
            nova_linha = linha + movimento[0]
            nova_coluna = coluna + movimento[1]

            # Verifica se está dentro dos limites do mapa
            if 0 <= nova_linha < len(mapa) and 0 <= nova_coluna < len(mapa[0]):
                tipo_celula = mapa[nova_linha][nova_coluna]

                # Ignora obstáculos
                if tipo_celula == OBSTACULO:
                    continue

                # Calcula a heurística para a nova posição
                heuristica = heuristica_manhattan((nova_linha, nova_coluna), tesouro)
                novo_caminho = caminho + [(nova_linha, nova_coluna)]

                # Adiciona a nova posição à fila com a heurística calculada
                heapq.heappush(fila, (heuristica, (nova_linha, nova_coluna), novo_caminho))

    # Retorna um array vazio se não houver caminho possível
    return []

def busca_a_estrela(mapa, inicio, tesouro):
    fila = [(0 + heuristica_manhattan(inicio, tesouro), 0, inicio, [inicio])]
    visitados = {}

    while fila:
        custo_total_estimado, custo_atual, (linha, coluna), caminho = heapq.heappop(fila)

        if (linha, coluna) == tesouro:
            return caminho  # Retorna o caminho percorrido até o tesouro

        # Marca a posição atual com o custo mínimo
        if (linha, coluna) in visitados and visitados[(linha, coluna)] <= custo_atual:
            continue
        visitados[(linha, coluna)] = custo_atual

        # Explora vizinhos
        for movimento in MOVIMENTOS:
            nova_linha = linha + movimento[0]
            nova_coluna = coluna + movimento[1]

            # Verifica se está dentro dos limites do mapa
            if 0 <= nova_linha < len(mapa) and 0 <= nova_coluna < len(mapa[0]):
                tipo_celula = mapa[nova_linha][nova_coluna]

                # Ignora obstáculos
                if tipo_celula == OBSTACULO:
                    continue

                # Calcula o novo custo acumulado para a nova posição
                novo_custo = custo_atual + (CUSTO_VAZIO if tipo_celula == '.' else CUSTO_LAMA)

                # Se já visitamos a posição com um custo menor, ignore esta rota
                if (nova_linha, nova_coluna) in visitados and visitados[(nova_linha, nova_coluna)] <= novo_custo:
                    continue

                # Calcula o custo total estimado para a nova posição
                heuristica = heuristica_manhattan((nova_linha, nova_coluna), tesouro)
                custo_total_estimado = novo_custo + heuristica
                novo_caminho = caminho + [(nova_linha, nova_coluna)]

                # Adiciona a nova posição à fila com o custo estimado total
                heapq.heappush(fila, (custo_total_estimado, novo_custo, (nova_linha, nova_coluna), novo_caminho))

    # Retorna um array vazio se não houver caminho possível
    return []
# Exemplo de uso
mapa = [
    ['I', '#', '.', '#', 'L', 'L', 'T'],
    ['.', '#', '.', '#', 'L', '#', '.'],
    ['.', '#', '.', '#', 'L', '#', '.'],
    ['.', '#', '.', '.', '.', '#', '.'],
    ['.', '#', '.', '#', '.', '#', '.'],
    ['.', '#', '.', '#', '.', '#', '.'],
    ['.', '.', '.', '#', '.', '.', '.']
]

grid1 = [
    ['I', '.', '#', '.', '.', '.', '.', '.', '.', '.'],
    ['#', '.', '#', '#', '.', '#', '#', '.', '#', '.'],
    ['.', '.', '.', '.', '.', '.', '#', '.', '.', '.'],
    ['#', '.', '#', '.', '#', '.', '.', '.', '#', '.'],
    ['.', '.', '#', '.', '.', '#', '#', '.', '#', '.'],
    ['.', '#', '.', '.', '.', '.', '#', '.', '#', '.'],
    ['.', '.', '.', '#', '.', '.', '.', '.', '#', 'T'],
    ['.', '#', '#', '.', '#', '#', '.', '#', '#', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '#', '.'],
    ['.', '.', '#', '.', '#', '.', '#', '.', '.', '.'],
]
pos_inicial1 = (0, 0)
pos_tesouro1 = (6, 9)

grid2 = [
    ['I', '.', '.', '.', '.', '.'],
    ['#', '#', '.', '#', '#', '.'],
    ['.', '.', '.', '#', 'L', '.'],
    ['.', 'L', '#', 'T', '.', '.'],
    ['.', '.', '.', '.', '.', '.']
]
pos_inicial2 = (0, 0)
pos_tesouro2 = (3, 3)

grid3 = [
    ['I', '.', 'L', 'L', 'L', '.', 'T'],
    ['.', '.', '.', 'L', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.'],
]
pos_inicial3 = (0, 0)
pos_tesouro3 = (0, 6)


# bcu_esperado1 = [(0, 0), (0, 1), (1, 1), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (3, 5), (3, 6), (3, 7), (2, 7), (2, 8), (2, 9), (3, 9), (4, 9), (5, 9), (6, 9)]
# bcu_esperado2 = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (1, 5), (2, 5), (3, 5), (3, 4), (3, 3)]
# bcu_esperado3 = [(0, 0), (0, 1), (1, 1), (1, 2), (2, 2), (2, 3), (2, 4), (1, 4), (1, 5), (0, 5), (0, 6)]

# # Executa o algoritmo UCS
# caminho_bcu1 = busca_custo_uniforme(grid1, pos_inicial1, pos_tesouro1)
# caminho_bcu2 = busca_custo_uniforme(grid2, pos_inicial2, pos_tesouro2)
# caminho_bcu3 = busca_custo_uniforme(grid3, pos_inicial3, pos_tesouro3)


#gulosa_esperado1 = [(0, 0), (0, 1), (1, 1), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (3, 5), (3, 6), (3, 7), (4, 7), (5, 7), (6, 7), (6, 6), (7, 6), (8, 6), (8, 7), (9, 7), (9, 8), (9, 9), (8, 9), (7, 9), (6, 9)]
#gulosa_esperado2 = [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 1), (3, 1), (4, 1), (4, 2), (4, 3), (3, 3)]
#gulosa_esperado3 = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6)]

# caminho_gulosa1 = busca_gulosa(grid1, pos_inicial1, pos_tesouro1)
# caminho_gulosa2 = busca_gulosa(grid2, pos_inicial2, pos_tesouro2)
# caminho_gulosa3 = busca_gulosa(grid3, pos_inicial3, pos_tesouro3)

caminho_a_estrela1 = [(0, 0), (0, 1), (1, 1), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (3, 5), (3, 6), (3, 7), (2, 7), (2, 8), (2, 9), (3, 9), (4, 9), (5, 9), (6, 9)]
caminho_a_estrela2 = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (1, 5), (2, 5), (3, 5), (3, 4), (3, 3)]
caminho_a_estrela3 = [(0, 0), (0, 1), (1, 1), (1, 2), (2, 2), (2, 3), (2, 4), (1, 4), (1, 5), (0, 5), (0, 6)]

estrela1 = busca_gulosa(grid1, pos_inicial1, pos_tesouro1)
estrela2 = busca_gulosa(grid2, pos_inicial2, pos_tesouro2)
estrela3 = busca_gulosa(grid3, pos_inicial3, pos_tesouro3)

print(f"Caminho correto: {caminho_a_estrela1}\n\n Resultado retornado pela funcao: {estrela1}")

print(caminho_a_estrela1 == estrela1)
# print(caminho_a_estrela2 == estrela2)
# print(caminho_a_estrela3 == estrela3)



