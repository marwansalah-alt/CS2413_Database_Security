"""Run the controlled before/after database security demonstration."""
from authentication import LoginSystem, make_hash, weak_md5
from access_control import perform_action
from database import create_database
from queries import safe_search, unsafe_search


def main():
    db = create_database()
    attack = "' OR '1'='1"

    print("=== SQL injection test ===")
    print("BEFORE - rows returned:", len(unsafe_search(db, attack)))
    print("AFTER  - rows returned:", len(safe_search(db, attack)))

    print("\n=== Password test ===")
    print("BEFORE - same password gives same MD5 hash:",
          weak_md5("password123") == weak_md5("password123"))
    print("AFTER  - same password gives different salted hashes:",
          make_hash("password123") != make_hash("password123"))

    users = LoginSystem()
    users.add_user("zaied", "river-stone-cloud-2026")
    for _ in range(5):
        last = users.login("zaied", "wrong", now=1000)
    print("AFTER  - login after five wrong attempts:", last[1])
    print("AFTER  - correct password while locked:",
          users.login("zaied", "river-stone-cloud-2026", now=1001)[1])

    print("\n=== RBAC and audit test ===")
    print("Viewer update:", "allowed" if perform_action(db, "zeid", "viewer", "update") else "denied")
    print("Analyst update:", "allowed" if perform_action(db, "abdularhaman", "analyst", "update") else "denied")
    print("Viewer delete:", "allowed" if perform_action(db, "zeid", "viewer", "delete") else "denied")
    for entry in db.execute("SELECT username, action, result FROM audit_log"):
        print(f"Audit: {entry['username']} | {entry['action']} | {entry['result']}")
    db.close()


if __name__ == "__main__":
    main()
