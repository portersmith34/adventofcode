import unittest
from aoc2023.day5.seeds import find_first_location

class TestScratchcards2(unittest.TestCase):
    
    @classmethod
    def setUpClass(self):
        file = open("aoc2023/day5/test input.txt", "r")
        self.sample = file.readlines()
        file.close()
        file = open("aoc2023/day5/seed input.txt", "r")
        self.puzzle = file.readlines()
        file.close()
    
    def setUp(self):
        pass
    
    
    def test_sample_input(self):
        self.assertEqual(find_first_location(self.sample), 35)


    # def test_real_input(self):
    #     self.assertEqual(find_first_location(self.puzzle), 0)