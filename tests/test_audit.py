"""Tests for permission logging (Logan)."""
import unittest
from access_control import perform_action
from database import create_database


class AuditTests(unittest.TestCase):
    def setUp(self):
        self.db = create_database()

    def tearDown(self):
        self.db.close()

    def test_denied_action_is_logged(self):
        self.assertFalse(perform_action(self.db, "zeid", "viewer", "delete"))
        event = self.db.execute("SELECT result FROM audit_log").fetchone()[0]
        self.assertEqual(event, "denied")

    def test_allowed_action_is_logged(self):
        self.assertTrue(perform_action(self.db, "abdularhaman", "analyst", "update"))
        event = self.db.execute("SELECT result FROM audit_log").fetchone()[0]
        self.assertEqual(event, "allowed")

    def test_denied_update_does_not_change_data(self):
        perform_action(self.db, "zeid", "viewer", "update")
        status = self.db.execute("SELECT status FROM accounts WHERE account_number='A100'").fetchone()[0]
        self.assertEqual(status, "active")
