from models import *

# create some data for testing
def create_data():
    # user
    User.create(
        name="Kees",
        address="plein 44",
        location="Amsterdam",
        postal_code="1104MM",
        credit_card="01234"
    )
    User.create(
        name="Jeroen",
        address="Wallen 12",
        location="Amsterdam",
        postal_code="1105AA",
        credit_card="45678"
    )
    # tag
    Tag.create(tag="Clothes")
    Tag.create(tag="Lifestyle")
    Tag.create(tag="Books")

    # products
    Product.create(
        name="sweater",
        description="sweater",
        price=10,
        quantity=1,
        tags="Clothes"
    )
    Product.create(
        name="shoes",
        description="Shoes to walking",
        price=30,
        quantity=5,
        tags="Clothes"
    )
    Product.create(
        name="code Book",
        description="write down code book",
        price=20,
        quantity=5,
        tags="Books"
    )
    Product.create(
        name="Espresso machine",
        description="to make Espresso",
        price=50,
        quantity=3,
        tags="Lifestyle"
    )
    # product by owner
    UserProduct.create(
        owner="Kees",
        product="shoes",
        quantity=1,
        tags="Clothes"
    )
    UserProduct.create(
        owner="Jeroen",
        product="code Book",
        quantity=1,
        tags="Books"
    )





