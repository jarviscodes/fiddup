import unittest
from unittest.mock import patch
from io import StringIO

from fiddup.views import (
    prepare_hash_table_header,
    prepare_name_table_header,
    refine_inputs,
    get_name_table_data,
)


class TestTableHeaders(unittest.TestCase):
    def test_name_table(self):
        table_header = prepare_name_table_header()
        self.assertIsInstance(
            table_header, list, "Table header must be list of columns."
        )
        table_header_length = len(table_header)
        table_header_columns = len(table_header[0])
        self.assertEqual(table_header_length, 1, "Need exactly 1 header row.")
        self.assertEqual(
            table_header_columns, 3, "Need exactly 3 header columns."
        )

    def test_hash_table(self):
        table_header = prepare_hash_table_header()
        self.assertIsInstance(
            table_header, list, "Table header must be list of columns."
        )
        table_header_length = len(table_header)
        table_header_columns = len(table_header[0])
        self.assertEqual(table_header_length, 1, "Need exactly 1 header row.")
        self.assertEqual(
            table_header_columns, 4, "Need exactly 4 header columns."
        )


class TestTableData(unittest.TestCase):
    table_data = [[1, 2, 3], ["a", "b", "c"]]

    justify_dict = {0: "left", 1: "left", 2: "right"}

    def test_get_table_data(self):
        table = get_name_table_data(table_data=self.table_data)
        self.assertTrue("Results" in table.title)
        self.assertFalse(table.inner_heading_row_border)
        self.assertDictEqual(table.justify_columns, self.justify_dict)
        self.assertEqual(table.table_data[0][0], 1)
        self.assertEqual(table.table_data[0][1], 2)
        self.assertEqual(table.table_data[0][2], 3)
        self.assertEqual(table.table_data[1][0], "a")
        self.assertEqual(table.table_data[1][1], "b")
        self.assertEqual(table.table_data[1][2], "c")


class TestInputs(unittest.TestCase):

    extensions_dirty = [".mp4", ".mp3", "wma", "..txt"]
    extensions_clean = ["mp4", "mp3", "wma", "txt"]

    def test_refine_extensions(self):
        (
            verbose,
            extensions,
            directory,
            in_path,
            threshold,
            chunk_count,
        ) = refine_inputs(
            verbose=False,
            extensions=self.extensions_dirty,
            directory=False,
            in_path="",
            threshold=0.5,
            chunk_count=5,
        )
        self.assertListEqual(extensions, self.extensions_clean)

    def test_out_of_range_threshold(self):
        with patch("sys.stdout", new=StringIO()) as fakeOutput:
            with self.assertRaises(SystemExit):
                refine_inputs(
                    verbose=False,
                    extensions=self.extensions_dirty,
                    directory=False,
                    threshold=1.8,
                    chunk_count=5,
                )
            self.assertTrue(
                "Please specify a value" in fakeOutput.getvalue().strip()
            )


if __name__ == "__main__":
    unittest.main()
