"""Tests for role permissions (Zeid)."""
import unittest
from access_control import allowed


class RoleTests(unittest.TestCase):
    def test_viewer_can_read(self):
        self.assertTrue(allowed("viewer", "read"))

    def test_viewer_cannot_update(self):
        self.assertFalse(allowed("viewer", "update"))

    def test_analyst_can_update(self):
        self.assertTrue(allowed("analyst", "update"))

    def test_only_admin_can_delete(self):
        self.assertTrue(allowed("admin", "delete"))
        self.assertFalse(allowed("analyst", "delete"))
