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

    def test_bucket_add_existing_bucket(self):
        """
        Tests for adding existing bucket
        """
        response = self.auth.add_bucket('travel', "My wish list")
        self.assertEqual('This bucket already exists', response)

    def test_bucket_empty_bucket_name(self):
        """
        Tests for empty bucket name during register
        """
        response = self.auth.add_bucket('', 'Daisys wish list')
        self.assertEqual('Bucket name empty', response)

    def test_bucket_update(self):
        """
        Tests for editing bucket details
        """
        response = self.auth.update_bucket('Travels', 'I updated my bucketlist')
        self.assertEqual('Bucket updated', response)

    

    def tearDown(self):
        del self.auth

if __name__ == '__main__':
    unittest.main()
