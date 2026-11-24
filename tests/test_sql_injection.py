"""Tests for the before/after SQL injection example (Marwan)."""
import unittest
from database import create_database
from queries import unsafe_search, safe_search


class SQLInjectionTests(unittest.TestCase):
    def setUp(self):
        self.db = create_database()

    def tearDown(self):
        self.db.close()

    def test_normal_search(self):
        self.assertEqual(len(safe_search(self.db, "Zaied")), 1)

    def test_before_attack_returns_every_account(self):
        attack = "' OR '1'='1"
        self.assertEqual(len(unsafe_search(self.db, attack)), 3)

    def test_after_attack_returns_no_accounts(self):
        attack = "' OR '1'='1"
        self.assertEqual(len(safe_search(self.db, attack)), 0)
