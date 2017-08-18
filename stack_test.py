import unittest
from stack import Stack

class Test_stack(unittest.TestCase):


    # def set_up(self):
    #     stack = Stack()

    def test_create(self):
        stack = Stack()
        self.assertTrue(stack.isEmpty())

    def test_push_and_top(self):
        stack = Stack()
        self.assertEqual(1, stack.top())


if __name__ == '__main__':
	unittest.main()
