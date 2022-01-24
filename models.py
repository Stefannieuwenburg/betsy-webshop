import os
from peewee import *
from main import *



db = SqliteDatabase('betsy.db', pragmas=(
    ('foreign_keys', 1), ('journal_mode', 'wall')))

class BaseModel(Model):
    class Meta:
        database = db

class user(BaseModel):
    name = CharField()

class user_address(BaseModel):
    user = ForeignKeyField(user, backref='address')
    street = CharField()
    postal_code = CharField()
    city = CharField()

class user_billing(BaseModel):
    user = ForeignKeyField(user, backref='billing')
    card_type = CharField()
    card_number = IntegerField()

class product(BaseModel):
    owner = ForeignKeyField(user, backref='products')
    name = CharField()
    description = CharField()
    price = FloatField()
    quantity = IntegerField()

    
class tag(BaseModel):
    name = CharField()

    
class product_tag(BaseModel):
    product = ForeignKeyField(product)
    tag = ForeignKeyField(tag)


class transaction(BaseModel):
    buyer = ForeignKeyField(user, backref='transactions')
    bought_product = ForeignKeyField(product, backref='transactions')
    quantity = IntegerField()
    total_price = FloatField()
    bought_at = DateTimeField()


db.connect()
print('Connected to database.')

# create a person in the database
 

def data_User():
# 1e User = lizzy
    lizzy = user.create(name="lizzy")

    lizzy_address = user_address.create(
        user=lizzy, 
        street='Hoofdweg 34', 
        postal_code='1104 MM', 
        city='Amsterdam'
    )

    lizzy_billing = user_billing.create(
        user=lizzy, 
        card_type='Rabobank', 
        card_number=12345678
    )

    sweater = product.create(
        owner=lizzy, 
        name='sweater', 
        description='Warm home sweater handmade by grandma Betsy',
        price=20.99,
        quantity=3
    )

    socks = product.create(
        owner=lizzy,
        name='socks',
        description='Warm home socks handmade by grandma Betsy',
        price=8.99,
        quantity=5
    )

    hat = product.create(
        owner=lizzy,
        name='hat',
        description='Warm home hat handmade by grandma',
        price=14.99,
        quantity=3
    )

    # 2e User = kees
    kees = user.create(name="kees")

    kees_address = user_address.create(
        user=kees,
        street='Bijstraat 70',
        postal_code='1188 AB',
        city='Leiden'
    )

    kees_billing = user_billing.create(
        user=kees,
        card_type='ABN Amro',
        card_number=87654321
    )

    sausages = product.create(
        owner=kees,
        name='Sausages',
        description='Fresh sausages from the farm',
        price=1.99,
        quantity=25
    )

    steak = product.create(
        owner=kees,
        name='Steak',
        description='Fresh steak from the farm',
        price=7.45,
        quantity=10
    )

    chicken_drums = product.create(
        owner=kees,
        name='Chicken Drums',
        description='Fresh chicken drums from the farm',
        price=4.99,
        quantity=20
    )

    #Tags
    
    clothing= tag.create(name='clothing')

    food = tag.create(name='food')


    # lizzy
    product_tag.create(product = sweater,tag=clothing)

    product_tag.create(product = socks,tag=clothing)

    product_tag.create(product = hat,tag=clothing)    

    # kees
    product_tag.create(product = sausages,tag=food)

    product_tag.create( product = steak,tag=food)

    product_tag.create(product = chicken_drums,tag=food)
    
db.create_tables([user,user_address,user_billing,product,tag,product_tag,transaction],safe = True)
print('Created tables.')
    


