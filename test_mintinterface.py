# test_mintinterface.py
"""
Tests for MintInterface module.
"""

import unittest
from mintinterface import MintInterface

class TestMintInterface(unittest.TestCase):
    """Test cases for MintInterface class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MintInterface()
        self.assertIsInstance(instance, MintInterface)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MintInterface()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
