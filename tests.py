# tests.py
# Tests your dfs() and bfs() and edge_exists() work correctly
# Do not modify!

import unittest
from graph import Graph


def print_path(path):
    for i, x in enumerate(path):
        end = "" if i == len(path) - 1 else " -> "
        print(f"{x}", end=end)
    print()


class TestGraphEdgeExists(unittest.TestCase):
    def test_int_graph_edges(self):
        g1 = Graph()
        for i in range(10):
            g1.add_edge(i, i + 1)

        print("------g1------")
        print(g1)  # uses __str__

        self.assertTrue(g1.edge_exists(0, 1))
        self.assertTrue(g1.edge_exists(5, 4))
        self.assertTrue(g1.edge_exists(9, 10))
        self.assertFalse(g1.edge_exists(4, 6))
        self.assertFalse(g1.edge_exists(2, 20))
        self.assertFalse(g1.edge_exists(20, 2))

    def test_string_graph_edges(self):
        city = Graph()
        city.add_edge("Seattle", "Chicago")
        city.add_edge("Seattle", "Denver")
        city.add_edge("Seattle", "San Francisco")
        city.add_edge("San Francisco", "Denver")
        city.add_edge("San Francisco", "Los Angeles")
        city.add_edge("Los Angeles", "Denver")
        city.add_edge("Los Angeles", "Kansas City")
        city.add_edge("Los Angeles", "Dallas")
        city.add_edge("Denver", "Chicago")
        city.add_edge("Denver", "Kansas City")
        city.add_edge("Kansas City", "Chicago")
        city.add_edge("Kansas City", "New York")
        city.add_edge("Kansas City", "Atlanta")
        city.add_edge("Kansas City", "Dallas")
        city.add_edge("Chicago", "Boston")
        city.add_edge("Chicago", "New York")
        city.add_edge("Boston", "New York")
        city.add_edge("Atlanta", "New York")
        city.add_edge("Atlanta", "Dallas")
        city.add_edge("Atlanta", "Houston")
        city.add_edge("Atlanta", "Miami")
        city.add_edge("Houston", "Miami")
        city.add_edge("Houston", "Dallas")

        print("------cityGraph------")
        print(city)  # uses __str__

        self.assertTrue(city.edge_exists("Seattle", "Denver"))
        self.assertTrue(city.edge_exists("Houston", "Dallas"))
        self.assertTrue(city.edge_exists("Miami", "Atlanta"))
        self.assertFalse(city.edge_exists("Denver", "Dallas"))
        self.assertFalse(city.edge_exists("Denver", "Burlington"))
        self.assertFalse(city.edge_exists("Burlington", "New York"))


class TestGraphDFS(unittest.TestCase):
    def test_int_graph_dfs(self):
        g1 = Graph()
        for i in range(10):
            g1.add_edge(i, i + 1)

        path = g1.dfs(0, 10)
        self.assertIsNotNone(path)
        print("------dfs g1 path------")
        print_path(path)
        self.assertEqual(len(path), 11)
        self.assertEqual(path[0], 0)
        self.assertEqual(path[-1], 10)

        last = path[0]
        for current in path[1:]:
            self.assertTrue(g1.edge_exists(last, current))
            last = current

    def test_string_graph_dfs(self):
        city = Graph()
        city.add_edge("Seattle", "Chicago")
        city.add_edge("Seattle", "Denver")
        city.add_edge("Seattle", "San Francisco")
        city.add_edge("San Francisco", "Denver")
        city.add_edge("San Francisco", "Los Angeles")
        city.add_edge("Los Angeles", "Denver")
        city.add_edge("Los Angeles", "Kansas City")
        city.add_edge("Los Angeles", "Dallas")
        city.add_edge("Denver", "Chicago")
        city.add_edge("Denver", "Kansas City")
        city.add_edge("Kansas City", "Chicago")
        city.add_edge("Kansas City", "New York")
        city.add_edge("Kansas City", "Atlanta")
        city.add_edge("Kansas City", "Dallas")
        city.add_edge("Chicago", "Boston")
        city.add_edge("Chicago", "New York")
        city.add_edge("Boston", "New York")
        city.add_edge("Atlanta", "New York")
        city.add_edge("Atlanta", "Dallas")
        city.add_edge("Atlanta", "Houston")
        city.add_edge("Atlanta", "Miami")
        city.add_edge("Houston", "Miami")
        city.add_edge("Houston", "Dallas")

        path = city.dfs("Seattle", "Miami")
        self.assertIsNotNone(path)
        print("------dfs cityGraph path------")
        print_path(path)
        self.assertEqual(path[0], "Seattle")
        self.assertEqual(path[-1], "Miami")

        last = path[0]
        for current in path[1:]:
            self.assertTrue(city.edge_exists(last, current))
            last = current


class TestGraphBFS(unittest.TestCase):
    def test_int_graph_bfs(self):
        g1 = Graph()
        for i in range(10):
            g1.add_edge(i, i + 1)

        path = g1.bfs(0, 10)
        self.assertIsNotNone(path)
        print("------bfs g1 path------")
        print_path(path)
        self.assertEqual(len(path), 11)
        self.assertEqual(path[0], 0)
        self.assertEqual(path[-1], 10)

        last = path[0]
        for current in path[1:]:
            self.assertTrue(g1.edge_exists(last, current))
            last = current

    def test_string_graph_bfs(self):
        city = Graph()
        city.add_edge("Seattle", "Chicago")
        city.add_edge("Seattle", "Denver")
        city.add_edge("Seattle", "San Francisco")
        city.add_edge("San Francisco", "Denver")
        city.add_edge("San Francisco", "Los Angeles")
        city.add_edge("Los Angeles", "Denver")
        city.add_edge("Los Angeles", "Kansas City")
        city.add_edge("Los Angeles", "Dallas")
        city.add_edge("Denver", "Chicago")
        city.add_edge("Denver", "Kansas City")
        city.add_edge("Kansas City", "Chicago")
        city.add_edge("Kansas City", "New York")
        city.add_edge("Kansas City", "Atlanta")
        city.add_edge("Kansas City", "Dallas")
        city.add_edge("Chicago", "Boston")
        city.add_edge("Chicago", "New York")
        city.add_edge("Boston", "New York")
        city.add_edge("Atlanta", "New York")
        city.add_edge("Atlanta", "Dallas")
        city.add_edge("Atlanta", "Houston")
        city.add_edge("Atlanta", "Miami")
        city.add_edge("Houston", "Miami")
        city.add_edge("Houston", "Dallas")

        path = city.bfs("Seattle", "Miami")
        self.assertIsNotNone(path)
        print("------bfs cityGraph path------")
        print_path(path)
        self.assertEqual(path[0], "Seattle")
        self.assertEqual(path[-1], "Miami")
        self.assertEqual(len(path), 5)

        last = path[0]
        for current in path[1:]:
            self.assertTrue(city.edge_exists(last, current))
            last = current


if __name__ == "__main__":
    unittest.main()
