import unittest
import gondola

class TestGondola(unittest.TestCase):
    
    @classmethod
    def setUpClass(self):
        file = open("2023/day3/test values.txt", "r")
        self.lines = file.readlines()
        file.close()
    
    
    def setUp(self):
        pass
    
    def test_input(self):
        sum = gondola.find_part_numbers(self.lines)
        self.assertEqual(sum, 4361)