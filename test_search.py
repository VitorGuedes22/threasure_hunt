import search as src
import unittest
import mapas 

mp = mapas.mapas
class TestSearch(unittest.TestCase):
    def test_bcu(self):
        for grid,inicio,tesouro,resultado in mp.values():
            self.assertEqual(src.busca_custo_uniforme(grid,inicio,tesouro), mapas.bcu_esperado[resultado])
        
    
    def test_gulosa(self):
        for grid,inicio,tesouro,resultado in mp.values():
            self.assertEqual(src.busca_gulosa(grid,inicio,tesouro), mapas.gulosa_esperado[resultado])
    
    def test_a_estrela(self):
        for grid,inicio,tesouro,resultado in mp.values():
            self.assertEqual(src.busca_a_estrela(grid,inicio,tesouro), mapas.caminho_a_estrela[resultado])
    

if __name__ == "__main__":
    unittest.main()
