from peewee import *
import sqlite3
connection = sqlite3.connect('betsy.db')

db = SqliteDatabase('betsy.db')


class User(Model):
    name = CharField()

    class Meta:
        database = db


class User_Address(Model):
    user = ForeignKeyField(User, backref='address')
    street = CharField()
    postal_code = CharField()
    city = CharField()

    class Meta:
        database = db


class User_Billing(Model):
    user = ForeignKeyField(User, backref='billing')
    card_type = CharField()
    card_number = IntegerField()

    class Meta:
        database = db


class Product(Model):
    owner = ForeignKeyField(User, backref='products')
    name = CharField()
    description = CharField()
    price = FloatField()
    quantity = IntegerField()

    class Meta:
        database = db


class Tag(Model):
    name = CharField()

    class Meta:
        database = db


class ProductTag(Model):
    product = ForeignKeyField(Product)
    tag = ForeignKeyField(Tag)

    class Meta:
        database = db


class Transaction(Model):
    buyer = ForeignKeyField(User, backref='transactions')
    bought_product = ForeignKeyField(Product, backref='transactions')
    quantity = IntegerField()
    total_price = FloatField()
    bought_at = DateTimeField()

    class Meta:
        database = db


def init():
    connection = db.connect()

    if connection:
        print('Connected to database.')

    with db:
        db.create_tables([User,User_Address,User_Billing,Product,Tag,ProductTag,Transaction])

        print('Created tables.')


def test_data():
    # User1 - lizzy
    lizzy = User.create(
        name='lizzy'
    )

    lizzy_address = User_Address.create(
        user=lizzy, 
        street='Hoofdweg 34', 
        postal_code='1104 MM', 
        city='Amsterdam'
    )

    lizzy_billing = User_Billing.create(
        user=lizzy, 
        card_type='Rabobank', 
        card_number=12345678
    )

    sweater = Product.create(
        owner=lizzy, 
        name='sweater', 
        description='Warm home sweater handmade by grandma Betsy',
        price=20.99,
        quantity=3
    )

    socks = Product.create(
        owner=lizzy,
        name='socks',
        description='Warm home socks handmade by grandma Betsy',
        price=8.99,
        quantity=5
    )

    hat = Product.create(
        owner=lizzy,
        name='hat',
        description='Warm home hat handmade by grandma',
        price=14.99,
        quantity=3
    )

    # User2 - kees
    kees = User.create(
        name='kees'
    )

    kees_address = User_Address.create(
        user=kees,
        street='Bijstraat 70',
        postal_code='1188 AB',
        city='Leiden'
    )

    kees_billing = User_Billing.create(
        user=kees,
        card_type='ABN Amro',
        card_number=87654321
    )

    sausages = Product.create(
        owner=kees,
        name='Sausages',
        description='Fresh sausages from the farm',
        price=1.99,
        quantity=25
    )

    steak = Product.create(
        owner=kees,
        name='Steak',
        description='Fresh steak from the farm',
        price=7.45,
        quantity=10
    )

    chicken_drums = Product.create(
        owner=kees,
        name='Chicken Drums',
        description='Fresh chicken drums from the farm',
        price=4.99,
        quantity=20
    )

    #Tags
    
    clothing= Tag.create(name='clothing')

    food = Tag.create(name='food')

   

   
    # lizzy
    
    ProductTag.create(product=sweater,tag=clothing)

    ProductTag.create(product=socks,tag=clothing)

    ProductTag.create(product=hat,tag=clothing)    

    # kees
    ProductTag.create(product=sausages,tag=food)

    ProductTag.create( product=steak,tag=food)

    ProductTag.create(product=chicken_drums,tag=food)
    
    print('Database filled with data.')