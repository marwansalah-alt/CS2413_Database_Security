"""Tests for the password and login area (Abderrahman)."""
import unittest
from unittest.mock import patch
import authentication


class AuthenticationTests(unittest.TestCase):
    def setUp(self):
        # Small iteration count keeps unit tests quick, not production behavior.
        self.patcher = patch.object(authentication, "ITERATIONS", 1000)
        self.patcher.start()
        self.addCleanup(self.patcher.stop)
        self.auth = authentication.LoginSystem()
        self.auth.add_user("zaied", "correct-horse-2026")

    def test_password_is_not_stored_as_plaintext(self):
        self.assertNotIn("correct-horse-2026", self.auth.users["zaied"]["password_hash"])

    def test_same_password_has_different_hashes(self):
        self.assertNotEqual(authentication.make_hash("hello"), authentication.make_hash("hello"))

    def test_right_and_wrong_passwords(self):
        self.assertTrue(self.auth.login("zaied", "correct-horse-2026")[0])
        self.assertFalse(self.auth.login("zaied", "wrong")[0])

    def test_account_locks_after_five_failures(self):
        for _ in range(5):
            self.auth.login("zaied", "wrong", now=100)
        self.assertFalse(self.auth.login("zaied", "correct-horse-2026", now=101)[0])

    def test_same_error_for_unknown_username(self):
        self.assertEqual(self.auth.login("missing", "wrong")[1],
                         self.auth.login("zaied", "wrong")[1])
