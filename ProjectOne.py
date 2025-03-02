#!/usr/bin/env python
# coding: utf-8

from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter:
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        """
        Constructor to initialize MongoDB connection.
        
        :param username: MongoDB username
        :param password: MongoDB password
        """
        # Connection Variables
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 34468
        DB = 'AAC'
        COL = 'animals'
        
        # Initialize Connection
        self.client = MongoClient(f'mongodb://{username}:{password}@{HOST}:{PORT}')
        self.database = self.client[DB]
        self.collection = self.database[COL]

    # Create method to implement the C in CRUD
    def create(self, data):
        if data is not None:
            self.collection.insert_one(data)  # data should be dictionary
        else:
            raise Exception("Nothing to save, because data parameter is empty")

    # Read method to implement the R in CRUD
    def read(self, query):
        result = self.collection.find(query)
        return list(result) if result else []  # Return an empty list if no results

    # Update method to implement the U in CRUD
    def update(self, query, data):
        try:
            self.collection.update_many(query, {'$set': data})
            return True
        except Exception as e:
            return str(e)

    # Delete method to implement the D in CRUD
    def delete(self, query):
        try:
            result = self.collection.delete_many(query)
            if result.deleted_count > 0:
                return f"{result.deleted_count} document(s) deleted"
            else:
                return "No documents found to delete"
        except Exception as e:
            return str(e)


# Now, create an instance of AnimalShelter with dynamic username and password
username = "aacuser"  # Replace with your MongoDB username
password = "SNHU1234"  # Replace with your MongoDB password

# Instantiate AnimalShelter object
crud = AnimalShelter(username, password)

# Example animal data
snake = { "animal_id": "A987147", "animal_type" : "Snake", "breed":"Cobra", "color": "Brown"}

# Create the snake entry
crud.create(snake)

# Read the snake entry
original_snake = crud.read({"animal_id": "A987147"})
print("Original snake data:")
for result in original_snake:
    print(result)

# Update the snake entry
updated_snake = {"animal_id": "A987148"}
update_query = {"animal_id": "A987147"}
crud.update(update_query, updated_snake)

# Read the updated snake entry
updated_snake_data = crud.read({"animal_id": "A987148"})
print("Updated snake data:")
for result in updated_snake_data:
    print(result)

# Delete the snake entry by breed
delete_query = {"breed": "Cobra"}
delete_result = crud.delete(delete_query)
print(delete_result)