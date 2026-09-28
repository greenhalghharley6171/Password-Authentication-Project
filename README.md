# Secure Console Login & Registration System

A Python-based command-line interface (CLI) application that manages user registration and authentication using an integrated SQLite3 database. Built as a core portfolio piece to demonstrate fundamental backend logic, database management, and input validation.

## 🚀 Features
* **Secure Registration:** Validates usernames (length constraints, uniqueness checks) and enforces strict password complexity rules.
* **Authentication Engine:** Verifies credentials against records and dynamically handles failed attempts.
* **Account Lockout Security:** Protects user accounts by tracking failed attempts and implementing a local lockout state after 3 failed tries.
* **Robust Input Validation:** Implements exception handling (`try/except`) to gracefully manage unexpected user input and prevent application crashes.
* **Parameterized SQL Queries:** Prevents SQL Injection vulnerabilities by utilizing secure tokenized placeholders (`?`).

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Database Engine:** SQLite3 (Built-in)

## 📈 Future Enhancements
* Implement **Password Hashing** using the `hashlib` or `bcrypt` library to ensure credentials are never stored in plain text.
* Transition the account lockout tracking from local application memory to a persistent data column (`IsLocked`) within the SQLite table.
