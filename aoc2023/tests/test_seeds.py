import unittest
from aoc2023.day5.seeds import find_first_location

class TestSeeds(unittest.TestCase):
    
    @classmethod
    def setUpClass(self):
        with open("aoc2023/day5/test input.txt", "r") as file:
            self.sample = file.read()
        
        with open("aoc2023/day5/seed input.txt", "r") as file:
            self.puzzle = file.read()
    
    def setUp(self):
        pass
    
    def test_sample_input(self):
        self.assertEqual(find_first_location(self.sample), 35)
    
    def test_real_input(self):
        self.assertEqual(find_first_location(self.puzzle), 57075758)