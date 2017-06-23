import unittest

from app import app


class TestUser(unittest.TestCase):
    """
    This is a class that tests ther Users functionality
    """
    def setUp(self):
        """setup"""
        self.app = app.test_client()

    def test_register_successful_registration(self):
        """
        Tests for successful user registration
        """
        data = dict(fname="kerubo", lname="12345")
        response = self.app.post('/register', data=data, follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_login_successful(self):
        """
        Tests for successful user registration
        """
        data1 = dict(fname="kerubo", lname="12345")
        self.app.post('/register', data=data1, follow_redirects=True)
        data = dict(user_name="kerubo", password="12345")
        response = self.app.post('/login', data=data, follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    #
    # def test_login_invalid_credentials(self):
    #     """
    #     Tests for successful user registartion
    #     """
    #     register('sarah', '1234')
    #     response = login('sarah', '123')
    #     self.assertEqual('Invalid Credentials', response)
    #

    def tearDown(self):
        del self.app

if __name__ == '__main__':
    unittest.main()
