class Bucket:
    """
    initializes a bucket object

    """
    current_bucket = None
    def __init__(self, name, description, owner):
        self.name = name
        self.description = description
        self.owner = owner


