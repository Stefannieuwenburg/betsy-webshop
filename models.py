from peewee import SqliteDatabase,Model,TextField,DateField,IntegerField,ForeignKeyField,CharField,FloatField,DateTimeField

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


class Product_Tag(Model):
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



db.connect()
print('Connected to database.')

   
db.create_tables([User,User_Address,User_Billing,Product,Tag,Product_Tag,Transaction])
print('Created tables.')


        
if __name__ == '__main__':
    pass
   