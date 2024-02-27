import unittest
from aoc2023.day4.scratchcards2 import find_all_cards

class TestScratchcards2(unittest.TestCase):
    
    @classmethod
    def setUpClass(self):
        file = open("aoc2023/day4/test values.txt", "r")
        self.sample = file.readlines()
        file.close()
        file = open("aoc2023/day4/scratchcard input.txt", "r")
        self.puzzle = file.readlines()
        file.close()
    
    def setUp(self):
        pass
    
    
    def test_sample_input(self):
        self.assertEqual(find_all_cards(self.sample, 5), 30)

    def test_real_input(self):
        self.assertEqual(find_all_cards(self.puzzle, 10), 8477787)