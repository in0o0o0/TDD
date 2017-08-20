import unittest
from stack import Stack

class Test_stack(unittest.TestCase):

    def test_create(self):
        stack = Stack()
        self.assertTrue(stack.isEmpty())

    def test_push_and_top(self):
        stack = Stack()
        stack.push(1)
        self.assertEqual(1, stack.top())


if __name__ == '__main__':
	unittest.main()
