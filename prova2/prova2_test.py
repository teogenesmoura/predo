import unittest
from prova2 import FilaDeWookies
from prova2 import Wookie

class TestFilaDeWookies(unittest.TestCase):

    def test_empty_list_of_wookies(self):
        fila_de_wookies = FilaDeWookies('0', '0')
        numero_wookies = fila_de_wookies.get_numero_de_wookies()
        assert numero_wookies == 0, "Lista de wookies deve estar vazia"

    def test_create_fila_de_wookies(self):
        fila_de_wookies = FilaDeWookies('3', '4 4 1 3 5 2 6 7 8 9')
        numero_wookies = fila_de_wookies.get_numero_de_wookies()
        assert numero_wookies != 0, "Lista de wookies nao deve estar vazia"
        assert numero_wookies == 3, "Lista de wookies deve ter 3 wookies"

    def test_create_lista_de_cargas(self):
        fila_de_wookies = FilaDeWookies('3', '4 4 1 3 5 2 6 7 8 9')
        lista_de_cargas = fila_de_wookies.get_lista_cargas()
        assert len(lista_de_cargas) != 0, "Deve haver cargas na lista de cargas"
        assert isinstance(lista_de_cargas, list), "A lista de cargas deve ser uma array"

    def test_create_wookies_in_Fila_de_Wookies(self):
        fila_de_wookies = FilaDeWookies('3', '4 4 1 3 5 2 6 7 8 9')
        wookies = fila_de_wookies.get_lista_de_wookies()
        assert len(wookies) != 0, "Deve haver pelo menos um wookie na lista de wookies"
        for wookie in wookies:
            assert isinstance(wookie, Wookie), "o wookie deve ser uma instancia de Wookie"

    def test_correctly_distribute_load_among_wookies(self):
        fila_de_wookies = FilaDeWookies('3', '4 5 1 2 4 2 3 7 8 9')
        carga_por_wookie = fila_de_wookies.place_cargas_in_wookies()
        self.assertEqual(carga_por_wookie, "[[5,4,3],[4,2,2],[1]]")

if __name__ == '__main__':
    unittest.main()
