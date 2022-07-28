import pymongo

client = pymongo.MongoClient("mongodb+srv://nawabtaj:mongodb786@cluster0.4a4pxmc.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name" : "hasan",
    "email": "nawab@gmail.com",
    "surname": "mansuri"
}
db1 = client['mongotest1']
coll = db1['test']
coll.insert_one(d)
