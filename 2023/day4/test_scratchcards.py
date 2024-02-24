import unittest
import scratchcards

class TestGondola(unittest.TestCase):
    
    @classmethod
    def setUpClass(self):
        file = open("2023/day4/test values.txt", "r")
        self.sample = file.readlines()
        file.close()
        file = open("2023/day4/scratchcard input.txt", "r")
        self.puzzle = file.readlines()
        file.close()
    
    def setUp(self):
        pass
    
    def test_sample_input(self):
        self.assertEqual(scratchcards.find_winning_cards(self.sample, 5), 13)
        
    def test_real_input(self):
        self.assertEqual(scratchcards.find_winning_cards(self.puzzle, 10), 17782)
