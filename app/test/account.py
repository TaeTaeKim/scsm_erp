import unittest
from app.database.mysql import get_db
from app.service.account_service import AccountService
class TestAccount(unittest.TestCase):
    account_service = AccountService()