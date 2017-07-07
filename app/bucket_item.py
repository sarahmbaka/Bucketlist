class BucketItem:
    """
    initializes bucket item

    """
    def __init__(self, name, description,parent_bucket, status=None):
        self.name = name
        self.description = description
        self.parent_bucket = parent_bucket
        self.status = status
