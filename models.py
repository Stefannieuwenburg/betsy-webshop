# Models go here


from peewee import *

db = SqliteDatabase('betsy.db')




# def create_tables():
#     with database:
#         database.create_tables([User, Relationship, Message])
        
# create a person in the database
# Person.create(name="Jimmy", birthday="01-01-1980") 

# retrieve a single person by name
# jimmy = Person.get(Person.name == "Jimmy")

# update a person in the database
# jimmy.name = "James"
# jimmy.save()

# delete a person
# jimmy.delete_instance()