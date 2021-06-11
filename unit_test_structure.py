import unittest
import cap

class TestCap(unittest.TestCase):

    def test_one_word(self):
        text = 'python'
        result = cap.cap_text(text)
            # line yang akan membandingkan apakah function di file cap itu sama dengan value unittest
        self.assertEqual(result, 'Python')
            # line ini akan melakukan pembandingnya

    def test_two_word(self):
        text = 'Yosua Audi'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Yosua Audi')

if __name__ == '__main__':          # call unit test fucntion
    unittest.main()
