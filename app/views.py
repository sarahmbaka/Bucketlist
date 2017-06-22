from werkzeug.utils import redirect

from app.Bucketitem import Bucketitem
from app.bucket import Bucket
from app.user import User
from app import app
from flask import render_template, request, url_for

user_list = {}
buckets_list = []
bucketsitem_list = []


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_name = request.form['user_name']
        password = request.form['password']
        if password == user_list[user_name]:
            User.current_user = user_name
            print(User.current_user)
            return redirect('/index')
        return 'Invalid Credentials'
    elif request.method == 'GET':
        return render_template("enter.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user_name = request.form['fname']
        password = request.form['lname']
        user = User(user_name, password)
        if not user_name:
            return 'Name not provided'
        if len(password) < 1:
            return 'Password not provided'
        if isinstance(user_name, str):
            if user_name in user_list.keys():
                return 'User already registered'
            user_list[user_name] = password
            return redirect(url_for('login'))
    elif request.method == 'GET':
        return render_template("register.html")


@app.route('/index', methods=['GET','POST'])
def view_buckets():
    print(User.current_user)
    if request.method =='POST':
        return 'here'
    elif request.method =='GET':
        view_bucket = []
        print(User.current_user)
        for bucket in buckets_list:
            if User.current_user == bucket.owner:
                view_bucket.append(bucket)
        return render_template('index.html', buckets=view_bucket)


@app.route('/newbucket', methods=['GET', 'POST'])
def add_bucket():
    if request.method == 'POST':
        name = request.form['bucketname']
        description = request.form['bucketdesc']

        print(description)
        print(name)

        if not name:
            return 'Bucket name empty'

        for bucket in buckets_list:
            if name == bucket.name:
                print (bucket.name)
                return 'This bucket already exists'
        bucket = Bucket(name, description, User.current_user)
        buckets_list.append(bucket)
        return redirect('/index')


@app.route('/del_bucket', methods=['GET', 'POST'])
def del_bucket():
    name = request.form['bucketname']
    if request.method == 'POST':
        for bucket in buckets_list:
            if name == bucket.name:
                buckets_list.remove(bucket)
                return 'Bucket deleted'
        return 'Bucket does not exist'
    elif request.method == 'GET':
        return redirect('/index')


@app.route('/update_bucket', methods=['GET','POST'])
def update_bucket(self, name, description):
    if request.method =='POST':
        if len(name) < 1:
            return 'Bucket name empty'
        for bucket in self.buckets_list:
            if name == bucket.name:
                self.buckets_list.remove(bucket)
        bucket = Bucket(name, description)
        self.buckets_list.append(bucket)
        return 'Bucket updated'
    elif request.method=='GET':
        return redirect('/index')


@app.route('/additem',methods=['GET', 'POST'])
def add_bucketitem():

    print(Bucket.current_bucket)
    if request.method == 'POST':
        name = request.form['bucketname']
        description = request.form['bucketdesc']
        if len(name) < 1:
            return render_template('items.html', error_message='Bucket item name empty')

        parent_bucket = Bucket.current_bucket
        bucketsitem = Bucketitem(name, description,parent_bucket)
        for bucket_item in bucketsitem_list:
            if name == bucket_item.name:
                return 'This bucket item already exists'
        bucketsitem_list.append(bucketsitem)
        # return redirect('/bucketlist')
        return redirect(url_for('view_bucketsitems', bucket_parent=Bucket.current_bucket))


@app.route('/bucketlist/<bucket_parent>')
def view_bucketsitems(bucket_parent):
    item_list = []


    Bucket.current_bucket = bucket_parent
    print(Bucket.current_bucket)
    for item in bucketsitem_list:
        if bucket_parent == item.parent_bucket:
            item_list.append(item)
    return render_template('items.html', bucketitem=item_list)


@app.route('/delitem/<item_name>')
def del_bucketitem(item_name):

    for bucket_item in bucketsitem_list:
        if item_name == bucket_item.name:
            bucketsitem_list.remove(bucket_item)
            return redirect(url_for('view_bucketsitems', bucket_parent=Bucket.current_bucket))
    return 'Bucket item does not exist'


@app.route('/edit_item',methods=['POST'])
def update_bucketitem(item_name):
    if request.method == 'POST':
        name = request.form['bucketname']
        description = request.form['bucketdesc']
        if len(name) < 1:
            return 'Bucket name empty'
        for bucket_item in bucketsitem_list:
            if name == bucket_item.name:
                bucketsitem_list.remove(bucket_item)
        bucketsitem = Bucketitem(name, description)
        bucketsitem_list.append(bucketsitem)
        return redirect(url_for('view_bucketsitems', bucket_parent=Bucket.current_bucket))
