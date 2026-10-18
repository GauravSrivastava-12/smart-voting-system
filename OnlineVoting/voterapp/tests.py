from unittest.mock import patch

from django.conf import settings
from django.test import SimpleTestCase, TestCase

from . import database


class DatabaseConnectionTests(SimpleTestCase):
    @patch("voterapp.database.mysql.connector.connect")
    def test_connection_uses_configured_mysql_settings(self, connect):
        database.get_db_connection()

        connect.assert_called_once_with(**settings.MYSQL_DATABASE_CONFIG)


class HomePageTests(TestCase):
    def test_home_page_loads_without_mysql(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
