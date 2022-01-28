# Models go here
from rich import print
from peewee import (
CharField,DecimalField,ForeignKeyField, IntegerField, Model,
SqliteDatabase, DateField,TextField,DateTimeField,FixedCharField,
DateField,TimeField,TimestampField,BareField
)
import datetime
import os


db = SqliteDatabase("betsy.db")


class BaseTable(Model):
    class Meta:
        database = db


class User(BaseTable):
    name = TextField(null=False)
    address = TextField(null=False)
    billing_information = TextField(null=False)


class Tag(BaseTable):
    name = TextField(null=False, unique=True)


class Product(BaseTable):
    seller = ForeignKeyField(User, null=False, backref="products")
    name = TextField(null=False, index=True)
    description = TextField(null=False, index=True)
    price_in_cents = IntegerField(null=False)
    quantity = IntegerField(null=False, default=1)
    date_created = DateTimeField(null=False, default=datetime.datetime.now())


class Transaction(BaseTable):
    buyer = ForeignKeyField(User, null=False)
    product = ForeignKeyField(Product, null=False)
    number_sold = IntegerField(null=False, default=1)
    datetime = DateTimeField(null=False, default=datetime.datetime.now())
    selling_price_cents = IntegerField(null=False)
    total_price_cents = IntegerField(null=False)


class ProductTag(BaseTable):
    product = ForeignKeyField(Product, backref="tags")
    tag = ForeignKeyField(Tag, backref="tags")


def make_db():
    db.connect()
    print("Connect to database")
    db.create_tables([User, Tag, Product, Transaction, ProductTag])
    print("create tables")

def reset_db():
    if os.path.isfile("betsy.db"):
        os.remove("betsy.db")
        print("remove db betsy")
   


def fill_db():
    User.create(name="Kees",address="Bijlmer, Amsterdam", billing_information="ING 123")
    User.create(name="Miep",address="Schilderswijk, Den Haag", billing_information="ABN 456")
    User.create(name="Bep",address="Kanaleneiland, Utrecht", billing_information="Contant")
    User.create(name="Alex",address="ten Bosch, Den Haag", billing_information="nvt")
    Tag.create(name="food")
    Tag.create(name="clothing")
    Product.create(seller=1,name="cake", description="from the baker.", price_in_cents=300, quantity=5)
    Product.create(seller=1,name="chees", description="from the cow.", price_in_cents=500, quantity=10)
    Product.create(seller=1,name="ei", description="from chicken.", price_in_cents=400, quantity=12)
    Product.create(seller=2,name="pants", description="cloting for the body.", price_in_cents=5000,quantity=100)
    Product.create(seller=2,name="sweater", description="clothing for the body.", price_in_cents=6000, quantity=100)
    Product.create(seller=4,name="underwear", description="clothing for the body", price_in_cents=2500,quantity=100)
    ProductTag.create(product=1,tag=1)
    ProductTag.create(product=2,tag=1)
    ProductTag.create(product=3,tag=1)
    ProductTag.create(product=4,tag=2)
    ProductTag.create(product=5,tag=2)
    ProductTag.create(product=6,tag=2)
    ProductTag.create(product=7,tag=1)
    ProductTag.create(product=7,tag=2)
    print('db fill whit data')


if __name__ == "__main__":
    make_db()
    fill_db()
