import heapq

def heuristica_manhattan(posicao_atual, tesouro):
    """Calcula a heurística de Manhattan entre a posição atual e o tesouro."""
    return abs(posicao_atual[0] - tesouro[0]) + abs(posicao_atual[1] - tesouro[1])


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
    # Fila de prioridade: (f(n), posição, custo atual, caminho percorrido)
    fila = [(heuristica_manhattan(inicio, tesouro), inicio, 0, [inicio])]

    while fila:
        # Retira o nó com o menor custo total estimado (f(n) = g(n) + h(n))
        _, (linha, coluna), custo_atual, caminho = heapq.heappop(fila)

        # Se encontramos o tesouro, retorna o caminho
        if (linha, coluna) == tesouro:
            return caminho

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
                heuristica = heuristica_manhattan((nova_linha, nova_coluna), tesouro)
                custo_total_estimado = novo_custo + heuristica
                novo_caminho = caminho + [(nova_linha, nova_coluna)]

                # Adiciona a nova posição à fila com o custo total estimado
                heapq.heappush(fila, (custo_total_estimado, (nova_linha, nova_coluna), novo_custo, novo_caminho))

    # Retorna um array vazio se não houver caminho possível
    return []
