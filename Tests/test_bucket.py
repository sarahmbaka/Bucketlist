import unittest

from app import app
from app.views import buckets_list


class TestBucket(unittest.TestCase):
    """
    This is a class that tests the Bucket functionality
    """
    def setUp(self):
        """
        setup
        """
        self.app = app.test_client()
        data = dict(fname="kerubo", lname="12345")
        self.app.post('/register', data=data, follow_redirects=True)
        data1 = dict(user_name="kerubo", password="12345")
        self.app.post('/login', data=data1, follow_redirects=True)

    def test_bucket_add(self):
        """
        Tests for successful bucket add
        """
        data = dict(bucketname="test", bucketdesc="test2")
        response = self.app.post('/newbucket', data=data, follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_view_bucket(self):
        """
        Tests for successful view bucket
        """
        response = self.app.post('/index', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_bucket_delete(self):
        """"
        Tests for delete bucket
        """
        data = dict(bucketname="test", bucketdesc="test2")
        self.app.post('/newbucket', data=data, follow_redirects=True)
        response = self.app.delete('/del_bucket/test', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_bucket_add_existing_bucket(self):
        """
        Tests for adding existing bucket
        """
        data = dict(bucketname="test", bucketdesc="test2")
        self.app.post('/newbucket', data=data, follow_redirects=True)
        initial_length = len(buckets_list)
        self.app.post('/newbucket', data=data, follow_redirects=True)
        new_length = len(buckets_list)
        self.assertEqual(initial_length, new_length)

    def test_bucket_empty_bucket_name(self):
        """
        Tests for empty bucket name during register
        """
        data = dict(bucketname="", bucketdesc="test2")
        response = self.app.post('/newbucket', data=data, follow_redirects=True)
        self.assertEqual(400, response.status_code)

    def test_delete_none_existent_bucket(self):
        """
        Tests for delete of buckets that do not exist
        """
        response = self.app.delete('/del_bucket/no_bucket', follow_redirects=True)
        self.assertEqual(response.status_code, 400)

    def tearDown(self):
        del self.app

if __name__ == '__main__':
    unittest.main()
