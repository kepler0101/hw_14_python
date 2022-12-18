from pymongo import MongoClient

client = MongoClient("localhost", 27017)

database = client["notes"]

notes = database.notes

notes_ = [

{

“username”: “Ivan”

“note”: “привет! Это объявление!”

“date”: “2022.12.11”

},

{

“username”: “Egor”

“note”: “привет! Это объявление номер 2!”

“date”: “2022.12.12”

},



]

ids = notes.insert_many(notes_).inserted_ids

print(ids)
