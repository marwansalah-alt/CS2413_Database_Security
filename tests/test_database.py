"""Tests for the database setup area (Ziad)."""
import unittest
from database import create_database


class DatabaseTests(unittest.TestCase):
    def setUp(self):
        self.db = create_database()

    def tearDown(self):
        self.db.close()

    def test_sample_accounts_exist(self):
        count = self.db.execute("SELECT COUNT(*) FROM accounts").fetchone()[0]
        self.assertEqual(count, 3)

    def test_audit_table_exists(self):
        self.db.execute("SELECT * FROM audit_log")
