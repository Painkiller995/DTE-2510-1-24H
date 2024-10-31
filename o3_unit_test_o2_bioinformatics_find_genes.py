"""
This module represents implementation of unit tests for the bioinformatics module.

This implementation could be improved in the feature please check github for the latest version.
https://github.com/Painkiller995/DTE-2510-1-24H

The o2_bioinformatics_find_genes.py available at:
https://github.com/Painkiller995/DTE-2510-1-24H/blob/main/o2_bioinformatics_find_genes.py

"""

import unittest

from o2_bioinformatics_find_genes import find_genes


class TestGenome(unittest.TestCase):
    """
    Test the genome module.
    """

    def test_empty_string(self):
        """
        Test an empty string.
        """
        result = find_genes("")
        self.assertEqual("No genes found!", result)

    def test_rubbish_string(self):
        """
        Test a string with no genes.
        """
        result = find_genes("I AM A STRING WITH NO GENES WHATSOEVER")
        self.assertEqual("No genes found!", result)

    def test_valid_genome(self):
        """
        Test a valid genome.
        """
        result = find_genes("ATGTTTCTGTAG")
        self.assertIn("TTTCTG", result)

    def test_no_gene(self):
        """
        Test a genome with no genes.
        """
        result = find_genes("ATGATGATGTGA")
        self.assertEqual("No genes found!", result)

    def test_single_valid_gene(self):
        """
        Test a genome with a single valid gene.
        """
        result = find_genes("ATGCGTTAA")
        self.assertIn("CGT", result)


if __name__ == "__main__":
    unittest.main()
