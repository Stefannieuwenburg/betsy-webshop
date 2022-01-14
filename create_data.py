import os

os.remove("betsy.db")

from datetime import *
from models import *

db.connect()

# create some data for testing
def create_data():
    # user
    User.create(
        first_name="Klaas",
        last_name= "baas",
        street="plein",
        street_no = 44,
        city="Amsterdam" 
    )
    
    User.create(
        first_name="frits",
        last_name= "jansen",
        street="stadhuis",
        street_no = 20,
        city="Amsterdam"
    )

    # tags
    Tag.create(tag="Games")
    Tag.create(tag="Clothes")
    Tag.create(tag="Books")

    # products
    Product.create(
        name="doom",
        description="schooting game",
        price=40,
        quantity=3,
        tags="Games"
    )
    
    Product.create(
        name="sweater",
        description="sweater for cold weathear",
        price=10,
        quantity=1,
        tags="Clothes"
    )
    
    Product.create(
        name="schoes",
        description="Schoenen for walking",
        price=30,
        quantity=5,
        tags="Clothes"
    )
    
    Product.create(
        name="Code Book",
        description="for code ",
        price=20,
        quantity=5,
        tags="Books"
    )
    
    # product from user
    
    UserProduct.create(
        owner="Klaas",
        product="sweater",
        quantity=1,
        tags="Clothes"
    )

    UserProduct.create(
        owner="frits",
        product="Code Book",
        quantity=1,
        tags="Books"
    )






