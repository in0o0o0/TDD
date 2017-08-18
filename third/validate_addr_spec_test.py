import unittest
from validate_addr_spec import atsign_checker,split_address

class Test_calc_area(unittest.TestCase):


    # def set_up(self):
    #     stack = Stack()
    def test_atsign_checker(self):
        self.assertFalse(atsign_checker(['abc', 'de', '', 'example.com']))
        self.assertTrue(atsign_checker(['abc', 'de', 'f', 'example.com']))

    def test_split_address(self):
        self.assertEqual(['abc', 'de', '', 'example.com'], split_address("abc@de@@example.com"))
        self.assertEqual(['abc', 'de', 'example.com'], split_address("abc@de@example.com"))

    '''
    def test_domain_part(self):
        self.assertEqual(3, calc_area(1))
        self.assertEqual(196350, calc_area(250))
        self.assertEqual(0, calc_area(0))
        self.assertEqual(31416, calc_area(100))
        self.assertEqual(7, calc_area(1.5))
        self.assertEqual(314159265, calc_area(10000))
        self.assertTrue(isinstance(calc_area(1.5), int))

    def test_all_method(self):
        io = IO_mock()
        all_method(io)
        self.assertEqual([314,196350,31416,7],io.result)

    def test_to_float(self):
        self.assertEqual([10.0, 250.0, 100.0, 1.5], to_float(["10\n", "250\n", "100\n", "1.5\n"]))


    def test_push_and_top(self):
        stack = Stack()
        stack.push(1)
        self.assertEqual(1, stack.top())
    '''

class IO_mock:
    def input_data(self):
        return [10,250,100,1.5]

    def output_data(self,result):
        self.result = result

if __name__ == '__main__':
	unittest.main()
