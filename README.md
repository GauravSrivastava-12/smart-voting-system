# Face Recognition Voting System

A simple Django-based voting system for student elections with face-recognition-based verification. It supports voter registration, candidate management, election voting, and secure verification using face images.

> Important: This project is a demo and is not intended for a real public election without proper security review and deployment hardening.

## Features

- Student voter registration
- Candidate and election management
- Voting process
- Face-image verification support
- MySQL/MariaDB database integration
- Email OTP support

## Requirements

- Windows 10 or 11
- Python 3.10 to 3.13 (Python 3.12 recommended)
- MySQL or MariaDB
- Git

## Quick start

Follow the steps below from the project root.

### 1. Create a Python virtual environment

Open PowerShell in the repository folder and run:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
Copy-Item .env.example .env
```

If PowerShell blocks script activation, run this once in the same terminal:

```powershell
Set-ExecutionPolicy -Scope Process Bypass
```

Then activate the environment again.

### 2. Configure environment variables

Open `.env` and update the values for your local MySQL setup.

Important settings include:

- `MYSQL_HOST`
- `MYSQL_PORT`
- `MYSQL_USER`
- `MYSQL_PASSWORD`
- `MYSQL_NAME`
- `DJANGO_SECRET_KEY`
- Email values like `EMAIL_HOST`, `EMAIL_PORT`, `EMAIL_HOST_USER`, and `EMAIL_HOST_PASSWORD`

Generate a secure secret key:

```powershell
python -c "import secrets; print(secrets.token_urlsafe(50))"
```

Then paste the output into `DJANGO_SECRET_KEY` in `.env`.

> Do not commit `.env` to Git.

### 3. Create the MySQL database

Create a database named `online_voting` in MySQL/MariaDB.

You can do this with phpMyAdmin:

1. Open phpMyAdmin
2. Create a database called `online_voting`
3. Set the character set to `utf8mb4`
4. Import `online_voting.schema.sql`

Or with MySQL command line:

```cmd
mysql -u root -e "CREATE DATABASE online_voting CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;"
mysql -u root online_voting < online_voting.schema.sql
```

The schema file creates the required tables without adding sample personal voter data.

### 4. Run database setup and start the app

From the project root, run:

```powershell
Set-Location .\OnlineVoting
& "..\.venv\Scripts\python.exe" manage.py migrate
& "..\.venv\Scripts\python.exe" manage.py check
& "..\.venv\Scripts\python.exe" manage.py runserver
```

Then open:

```text
http://127.0.0.1:8000/
```

Keep the terminal open while using the app. Press `Ctrl + C` to stop the server.

## Email OTP setup

The app uses email OTP for verification. Configure the following values in `.env`:

- `EMAIL_HOST`
- `EMAIL_PORT`
- `EMAIL_HOST_USER`
- `EMAIL_HOST_PASSWORD`
- `DEFAULT_FROM_EMAIL`

For Gmail, use an app password instead of your normal login password. Enable 2-Step Verification first.

## Troubleshooting

### `ModuleNotFoundError`

Activate the virtual environment and install requirements again:

```powershell
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

### MySQL connection error

- Make sure MySQL/MariaDB is running
- Check `MYSQL_HOST`, `MYSQL_PORT`, `MYSQL_USER`, and `MYSQL_PASSWORD` in `.env`
- Make sure the database `online_voting` exists

### Database not found

Create the database and import the schema file again:

```cmd
mysql -u root -e "CREATE DATABASE online_voting CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;"
mysql -u root online_voting < online_voting.schema.sql
```

### OTP email not sending

- Verify Gmail app password setup
- Check the email settings in `.env`
- Make sure the `EMAIL_*` values are correct

## Notes

This repository intentionally excludes some local database dumps and image assets from GitHub to avoid exposing personal information or images without permission. If you want the app to show all images properly, add only images you are allowed to use.

## License

This project is provided for educational/demo use. Please check the repository for the exact licensing details if you plan to reuse or distribute it.
