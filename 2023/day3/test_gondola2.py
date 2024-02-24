import unittest
import gondola2

class TestGondola(unittest.TestCase):
    
    @classmethod
    def setUpClass(self):
        file = open("2023/day3/test values.txt", "r")
        self.lines = file.readlines()
        file.close()
    
    
    def setUp(self):
        pass
    
    def test_input(self):
        self.assertEqual(gondola2.find_gear_ratio(self.lines), 467835)