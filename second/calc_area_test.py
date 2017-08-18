import unittest
from calc_area import calc_area

class Test_calc_area(unittest.TestCase):


    # def set_up(self):
    #     stack = Stack()

    def test_calc_area(self):
        self.assertEqual(3, calc_area(1))
        self.assertEqual(196350, calc_area(250))
        self.assertEqual(0, calc_area(0))
        self.assertEqual(31416, calc_area(100))
        self.assertEqual(7, calc_area(1.5))
        self.assertEqual(314159265, calc_area(10000))

    '''
    def test_push_and_top(self):
        stack = Stack()
        stack.push(1)
        self.assertEqual(1, stack.top())
    '''

if __name__ == '__main__':
	unittest.main()
