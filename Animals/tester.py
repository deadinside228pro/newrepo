import unittest
from animal import *
from volier import *

class Test_Animal_Base(unittest.TestCase):
    def setUp(self):
        self._albert = Animal('Albert1', 10, 4, 15)

    def test_add(self):
        expected = 10
        actual = self._albert.age
        self.assert_(expected, actual)

if __name__ == "__mane__":
    unittest.main()

