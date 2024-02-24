import unittest
import gondola

class TestGondola(unittest.TestCase):
    file = open("2023/day3/test values.txt", "r")
    lines = file.readlines()
    file.close()
    
    def test_input(self):
        sum = gondola.find_part_numbers(self.lines)
        self.assertEqual(sum, 4361)


if __name__ == "__main__":
    unittest.main()