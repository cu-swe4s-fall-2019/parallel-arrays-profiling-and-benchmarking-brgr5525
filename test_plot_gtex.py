import unittest
import plot_gtex


class TestPlotGtex(unittest.TestCase):

    def test_linear_search_empty_list(self):
        key = 'cheddar'
        L = []

        r = plot_gtex.linear_search(key, L)
        self.assertEqual(r, -1)

    def test_linear_search_key_first(self):
        key = 'cheddar'
        L = ['cheddar', 'brie', 'provolone', 'swiss', 'gouda']

        r = plot_gtex.linear_search(key, L)
        self.assertEqual(r, 0)

    def test_linear_search_key_last(self):
        key = 'gouda'
        L = ['cheddar', 'brie', 'provolone', 'swiss', 'gouda']

        r = plot_gtex.linear_search(key, L)
        self.assertEqual(r, 4)

    def test_linear_search_key_mid(self):
        key = 'provolone'
        L = ['cheddar', 'brie', 'provolone', 'swiss', 'gouda']

        r = plot_gtex.linear_search(key, L)
        self.assertEqual(r, 2)



if __name__ == '__main__':
    unittest.main()
