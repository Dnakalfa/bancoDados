import datetime
import pprint

import pymongo as pyM

client = pyM.MongoClient("mongodb+srv://<projeto:projeto>@cluster0.<numero serial>.mongodb.net/?retryWrites=true&w=majority")

db = client.test
collection = db.test_collection
print(db.test_collection)

post = {
    "author": "BETO",
    "text": "Minha primeira aplicação baseada em Python",
    "tags": ["mongodb", "python", "pymongo"],
    "date": datetime.datetime.utcnow()

}

posts = db.posts
post_id = posts.insert_one(post).inserted_id
print(post_id)

#print(db.posts.find_one())

pprint.pprint(db.posts.find_one())

new_posts = [{
    "author": "Jonas",
    "text": "Outro texto",
    "tags": ["bulk", "post", "insert"],
    "date": datetime.datetime.utcnow()
    },
    {
    "author": "Carol",
    "text": "Novo post de Carol.",
    "title": "Mongo e legal",
    "date": datetime.datetime(2009, 11, 10, 10, 45)}]

# result = post.insert_many(new_posts)
# print(result.inserted_ids)

pprint.pprint(db.posts.find_one({"author": "Carol"}))


for post in posts.find():
    pprint.pprint(post)
