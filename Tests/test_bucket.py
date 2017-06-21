import unittest
from app.views import View

class Test_bucket(unittest.TestCase):
    """
    This calss tests Bucket functionality
    """
    def setUp(self):
        """setup"""
        self.auth = View()

    def test_bucket_add(self):
        """
        Tests for successful bucket add
        """
        response = self.auth.add_bucket('travel', 'My travel wish list')
        self.assertEqual('You have successfully added a bucket', response)

    def test_bucket_delete(self):
        """
        Tests for successful delete of item
        """
        response = self.auth.del_bucket('travel')
        self.assertEqual('Bucket deleted', response)

    

    def tearDown(self):
        del self.auth

if __name__ == '__main__':
    unittest.main()
