import unittest
from unittest.mock import patch
from io import StringIO

from fiddup.result import FiddupHashResult, FiddupNameResult, FiddupResultBase

class ResultTest(unittest.TestCase):
    def test_base_equals(self):
        x = FiddupResultBase(base_file="file1", compared_file="file2")
        z = x
        y = FiddupResultBase(base_file="file2", compared_file="file1")
        self.assertEqual(x, y)
        self.assertEqual(x, z)




if __name__ == '__main__':
    unittest.main()