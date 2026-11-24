"""Simple before/after password security demonstration."""
import hashlib
import hmac
import secrets
import time

# PBKDF2 is intentionally slower than MD5. Real systems should use current
# recommended password-hashing settings and a tested authentication framework.
ITERATIONS = 600_000
MAX_FAILURES = 5
LOCK_SECONDS = 15 * 60


def weak_md5(password):
    # BEFORE: for comparison only, never for real password storage.
    return hashlib.md5(password.encode()).hexdigest()


def make_hash(password):
    salt = secrets.token_bytes(16)
    digest = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, ITERATIONS)
    return salt.hex() + ":" + digest.hex()


def check_hash(password, stored):
    try:
        salt_hex, expected_hex = stored.split(":")
        actual = hashlib.pbkdf2_hmac(
            "sha256", password.encode(), bytes.fromhex(salt_hex), ITERATIONS
        )
        return hmac.compare_digest(actual, bytes.fromhex(expected_hex))
    except (ValueError, TypeError):
        return False


class LoginSystem:
    def __init__(self):
        self.users = {}

    def add_user(self, username, password):
        self.users[username] = {
            "password_hash": make_hash(password),
            "failures": 0,
            "locked_until": 0,
        }

    def login(self, username, password, now=None):
        if now is None:
            now = time.time()
        user = self.users.get(username)
        # Same error for unknown users and wrong passwords.
        if user is None:
            return False, "Invalid username or password"
        if now < user["locked_until"]:
            return False, "Account temporarily locked"
        if check_hash(password, user["password_hash"]):
            user["failures"] = 0
            return True, "Login successful"
        user["failures"] += 1
        if user["failures"] >= MAX_FAILURES:
            user["locked_until"] = now + LOCK_SECONDS
            return False, "Account temporarily locked"
        return False, "Invalid username or password"
