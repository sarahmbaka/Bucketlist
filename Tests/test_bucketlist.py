import unittest

from app import app



class Test_bucket(unittest.TestCase):
    """
    This is a class that tests ther Bucket functionality
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
        data = dict(bucketname="test", bucketdesc="test2")
        self.app.post('/newbucket', data=data, follow_redirects=True)

    def test_item_bucket_delete(self):
        """"
        Tests for delete item in  bucket
        """
        data = dict(bucketname="test", bucketdesc="test2")
        self.app.post('/additem/test', data=data, follow_redirects=True)
        response = self.app.get('/delitem/test', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_add_item(self):
        """"
        Tests for add item bucket
        """
        data = dict(bucketname="test2", bucketdesc="test2")
        self.app.post('/additem/test', data=data, follow_redirects=True)
        self.app.get('/bucketlist/test', follow_redirects=True)
        data = dict(bucketname="test", bucketdesc="test2")
        response = self.app.post('/additem', data=data, follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_bucket_item_add_existing(self):
        """
        Tests for adding existing bucket item
        """
        data = dict(bucketname="test2", bucketdesc="test2")
        self.app.post('/additem/test', data=data, follow_redirects=True)
        self.app.get('/bucketlist/test', follow_redirects=True)
        data = dict(bucketname="test", bucketdesc="test2")
        self.app.post('/additem', data=data, follow_redirects=True)
        response = self.app.post('/additem', data=data, follow_redirects=True)
        self.assertEqual(response.status_code, 409)

    # def test_bucket_item_delete_none_existant(self):
    #     """
    #     Tests for delete of buckets item that do not exist
    #     """
    #     response = self.auth.del_bucketitem('Bucket1')
    #     self.assertEqual('Bucket item does not exist', response)

    def tearDown(self):
        del self.app

if __name__ == '__main__':
    unittest.main()
