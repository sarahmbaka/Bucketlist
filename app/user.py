class User():
    """ 
    This class initializes  a user
    
    """
    current_user=None
    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password
