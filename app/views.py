from app.Bucketitem import Bucketitem
from app.bucket import Bucket
from app.user import User


class View():
    """
    This is the controller
    """

    user_list = {}
    buckets_list = []
    bucketsitem_list = []
    def register(self, user_name, password):
        user = User(user_name, password)
        if len(user_name) < 1:
            return 'Name not provided'
        if len(password) < 1:
            return 'Password not provided'

        if isinstance(user_name, str):
            if user_name in self.user_list.keys():
                return 'User already registered'
            id = len(self.user_list) + 1
            self.user_list[user_name] = password
            return 'You have successfully registered'
