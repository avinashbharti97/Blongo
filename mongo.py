import pymongo

#open the mongodb connection
conn = pymongo.MongoClient('mongodb://localhost:27017')

#print the available database
databases = conn.database_names()
for database in databases:
	print(database)
#close the MongoDB connection
conn.close()