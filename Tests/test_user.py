import unittest

from app.views import View


class Test_user(unittest.TestCase):
    """
    This is a class that tests ther Users functionality
    """
    def setUp(self):
        """setup"""
        self.auth = View()

    def test_register_successful_registration(self):
        """
        Tests for successful user registartion
        """
        response = self.auth.register('kerubo', '12345')
        self.assertEqual('You have successfully registered', response)

    def test_register_existing_user(self):
        """
        Tests for registering an existing user
        """
        self.auth.register('sarah', '1234')
        response = self.auth.register('sarah', '1234')
        self.assertEqual('User already registered', response)

    def test_login_invalid_credentials(self):
        """
        Tests for successful user registartion
        """
        response = self.auth.login('sarah', '123')
        self.assertEqual('Invalid Credentials', response)

    def test_register_missing_user_name(self):
        """
        Tests for missing user name
        """
        response = self.auth.register('', '1234')
        self.assertEqual('Name not provided', response)

    

    def tearDown(self):
        del self.auth

if __name__ == '__main__':
    unittest.main()
        