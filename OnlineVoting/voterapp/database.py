import mysql.connector
from django.conf import settings


def get_db_connection():
    return mysql.connector.connect(**settings.MYSQL_DATABASE_CONFIG)
