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

    def tearDown(self):
        del self.auth

if __name__ == '__main__':
    unittest.main()
        