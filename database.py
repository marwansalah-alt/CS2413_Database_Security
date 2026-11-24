"""SQLite database setup and sample records."""
import sqlite3


def create_database():
    db = sqlite3.connect(":memory:")
    db.row_factory = sqlite3.Row
    db.executescript("""
        CREATE TABLE accounts (
            id INTEGER PRIMARY KEY,
            owner TEXT NOT NULL,
            account_number TEXT NOT NULL,
            status TEXT NOT NULL
        );
        CREATE TABLE audit_log (
            id INTEGER PRIMARY KEY,
            username TEXT,
            action TEXT,
            result TEXT
        );
    """)
    db.executemany(
        "INSERT INTO accounts (owner, account_number, status) VALUES (?, ?, ?)",
        [("Zaied", "A100", "active"),
         ("Abdularhaman", "A101", "active"),
         ("Zeid", "A102", "frozen")],
    )
    db.commit()
    return db
