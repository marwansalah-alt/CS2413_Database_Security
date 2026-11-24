"""Before and after example of SQL injection."""


def unsafe_search(db, name):
    # BEFORE: for our controlled demo ONLY. Never use this with real data.
    sql = f"SELECT * FROM accounts WHERE owner = '{name}'"
    return db.execute(sql).fetchall()


def safe_search(db, name):
    # AFTER: a ? placeholder keeps user input separate from SQL.
    return db.execute("SELECT * FROM accounts WHERE owner = ?", (name,)).fetchall()
