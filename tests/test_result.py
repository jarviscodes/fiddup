import unittest
from fiddup.result import FiddupHashResult, FiddupNameResult, FiddupResultBase


class ResultBaseTest(unittest.TestCase):
    def test_base_equals(self):
        x = FiddupResultBase(base_file="file1", compared_file="file2")
        z = x
        y = FiddupResultBase(base_file="file2", compared_file="file1")
        self.assertEqual(x, y)
        self.assertEqual(x, z)

    def test_base_not_equals(self):
        x = FiddupResultBase(base_file="file1", compared_file="file2")
        y = FiddupResultBase(base_file="file3", compared_file="file4")

        self.assertNotEqual(x, y)


class NameResultTest(unittest.TestCase):
    compare_row = ["file1", "file2", 0.5]

    def test_terminaltable_row(self):
        """Check if the row data get's parsed as expected"""
        x = FiddupNameResult(
            base_file="file1", compared_file="file2", similarity=0.5
        )
        row = x.as_terminaltable_row()
        self.assertListEqual(row, self.compare_row)

    def test_name_equals(self):
        """Check if the base eq operator is called correctly"""
        x = FiddupNameResult(
            base_file="file1", compared_file="file2", similarity=0.5
        )
        y = FiddupNameResult(
            base_file="file2", compared_file="file1", similarity=0.5
        )
        self.assertEqual(x, y)


class HashResultTest(unittest.TestCase):
    compare_row = ["file1", "file2",
                   "aabbccddeeffaabbccddeeffaabbccddeeff", 100]

    def test_terminaltable_row(self):
        """Check if the row data get's parsed as expected"""
        x = FiddupHashResult(
            base_file="file1",
            compared_file="file2",
            file_hash="aabbccddeeffaabbccddeeffaabbccddeeff",
            base_size=100,
            compared_size=100,
        )
        row = x.as_terminaltable_row()
        self.assertListEqual(row, self.compare_row)


if __name__ == "__main__":
    unittest.main()
