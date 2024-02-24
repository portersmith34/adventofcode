import unittest
from  aoc2023.day3.gondola import find_part_numbers

class TestGondola(unittest.TestCase):
    
    @classmethod
    def setUpClass(self):
        file = open("aoc2023/day3/test values.txt", "r")
        self.lines = file.readlines()
        file.close()
    
    
    def setUp(self):
        pass
    
    def test_input(self):
        sum = find_part_numbers(self.lines)
        self.assertEqual(sum, 4361)