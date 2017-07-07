from app import app, BucketItem, Bucket, User
from flask import render_template, request, url_for, redirect


user_list = {}
buckets_list = []
bucketsitem_list = []


@app.route('/login', methods=['GET', 'POST'])
def login():
    """"
    Method to allow registered user to log in
    """
    if request.method == 'POST':
        user_name = request.form['user_name']
        password = request.form['password']
        if password == user_list[user_name]:
            User.current_user = user_name
            return redirect(url_for('view_buckets'))
        return 'Invalid Credentials'
    elif request.method == 'GET':
        return render_template("enter.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    """"
    Method to register new users
    """
    if request.method == 'POST':
        user_name = request.form['fname']

        password = request.form['lname']
        if not user_name:
            return 'Name not provided'
        if len(password) < 1:
            return 'Password not provided'
        if user_name in user_list.keys():
            return 'User already registered'
        user_list[user_name] = password
        return redirect('/login')
    elif request.method == 'GET':
        return render_template("register.html")


@app.route('/index', methods=['GET', 'POST'])
def view_buckets():
    """"
    Method to return all buckets belonging to user after log in
    """
    if request.method == 'POST':
        return 'here'
    elif request.method == 'GET':
        view_bucket = []
        for bucket in buckets_list:
            if User.current_user == bucket.owner:
                view_bucket.append(bucket)
        return render_template('index.html', buckets=view_bucket, user=User.current_user)


@app.route('/newbucket', methods=['GET', 'POST'])
def add_bucket():
    """"
    Allows user to add a bucket on their account
    """
    if request.method == 'POST':
        name = request.form['bucketname']
        description = request.form['bucketdesc']
        if not name:
            return redirect(url_for('view_buckets'))
        for bucket in buckets_list:
            if name == bucket.name:
                return 'This bucket already exists'
        bucket = Bucket(name, description, User.current_user)
        buckets_list.append(bucket)
        return redirect(url_for('view_buckets'))


@app.route('/update_bucket/<bucket_name>', methods=['POST'])
def update_bucket(bucket_name):
    """"
    Method to update  bucket information
    """
    name = request.form['bucketname']
    description = request.form['bucketdesc']
    # parent_bucket = Bucket.current_bucket
    if request.method == 'POST':
        if len(name) < 1:
            return 'Bucket name empty'
        for bucket in buckets_list:
            if bucket_name == bucket.name:
                bucket.name = name
                bucket.description = description
                Bucket.current_bucket = name
        return redirect(url_for('view_bucketsitems', bucket_parent=Bucket.current_bucket))


@app.route('/additem', methods=['GET', 'POST'])
def add_bucketitem():
    """"
    Method to add an item to a bucket
    """
    if request.method == 'POST':
        # import pdb; pdb.set_trace()
        name = request.form['bucketname']
        description = request.form['bucketdesc']
        if len(name) < 1:
            return render_template('items.html', error_message='Bucket item name empty')

        parent_bucket = Bucket.current_bucket
        bucketsitem = BucketItem(name, description, parent_bucket)
        for bucket_item in bucketsitem_list:
            if name == bucket_item.name:
                return redirect('/bucketlist', 'This bucket item already exists'), 409
                # return 'This bucket item already exists'
        bucketsitem_list.append(bucketsitem)
        return redirect(url_for('view_bucketsitems', bucket_parent=Bucket.current_bucket))

@app.route('/bucketlist/<bucket_parent>')
def view_bucketsitems(bucket_parent):
    """"
    returns bucket list items for a specific bucket with name bucket_parent
    """
    item_list = []
    Bucket.current_bucket = bucket_parent
    for item in bucketsitem_list:
        if bucket_parent == item.parent_bucket:
            item_list.append(item)
    return render_template('items.html', bucketitem=item_list, bucket=bucket_parent), 200


@app.route('/delitem/<item_name>', methods=['GET'])
def del_bucketitem(item_name):
    """
    method to delete bucket item
    """
    print(item_name)
    for bucket_item in bucketsitem_list:
        if item_name == bucket_item.name:
            bucketsitem_list.remove(bucket_item)
            return redirect(url_for('view_bucketsitems', bucket_parent=Bucket.current_bucket))
    return 'Bucket item does not exist'


@app.route('/del_bucket/<bucketname>', methods=['GET'])
def del_bucket(bucketname):
    """
    Delete bucket from bucket list
    """
    bucket_names = [bucket.name for bucket in buckets_list]
    if bucketname not in bucket_names:
        return redirect('/index', 'Bucket does not exist'), 400
    for bucket in buckets_list:
        if bucketname == bucket.name:
            buckets_list.remove(bucket)
            return redirect(url_for('view_buckets'))


@app.route('/edit_item/<item_name>', methods=['POST'])
def update_bucketitem(item_name):
    """
    Updates bucket item
    """
    if request.method == 'POST':
        name = request.form['bucketname']
        description = request.form['bucketdesc']
        if len(name) < 1:
            return 'Bucket name empty'
        parent_bucket = Bucket.current_bucket
        for bucket_item in bucketsitem_list:
            if item_name == bucket_item.name:
                bucket_item.name = name
                bucket_item.description = description

        return redirect(url_for('view_bucketsitems', bucket_parent=parent_bucket))
