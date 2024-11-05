import search as sch
import view_map as vw
import graph as gp


mapa = [
    ['I', '#', '.', '#', 'L', 'L', 'T'],
    ['.', '#', '.', '#', 'L', '#', '.'],
    ['.', '#', '.', '#', 'L', '#', '.'],
    ['.', '#', '.', '.', '.', '#', '.'],
    ['.', '#', '.', '#', '.', '#', '.'],
    ['.', '#', '.', '#', '.', '#', '.'],
    ['.', '.', '.', '#', '.', '.', '.'],
]

caminho = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (6, 1), (6, 2), (5, 2), (4, 2), (3, 2), (3, 3), (3, 4), (2, 4), (1, 4), (0, 4), (0, 5), (0, 6)]

# Mostra o mapa inicial
#vw.print_mapa(mapa)

# Mostra a grid com o caminho
#vw.print_caminho(mapa, caminho)

grid = [
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
pos_inicial = (0, 0)
pos_tesouro = (6, 9)

#vw.print_mapa(grid)

# caminho_bcu = busca_custo_uniforme(grid, pos_inicial, pos_tesouro)
# caminho_gulosa = busca_gulosa(grid, pos_inicial, pos_tesouro)
# caminho_a_estrela = busca_a_estrela(grid, pos_inicial, pos_tesouro)

caminho_bcu = [(0, 0), (0, 1), (1, 1), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (3, 5), (3, 6), (3, 7), (2, 7), (2, 8), (2, 9), (3, 9), (4, 9), (5, 9), (6, 9)]
caminho_gulosa = [(0, 0), (0, 1), (1, 1), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (3, 5), (3, 6), (3, 7), (4, 7), (5, 7), (6, 7), (6, 6), (7, 6), (8, 6), (8, 7), (9, 7), (9, 8), (9, 9), (8, 9), (7, 9), (6, 9)]
caminho_a_estrela = [(0, 0), (0, 1), (1, 1), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (3, 5), (3, 6), (3, 7), (2, 7), (2, 8), (2, 9), (3, 9), (4, 9), (5, 9), (6, 9)]

vw.print_caminho(grid, caminho_bcu, "Custo uniforme")
#vw.print_caminho(grid, caminho_gulosa, "Gulosa")
#vw.print_caminho(grid, caminho_a_estrela, "A*")

grid = [
    ['I', '.', '.', '.', '.', '.'],
    ['#', '#', '.', '#', '#', '.'],
    ['.', '.', '.', '#', 'L', '.'],
    ['.', 'L', '#', 'T', '.', '.'],
    ['.', '.', '.', '.', '.', '.']
]
pos_inicial = (0, 0)
pos_tesouro = (3, 3)

# caminho_bcu = busca_custo_uniforme(grid, pos_inicial, pos_tesouro)
# caminho_gulosa = busca_gulosa(grid, pos_inicial, pos_tesouro)
# caminho_a_estrela = busca_a_estrela(grid, pos_inicial, pos_tesouro)

caminho_bcu = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (1, 5), (2, 5), (3, 5), (3, 4), (3, 3)]
caminho_gulosa = [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 1), (3, 1), (4, 1), (4, 2), (4, 3), (3, 3)]
caminho_a_estrela = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (1, 5), (2, 5), (3, 5), (3, 4), (3, 3)]

#vw.print_caminho(grid, caminho_bcu, "Custo uniforme")
#vw.print_caminho(grid, caminho_gulosa, "Gulosa")
#vw.print_caminho(grid, caminho_a_estrela, "A*")


grid = [
    ['I', '.', 'L', 'L', 'L', '.', 'T'],
    ['.', '.', '.', 'L', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.'],
]
pos_inicial = (0, 0)
tesouro = (0, 6)

# caminho_bcu = busca_custo_uniforme(grid, pos_inicial, tesouro)
# caminho_gulosa = busca_gulosa(grid, pos_inicial, tesouro)
# caminho_a_estrela = busca_a_estrela(grid, pos_inicial, tesouro)

caminho_bcu = [(0, 0), (0, 1), (1, 1), (1, 2), (2, 2), (2, 3), (2, 4), (1, 4), (1, 5), (0, 5), (0, 6)]
caminho_gulosa = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6)]
caminho_a_estrela = [(0, 0), (0, 1), (1, 1), (1, 2), (2, 2), (2, 3), (2, 4), (1, 4), (1, 5), (0, 5), (0, 6)]

#vw.print_caminho(grid, caminho_bcu, "Busca custo uniforme")
#vw.print_caminho(grid, caminho_gulosa, "Busca gulosa")
#vw.print_caminho(grid, caminho_a_estrela, "Busca A*")


