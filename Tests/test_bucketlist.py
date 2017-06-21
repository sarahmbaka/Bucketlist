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

    def test_bucket_item_delete(self):
        """
        Tests for successful delete of item
        """
        response = self.auth.del_bucketitem('travel')
        self.assertEqual('Bucket item deleted', response)

    def test_bucket_item_add_existing(self):
        """
        Tests for adding existing bucket item
        """
        response = self.auth.add_bucketitem('travel', "My wish list")
        self.assertEqual('This bucket item already exists', response)

    def test_bucket_item_empty_name(self):
        """
        Tests for empty bucket item name during register
        """
        response = self.auth.add_bucketitem('', 'Daisys wish list')
        self.assertEqual('Bucket item name empty', response)

    def test_bucket_item_update(self):
        """
        Tests for editing bucket item details
        """
        response = self.auth.update_bucketitem('Travels', 'I updated my bucketlist')
        self.assertEqual('Bucket item updated', response)

    def test_bucket_item_delete_none_existant(self):
        """
        Tests for delete of buckets item that do not exist
        """
        response = self.auth.del_bucketitem('Bucket1')
        self.assertEqual('Bucket item does not exist', response)

    def tearDown(self):
        del self.auth

if __name__ == '__main__':
    unittest.main()
