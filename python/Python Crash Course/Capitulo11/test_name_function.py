import unittest
from name_function import get_formatted_name

class nameTestCase(unittest.TestCase):

    def test_first_last_name(self):
        formated_name = get_formatted_name('thales', 'diniz')
        self.assertEqual(formated_name, 'Thales Diniz')

unittest.main()