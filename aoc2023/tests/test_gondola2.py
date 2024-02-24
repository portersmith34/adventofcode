import unittest
from  aoc2023.day3.gondola2 import find_gear_ratio


class TestGondola2(unittest.TestCase):
    
    @classmethod
    def setUpClass(self):
        file = open("aoc2023/day3/test values.txt", "r")
        self.lines = file.readlines()
        file.close()
    
    
    def setUp(self):
        pass
    
    def test_input(self):
        self.assertEqual(find_gear_ratio(self.lines), 467835)