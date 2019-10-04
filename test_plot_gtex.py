import unittest
import plot_gtex
import data_viz


class TestPlotGtex(unittest.TestCase):

    def test_linear_search_empty_list(self):
        key = 'cheddar'
        L = []

        r = plot_gtex.linear_search(key, L)
        self.assertEqual(r, -1)

    def test_linear_search_key_not_there(self):
        key = 'mozzarella'
        L = ['cheddar', 'brie', 'provolone', 'swiss', 'gouda']

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

    def test_binary_search_empty_list(self):
        key = 'cheddar'
        L = []

        r = plot_gtex.binary_search(key, L)
        self.assertEqual(r, -1)

    def test_binary_search_key_not_there(self):
        key = 'mozzarella'
        L = [['brie', 0], ['cheddar', 1], ['gouda', 2], ['provolone', 3]]

        r = plot_gtex.binary_search(key, L)
        self.assertEqual(r, -1)

    def test_binary_search_key_first(self):
        key = 'brie'
        L = [['brie', 0], ['cheddar', 1], ['gouda', 2], ['provolone', 3]]

        r = plot_gtex.binary_search(key, L)
        self.assertEqual(r, 0)

    def test_binary_search_key_last(self):
        key = 'provolone'
        L = [['brie', 0], ['cheddar', 1], ['gouda', 2], ['provolone', 3]]

        r = plot_gtex.binary_search(key, L)
        self.assertEqual(r, 3)

    def test_binary_search_key_mid(self):
        key = 'gouda'
        L = [['brie', 0], ['cheddar', 1], ['gouda', 2], ['provolone', 3]]

        r = plot_gtex.binary_search(key, L)
        self.assertEqual(r, 2)


if __name__ == '__main__':
    unittest.main()
