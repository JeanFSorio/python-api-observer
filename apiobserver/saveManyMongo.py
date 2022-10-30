
from pymongo import MongoClient

from apiobserver.saveMany import saveMany
def get_database():
 
   # Provide the mongodb atlas url to connect python to mongodb using pymongo
   CONNECTION_STRING = "mongodb://mongo:mjfCq9Q17i7cFKmJo1n0@containers-us-west-28.railway.app:6991/test?authSource=admin&retryWrites=true&w=majority"
 
   # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
   client = MongoClient(CONNECTION_STRING)
 
   # Create the database for our example (we will use the same database throughout the tutorial
   return client['eleicao']
  
def saveManyMongo(response):
    dbname = get_database()
    collection_name = dbname["resultados"]
    newResponse = verifyDuplicate(collection_name, response)
    if len(newResponse) > 0:
       collection_name.insert_many(newResponse)
    print(f'{len(newResponse)} dados adicionados')

def verifyDuplicate(collection, response):
   newResponse = []
   for res in response:
      if (collection.find_one(res) is None):
         newResponse.append(res)
   return newResponse
      