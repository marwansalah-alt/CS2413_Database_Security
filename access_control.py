"""Role-based access control and a small audit log."""

ROLES = {
    "viewer": {"read"},
    "analyst": {"read", "update"},
    "admin": {"read", "update", "delete"},
}


def allowed(role, action):
    return action in ROLES.get(role, set())


def perform_action(db, username, role, action, account="A100"):
    permission = allowed(role, action)
    if permission and action == "update":
        db.execute("UPDATE accounts SET status = ? WHERE account_number = ?",
                   ("frozen", account))
    elif permission and action == "delete":
        db.execute("DELETE FROM accounts WHERE account_number = ?", (account,))
    db.execute("INSERT INTO audit_log (username, action, result) VALUES (?, ?, ?)",
               (username, action, "allowed" if permission else "denied"))
    db.commit()
    return permission
