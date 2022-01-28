__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"
from rich import print
from models import Product, ProductTag, Tag, Transaction, User

# Search for products based on a term. Searching for 'sweater' should yield all products that have the word
# 'sweater' in the name. This search should be case-insensitive.
def search(term):
    print("* search:", term)
    query = Product.select().where(Product.name.contains(term) | Product.description.contains(term))
    result = list(query.execute())
    print("result:", result)

# View the products of a given user.
def list_user_products(user_id):
    print("* list_user_products:", user_id)
    query = Product.select().where(Product.seller == user_id)
    result = list(query.execute())
    print("result:", result)

# View all products for a given tag.
def list_products_per_tag(tag_id):
    print("* list_products_per_tag:", tag_id)
    query = Product.select().join(ProductTag, on=(Product.id == ProductTag.product))\
        .join(Tag, on=Tag.id == ProductTag.tag).where(Tag.id == tag_id)
    result = list(query.execute())
    print("result:", result)


# Add a product to a user.
def add_product_to_catalog(user_id, name, description, price_in_cents, quantity):
    print("* add_product_to_catalog:", user_id, name, description, price_in_cents, quantity)
    result = Product.create(seller=user_id, name=name, description=description, price_in_cents=price_in_cents,
    quantity=quantity)
    print("result:", result)

# Update the stock quantity of a product.
def update_stock(product_id, new_quantity):
    print("* update_stock:", product_id, new_quantity)
    query = Product.update({Product.quantity: new_quantity}).where(Product.id == product_id)
    result = query.execute()
    print("result:", result)

# Handle a purchase between a buyer and a seller for a given product
def purchase_product(product_id, buyer_id, quantity):
    print("* purchase_product:", product_id, buyer_id, quantity)
    query_product = Product.select().where(Product.id == product_id)
    product = query_product.execute()[0]
    if quantity > product.quantity:
        print("Error: Not enough items in stock.")
        return False
    new_quantity = product.quantity - quantity
    current_price = product.price_in_cents
    total_price = current_price * quantity
    Product.update(quantity=new_quantity).where(Product.id == product_id).execute()
    Transaction.create(buyer=buyer_id, product_id=product_id, number_sold=quantity, selling_price_cents=current_price,
                       total_price_cents=total_price)

 # Remove a product from a user.
def remove_product(product_id):
    print("* remove_product:", product_id)
    query = Product.delete().where(Product.id == product_id)
    result = query.execute()
    print("result:", result)


def show_users():
    print("* Show users")
    query = User.select()
    result = query.execute()
    for user in result:
        print(f"{user.id}; {user.name}; {user.address}; {user.billing_information}")


def show_users_products():
    print("* Show users/products")
    query = User.select().join(Product, on=(User.id == Product.seller))
    result = query.execute()
    for user in result:
        products = []
        for product in user.products:
            products.append(product.name)
        print(f"{user.id}; {user.name}; {products}")


def show_products():
    print("* Show products")
    query = Product.select()
    result = query.execute()
    for product in result:
        print(f"{product.id}; {product.name}; {product.description}; {product.quantity}; {product.price_in_cents}")


def show_products_tags():
    print("* Show products/tags")
    query = Product.select().join(ProductTag, on=(Product.id == ProductTag.product))\
        .join(Tag, on=Tag.id == ProductTag.tag)
    result = query.execute()
    for product in result:
        tags = []
        for tag in product.tags:
            tags.append(tag.tag.name)
        print(f"{product.id}; {product.name}; {product.quantity}; {tags}")


def show_transactions():
    print("* Show transactions")
    query = Transaction.select().join(User, on=(Transaction.buyer == User.id))\
        .join(Product, on=(Transaction.product == Product.id))
    result = query.execute()
    for transaction in result:
        print(f"{transaction.id}; {transaction.buyer.name}; {transaction.product.name}; {transaction.total_price_cents}")


if __name__ == "__main__":
    # search("sweater")
    list_user_products(1)
    # list_products_per_tag(1)
    # list_products_per_tag(2)
    # add_product_to_catalog(1, "chees", "from the farm", 450, 10)
    # search("chees")
    # remove_product(8)
    # search("chees")
    # update_stock(1, 8000)
    # show_users()
    # show_products()
    # show_users_products()
    # show_products_tags()
    # show_transactions()
    # purchase_product(6, 3, 2)
    show_products()
    # show_transactions()
    pass
