import unittest
from stack import Stack

class Test_stack(unittest.TestCase):
    def test_create(self):
        stack = Stack()
        self.assertTrue(stack.isEmpty())


if __name__ == '__main__':
	unittest.main()
