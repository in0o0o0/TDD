import unittest
from validate_addr_spec import atsign_checker,split_address, find_last_at, split_domain_local
from validate_addr_spec import checker_d1,checker_d2, checker_d3, checker_d4,checker_d5
from validate_addr_spec import checker_lq1,checker_lq2,strip_double_quotation, checker_lq5, output_boolean

class Test_calc_area(unittest.TestCase):

    def test_atsign_checker(self):
        self.assertFalse(atsign_checker(['abc', 'de', '', 'example.com']))
        self.assertTrue(atsign_checker(['abc', 'de', 'f', 'example.com']))
        self.assertFalse(atsign_checker(['']))
        self.assertFalse(atsign_checker(['aaaa']))

    def test_split_address(self):
        self.assertEqual(['abc', 'de', '', 'example.com'], split_address('abc@de@@example.com', '@'))
        self.assertEqual(['abc', 'de', 'example.com'], split_address('abc@de@example.com', '@'))
        self.assertEqual(['abcexample.com'], split_address('abcexample.com', '@'))

    def test_find_last_at(self):
        self.assertEqual(6, find_last_at('abc@de@example.com'))

    def test_split_domain_local(self):
        self.assertEqual(('abc@de', 'example.com'), split_domain_local('abc@de@example.com', 6))

    def test_checker_d1(self):
        self.assertTrue(checker_d1('example.com'))
        self.assertFalse(checker_d1('example.comああ'))

    def test_checker_d2(self):
        self.assertTrue(checker_d2('example.com'))
        self.assertFalse(checker_d2('.example.com'))

    def test_checker_d3(self):
        self.assertTrue(checker_d3('example.com'))
        self.assertFalse(checker_d3('example.com.'))

    def test_checker_d4(self):
        self.assertTrue(checker_d4(['example', 'com']))
        self.assertFalse(checker_d4(['example', '', 'com']))

    def test_checker_d5(self):
        self.assertTrue(checker_d5('example'))
        self.assertFalse(checker_d5(''))
        self.assertTrue(checker_d5('a'))

    def test_checker_lq1(self):
        self.assertTrue(checker_lq1('"test'))
        self.assertFalse(checker_lq1('test'))

    def test_checker_lq2(self):
        self.assertTrue(checker_lq2('test"'))
        self.assertFalse(checker_lq2('test'))

    def test_strip_double_quotation(self):
        self.assertEqual('test',strip_double_quotation('"test"'))

    def test_checker_lg5(self):
        self.assertTrue(checker_lq5('""'))
        self.assertTrue(checker_lq5('"abc"'))
        self.assertFalse(checker_lq5('"'))

    def test_output_boolean(self):
        self.assertEqual('ok', output_boolean(True))
        self.assertEqual('ng', output_boolean(False))

class IO_mock:
    def input_data(self):
        return [10,250,100,1.5]

    def output_data(self,result):
        self.result = result

if __name__ == '__main__':
	unittest.main()
