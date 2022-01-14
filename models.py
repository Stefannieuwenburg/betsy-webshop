# Models go here


from peewee import *

db = SqliteDatabase('betsy.db',pragmas={"foreign_keys": 1})



class BaseModel():
    class Meta:
        database = db


class User(BaseModel):
    first_name = CharField()
    last_name = CharField()
    street = CharField()
    street_no = IntegerField()
    city = CharField()
    


class Tag(BaseModel):
    name = CharField()


class Catalog(BaseModel):
    catalog_id = AutoField()
    user_id = ForeignKeyField(User)


class Product(BaseModel):
    product = CharField()
    description = CharField()
    tags = ManyToManyField(Tag)
    price = DecimalField()
    quantity = IntegerField()


class UserProduct(BaseModel):
    user_id = ForeignKeyField(User)
    product_id = ForeignKeyField(Product)
    number = IntegerField()


class Transaction(BaseModel):
    user_id = ForeignKeyField(User)
    product_id = ForeignKeyField(Product)
    quantity = IntegerField(constraints=[Check("quantity >= 0")])
    sell_date = DateField()
    sell_price = DecimalField()


ProductTag = Product.tags.get_through_model()


def create_tables():
    with db:
        db.create_tables(
            [User, Product, Tag, UserProduct, ProductTag, Transaction, Catalog]
        )


if __name__ == "__main__":
    create_tables()

