from flask import Flask


app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://my_user:my_pass@mongo:27017/my_mongo_db?authSource=admin"


# This works!!! ✔️
@app.route('/test_flask_pymongo/')
def test_flask_pymongo():
    try:
        from flask_pymongo import PyMongo
        client = PyMongo(app)
        insert_return = client.db.MyCustomCollection.insert_one({"hello": "world"})
        find_result = client.db.MyCustomCollection.find_one()
        return f'{insert_return} | {find_result}'
    except Exception as e:
        return f'Exception: {e}'


# This doesn't work!!! ❌
@app.route('/test_flask_mongoengine/')
def test_flask_mongoengine():
    try:
        from flask_mongoengine import MongoEngine
        db = MongoEngine(app)
        class MyCustomCollection(db.Document):
            hello = db.StringField()
        insert_return = MyCustomCollection.objects.create(hello="world")
        find_result = MyCustomCollection.objects.first()
        return f'{insert_return} | {find_result}'
    except Exception as e:
        return f'Exception: {e}'


if __name__ == "__main__":
    app.run()
