import pprint

import pymongo as pyM

client = pyM.MongoClient("mongodb+srv://<projeto:projeto>@cluster0.<numero serial>.mongodb.net/?retryWrites=true&w=majority")

db = client.test
posts = db.post

for post in posts.find():
    pprint.pprint(post)

print(posts.count_documents({}))

for post in posts.find({}).sort("date"):
    pprint.pprint(post)

