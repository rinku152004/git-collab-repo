import pymongo
#Establish a connection to the MongoDB server running on localhost at 27017
myclient = pymongo.MongoClient("mongodb://localhost:27017/") 
# database created
mydb = myclient["mydatabase"] #This is the database
mycol=mydb["Customers"]  #This is the collection
mydict={"Name":"Rinku Metaliya","Address":"Rajkot","Age":"22","Department":"AIML"}
x=mycol.insert_one(mydict)
print(mycol.find_one()) # To find and print first document in the collection & Use Find() to iterate and print every document

#Use Projection to remove _id Field :- find({},{"_id":0,"Name":1,"Age":1,"Department":1,"Address":1})
for x in mycol.find({},{"_id":0,"Name":1,"Age":1,"Department":1,"Address":1}):
  print(x)
print()

# y=json.dumps(x)
# print(y)
# z=json.loads(y)
# print(z["Name"])

print(myclient.list_database_names())

dblist = myclient.list_database_names()
if "mydatabase" in dblist:
  print("The database exists.")

print(mydb.list_collection_names())

collist = mydb.list_collection_names()
if "Customers" in collist:
  print("The collection exists.")

print(pymongo.version)
print()

# Insert Multiple Documents and unique IDs assigned by MongoDB automatically
mylist = [
  { "Name": "Annu", "Address": "Ahmedabad"},
  { "Name": "Hardavi", "Address": "Mumbai"},
  { "Name": "Mitali", "Address": "Varanasi"},
  { "Name": "Sanjana", "Address": "Jaipur"},
  { "Name": "Hetal", "Address": "Gandhinagar"},
  { "Name": "Ridhdhi", "Address": "Junagadh"},
  { "Name": "Srushti", "Address": "Surendranagar"},
  { "Name": "Vaishali", "Address": "Katchh"},
  { "Name": "Apexa", "Address": "Dwarka"},
  { "Name": "Anjali", "Address": "Porbandar"},
  { "Name": "Chandni", "Address": "Bhavnagar"},
  { "Name": "Vicky", "Address": "Botad"},
  { "Name": "Vihaa", "Address": "Amreli"},
  { "Name": "Payal", "Address": "Mahuva"}
]

x = mycol.insert_many(mylist)

#print list of the _id values of the inserted documents:
# print(x.inserted_ids)
print()

#Insert Multiple Documents, with Specified unique IDs
mylist = [
  { "_id": 1, "Name": "Jainil", "Address": "Highway 37"},
  { "_id": 2, "Name": "Aayush", "Address": "Lowstreet 27"},
  { "_id": 3, "Name": "Rahul", "Address": "Apple st 652"},
  { "_id": 4, "Name": "Honey", "Address": "Mountain 21"},
  { "_id": 5, "Name": "Mital", "Address": "Valley 345"},
  { "_id": 6, "Name": "Sandip", "Address": "Ocean blvd 2"},
  { "_id": 7, "Name": "Bhakti", "Address": "Green Grass 1"},
  { "_id": 8, "Name": "Ruhi", "Address": "Sky st 331"},
  { "_id": 9, "Name": "Susi", "Address": "One way 98"},
  { "_id": 10, "Name": "Vishal", "Address": "Yellow Garden 2"},
  { "_id": 11, "Name": "Bhavna", "Address": "Park Lane 38"},
  { "_id": 12, "Name": "Manisha", "Address": "Central st 954"},
  { "_id": 13, "Name": "Rajal", "Address": "Main Road 989"},
  { "_id": 14, "Name": "Vidhuuu", "Address": "Sideway 1633"},
  { "_id": 15, "Name": "Vinod", "Address": "Rajkot"}
]

x = mycol.insert_many(mylist)
for x in mycol.find():
  print(x)
  
#print list of the _id values of the inserted documents:
# print(x.inserted_ids)
print()

#Query to filter the result
myquery = {"Address":{"$gt":"S"}} #$lt:S-gives all address start with letter lessthan S
mydoc= mycol.find(myquery)        #$gt:S-gives all address start with letter greater and equal S
for x in mydoc:                   #$regex:^S-gives all address starts with only S
  print(x)
print()

# #SORT THE RESULT
# mydoc= mycol.find().sort("Name",-1) # Use -1 for descending order
# for x in mydoc:                     # default is 1 for ascending order
#   print(x)

# #DELETE DOCUMENT
# myquery = { "Address": "Botad" }
# y=mycol.delete_one(myquery)
# print(y.deleted_count,"Documents deleted.")
# print("Result after deletion:")
# #print the customers collection after the deletion:
# for x in mycol.find():
  # print(x)

# #DELETE MORE THAN ONE DOCS
# myquery = { "Address": {"$regex":"^S"} }
# x=mycol.delete_many(myquery)
# print(x.deleted_count,"Documents deleted.")
# print("Result after deletion:")
# #print the customers collection after the deletion:
# for x in mycol.find():
  # print(x)

# #DELETE ALL DOCS
# x=mycol.delete_many({})
# print(x.deleted_count,"Documents deleted.")
# print("Result after deletion:")
# #print the customers collection after the deletion:
# for x in mycol.find():
#   print(x)


# mycol.drop()  #DELETE THE COLLECTION
# mydb.drop_collection("Customers")  #DELETE A COLLECTION

#UPDATE COLLECTION
myquery = { "Address": "Valley 345" }
newvalues = { "$set": { "Address": "Kenya" } }
mycol.update_one(myquery, newvalues)
#print "Customers" after the update:
for x in mycol.find():
  print(x)

print()
#UPDATE MORE THAN ONE DOCS
myquery = { "Address": { "$regex": "^S" } }
newvalues = { "$set": { "Name": "Minnie" } }
x = mycol.update_many(myquery, newvalues)
print(x.modified_count, "documents updated.")
for x in mycol.find():
  print(x)

print()
#LIMIT THE RESULT
myresult = mycol.find().limit(5)
#print the result:
for x in myresult:
  print(x)