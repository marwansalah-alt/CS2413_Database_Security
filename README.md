# CS2413 - Database Security Project

University of New Brunswick | Information Security | Fall 2026

We made a small Python and SQLite project to compare an insecure database system with a more secure version. All data is fake and the attack example runs locally.

## What we tested

| Problem (before) | Protection (after) |
| --- | --- |
| SQL injection returns records it should not | Parameterized SQL query |
| MD5 gives matching hashes for matching passwords | Salted PBKDF2 password hashes |
| Repeated password guesses can continue | Account lock after 5 failures |
| A viewer may try to change records | Role-based access control |
| No visible record of access decisions | SQLite audit table |

## How to run

Install Python 3.9 or newer. No extra packages are needed.

```bash
python main.py
python -m unittest discover -s tests -v
```

The first command prints the before/after demo. The second command runs all 17 tests.

## Project files

- `database.py` - creates a database with three fake accounts
- `queries.py` - vulnerable and safe search example
- `authentication.py` - password hashes and login lockout
- `access_control.py` - roles and audit logging
- `main.py` - runs the demonstration
- `tests/` - tests organized by project area
- `screenshots/` - screenshots of tests and results for the presentation

## Sample users in our tests

We used sample names from our group instead of Alice, Bob, and Carol:
`Zaied`, `Abdularhaman`, and `Zeid` are the three fake database account owners.
The login demonstration uses `zaied`. Role and audit checks use `zeid` and `abdularhaman`.
These are **test accounts only**, not real accounts or passwords.

## Team contributions

The five team members are Zaied, Abdularhaman, Zeid, Marwan, and Logan.
Fill in each person's **actual work** (coding, testing, screenshots, documentation, review)
before submission. Test filenames describe features, not authors.
One computer can push the completed project; a single Git author does not prove who made each contribution.

## Results and limitations

The tests cover a small local SQLite database, not a real website or production server. The unsafe query and MD5 function exist only for demonstrating the "before" problems. PBKDF2 uses 600,000 iterations in the demo; unit tests temporarily lower this number to run faster. The code does not include full real-world account management, network security, or deployment.

Add your captured screenshots and final report link when ready.
