# Password Manager CLI with python

Exercise using Python with the [sqlite3](https://docs.python.org/3/library/sqlite3.html) DB-API interface for [SQLite](https://www.sqlite.org/index.html) databases.

It's a password manager CLI that creates a single user with a master password to manage passwords. User can view, show (reveal), add, edit and delete the stored passwords.

Run any of the following commands in the project's root to run the exercise.

```
python main.py
```

```
python3 main.py
```

It may be necessary to install [`python-tabulate`](https://pypi.org/project/tabulate/) via:

```
pip install tabulate
```

The file `database.db` is purged when a new user is create.

Versions used in development:

- `SQLite 3.31.1`.
- `Python 3.8.10`
- `python-tabulate 0.8.10`
