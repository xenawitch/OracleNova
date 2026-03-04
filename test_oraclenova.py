# test_oraclenova.py
"""
Tests for OracleNova module.
"""

import unittest
from oraclenova import OracleNova

class TestOracleNova(unittest.TestCase):
    """Test cases for OracleNova class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = OracleNova()
        self.assertIsInstance(instance, OracleNova)
        
    def test_run_method(self):
        """Test the run method."""
        instance = OracleNova()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
