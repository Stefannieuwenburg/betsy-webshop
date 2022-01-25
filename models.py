# Models go here

import peewee
import datetime
import os

database_file = "betsy.db"
db = peewee.SqliteDatabase(database_file)


class BaseTable(peewee.Model):
    class Meta:
        database = db


class User(BaseTable):
    name = peewee.TextField(null=False)
    address = peewee.TextField(null=False)
    billing_information = peewee.TextField(null=False)


class Tag(BaseTable):
    name = peewee.TextField(null=False, unique=True)


class Product(BaseTable):
    seller = peewee.ForeignKeyField(User, null=False, backref="products")
    name = peewee.TextField(null=False, index=True)
    description = peewee.TextField(null=False, index=True)
    price_in_cents = peewee.IntegerField(null=False)
    quantity = peewee.IntegerField(null=False, default=1)
    date_created = peewee.DateTimeField(null=False, default=datetime.datetime.now())


class Transaction(BaseTable):
    buyer = peewee.ForeignKeyField(User, null=False)
    product = peewee.ForeignKeyField(Product, null=False)
    number_sold = peewee.IntegerField(null=False, default=1)
    datetime = peewee.DateTimeField(null=False, default=datetime.datetime.now())
    selling_price_cents = peewee.IntegerField(null=False)
    total_price_cents = peewee.IntegerField(null=False)


class ProductTag(BaseTable):
    product = peewee.ForeignKeyField(Product, backref="tags")
    tag = peewee.ForeignKeyField(Tag, backref="tags")


def make_db():
    db.connect()
    db.create_tables([User, Tag, Product, Transaction, ProductTag])


def reset_db():
    if os.path.isfile(database_file):
        os.remove(database_file)
    make_db()


def fill_db():
    User.create(name="Kees", address="Bijlmer, Amsterdam", billing_information="ING 123")
    User.create(name="Miep", address="Schilderswijk, Den Haag", billing_information="ABN 456")
    User.create(name="Bep", address="Kanaleneiland, Utrecht", billing_information="Contant")
    User.create(name="Alex", address="ten Bosch, Den Haag", billing_information="nvt")
    Tag.create(name="food")
    Tag.create(name="clothing")
    Product.create(seller=1,  name="cake", description="from the baker.", price_in_cents=300, quantity=5)
    Product.create(seller=1,  name="chees", description="from the cow.", price_in_cents=500, quantity=10)
    Product.create(seller=1,  name="ei", description="from chicken.", price_in_cents=400, quantity=12)
    Product.create(seller=2,  name="pants", description="cloting for the body.", price_in_cents=5000,
                   quantity=100)
    
    Product.create(seller=2,  name="sweater", description="clothing for the body.", price_in_cents=6000,
                   quantity=100)
    Product.create(seller=4,  name="underwear", description="clothing for the body", price_in_cents=2500,
                   quantity=100)
    ProductTag.create(product=1, tag=1)
    ProductTag.create(product=2, tag=1)
    ProductTag.create(product=3, tag=1)
    ProductTag.create(product=4, tag=2)
    ProductTag.create(product=5, tag=2)
    ProductTag.create(product=6, tag=2)
    ProductTag.create(product=7, tag=1)
    ProductTag.create(product=7, tag=2)


if __name__ == "__main__":
    make_db()
    fill_db()
