# Smart Voting System

A Django demo application for student election management, voter/candidate
registration, voting, and face-image handling.

> **Demo only:** this is a legacy student project, not election-grade software.
> Do not expose it to the internet or use it for a real election. It contains
> sample personal data and legacy authentication/query code that requires a
> security and privacy redesign before any real-world use.

## Requirements

- Windows 10/11
- Python 3.10–3.13 (Python 3.12 recommended)
- MySQL or MariaDB

The application uses two databases: Django's built-in admin/auth/session
features use the local SQLite file, while the voter, candidate, election, and
voting pages connect directly to MySQL/MariaDB.

## Windows setup

Open PowerShell in the repository root (the folder containing this README).

### 1. Create the Python environment

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
Copy-Item .env.example .env
```

If activation is blocked, run `Set-ExecutionPolicy -Scope Process
ExecutionPolicy Bypass` in that PowerShell window and activate again. Or use
`.venv\Scripts\python.exe` instead of `python` in the commands below.

The supplied `.env` defaults are for a local XAMPP-style MySQL installation.
Edit `.env` if your MySQL username, password, host, or port differs. Replace
`DJANGO_SECRET_KEY` with a private random value before sharing or deploying the
app. For example, generate one with:

```powershell
python -c "import secrets; print(secrets.token_urlsafe(50))"
```

Set the generated value as `DJANGO_SECRET_KEY` in `.env`. Never commit `.env`.

### 2. Create and import the MySQL database

Start MySQL/MariaDB (for XAMPP, click **Start** next to MySQL in the Control
Panel). Create a database named `online_voting` using the `utf8mb4` character
set, then import `online_voting.schema.sql` into it.

You can do this in phpMyAdmin:

1. Open phpMyAdmin and create `online_voting` with collation
   `utf8mb4_general_ci`.
2. Select the new database, open **Import**, choose
   `online_voting.schema.sql`, and start the import.

Alternatively, run these commands from **Command Prompt** (not PowerShell) in
the repository root:

```cmd
mysql -u root -e "CREATE DATABASE online_voting CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;"
mysql -u root online_voting < online_voting.schema.sql
```

If `mysql` is not on `PATH`, use phpMyAdmin or run the commands with the full
path to your MySQL/MariaDB `mysql.exe`.

The schema-only SQL file creates the required tables without inserting the
personal sample voter records from the original local dump. The original
`online_voting.sql`, local SQLite database, face-image folders, and bundled
photo assets are intentionally excluded from GitHub to avoid exposing personal
images or assets with unknown licenses. Some pages may therefore lack their
background/portrait images in a fresh clone. Add only images you have
permission to use; do not publish personal records or face images.

### 3. Check the database and start the site

In PowerShell, from the repository root:

```powershell
Set-Location .\OnlineVoting
& "..\.venv\Scripts\python.exe" -c "import os; os.environ.setdefault('DJANGO_SETTINGS_MODULE','OnlineVoting.settings'); import django; django.setup(); from voterapp.database import get_db_connection; c=get_db_connection(); c.close(); print('MySQL connection OK')"
& "..\.venv\Scripts\python.exe" manage.py migrate
& "..\.venv\Scripts\python.exe" manage.py check
& "..\.venv\Scripts\python.exe" manage.py runserver
```

These commands use the virtual environment directly, so activating it is
optional.
Open <http://127.0.0.1:8000/> and leave the terminal running while you use the
site. Press **Ctrl+C** to stop it.

## Email OTP configuration

OTP emails use the settings `EMAIL_HOST`, `EMAIL_PORT`, `EMAIL_HOST_USER`,
`EMAIL_HOST_PASSWORD`, and `DEFAULT_FROM_EMAIL` in `.env`. For Gmail, enable
2-Step Verification and use a Google app password; do not use your normal
account password. The old SMTP credential that was embedded in the legacy
source has been removed. If it was ever active, revoke it and generate a new
app password.

## Troubleshooting

- **`ModuleNotFoundError`**: activate `.venv` and run
  `python -m pip install -r requirements.txt`.
- **MySQL connection refused**: start the MySQL/MariaDB service and check
  `MYSQL_HOST`, `MYSQL_PORT`, and firewall settings in `.env`.
- **Access denied**: check `MYSQL_USER` and `MYSQL_PASSWORD` in `.env`.
- **Unknown database `online_voting` or missing tables**: create the database
  and import `online_voting.schema.sql`.
- **The home page loads but election pages fail**: the home page does not query
  MySQL; confirm the MySQL service is running and the SQL dump was imported.
- **OTP sending fails**: check Gmail's app password and the `EMAIL_*` values in
  `.env`.
