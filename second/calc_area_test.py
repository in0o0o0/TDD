import unittest
from calc_area import calc_area

class Test_calc_area(unittest.TestCase):


    # def set_up(self):
    #     stack = Stack()

    def test_calc_area(self):
        self.assertEqual(3,calc_area(1))

    '''
    def test_push_and_top(self):
        stack = Stack()
        stack.push(1)
        self.assertEqual(1, stack.top())
    '''

if __name__ == '__main__':
	unittest.main()
