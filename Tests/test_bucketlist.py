import unittest
from app.views import View

class Test_bucketitem(unittest.TestCase):
    """
    This class tests Bucket functionality
    """
    def setUp(self):
        """setup"""
        self.auth = View()

    def test_bucket_item_add(self):
        """
        Tests for successful bucket item add
        """
        response = self.auth.add_bucketitem('travel', 'My travel wish list')
        self.assertEqual('You have successfully added a bucket item', response)

    

    def tearDown(self):
        del self.auth

if __name__ == '__main__':
    unittest.main()
