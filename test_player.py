import unittest
from player import Player


class TestPlayerMethods(unittest.TestCase):
    def test_str(self):
        player = Player(1)
        self.assertEqual(player == "Player #1")
        player = Player(2)
        self.assertEqual(player == "Player #2")

    if __name__ == '__main__':
        unittest.main()
