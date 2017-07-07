from flask import Flask
from app.bucket_item import BucketItem
from app.bucket import Bucket
from app.user import User

# Initialize the app
app = Flask(__name__, instance_relative_config=True)

# Load the views
from app import views

app.config.from_object('config')
