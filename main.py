__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"

from models import *
from create_data import *
from datetime import *


db.connect()
db.create_tables([User, Tag, Product, UserProduct, Transaction])

    
def search(term):
    search_term = term.lower()
    match = Product.select().where(
        (fn.lower(Product.name).contains(search_term)) | (fn.lower(Product.description).contains(search_term))
    )
    if match:
        print(f"The term {term} has been matched to:")
        for product in match:
            print(product.name)
    else:
        print('Product not found')


# View the products of a given user.
def list_user_products(user_id):
    product_list = UserProduct.select().where(UserProduct.owner == user_id)

    if product_list:
        print(f"{user_id} has:")
        for product in product_list:
            print(product.product)
    else:
        print('The owner does not exist or has no products.')


# View all products for a given tag.
def list_products_per_tag(tag_id):
    product_list = Product.select().where(Product.tags == tag_id)

    if product_list:
        print(f"These are the products tagged {tag_id}:")
        for product in product_list:
            print(product.name)
    else:
        print('The tag does not exist or has no products attached.')


# Add a product to a user.
def add_product_to_catalog(user_id, product):
    product_to_get = Product.select().where(Product.name == product)
    new_owner = User.select().where(User.name == user_id)

    if product_to_get and new_owner:
        added_product = UserProduct.create(owner=user_id,product=product,quantity=1,tags=Product.tags
        )
        print('New product added.')
        return added_product
    else:
        print('Person or product not found.')


# Remove a product from a user.
def remove_product(product_id):
    try:
        product = UserProduct.get(UserProduct.product == product_id)
        print(f"The product {product_id} has been removed.")
        return product.delete_instance()
    except DoesNotExist:
        print('Can not find product.')


# Update the stock quantity of a product.
def update_stock(product_id, new_quantity):
    product_to_change = Product.get(Product.name == product_id)

    if product_to_change:
        print(f'Old amount {product_to_change.name}: {product_to_change.quantity}')
        product_to_change.quantity = new_quantity
        product_to_change.save()
        print(f'New amount {product_to_change.name}: {product_to_change.quantity}')
    else:
        print('Can not find product')


# Handle a purchase between a buyer and a seller for a given product
def purchase_product(product_id, buyer_id, quantity):
    buyer = User.get(User.name == buyer_id)
    product_to_buy = Product.get(Product.name == product_id)
    
    if buyer and product_to_buy:
        current_date = datetime.now().date()
        get_date = datetime.strftime(current_date, '%d-%m-%Y')
        check_amount = product_to_buy.quantity - quantity
        # check if quantity exists
        if check_amount >= 0:
            
            # add a new transaction to the db
            transaction = Transaction.create(
                date=get_date,
                user=buyer_id,
                product=product_id,
                quantity=quantity
            )
            print(f"Transaction complete: {transaction.date}, {transaction.user}")

            add_product_to_catalog(buyer_id, product_id)
            list_user_products(buyer_id)
            
            if check_amount == 0:
                # delete product
                return remove_product(product_id)
            # update
            return update_stock(product_id, check_amount)    
        else:
            print('Amount not in stock.')
    else:
        print('User or product not found.')    

if __name__ == "__main__":
    pass



   
    
# <<<<<<<<<: search try out :>>>>>>>>>>

# search('sweater')
# search('Espresso machine')

# list_user_products('Kees')
# list_user_products('Jeroen')

# list_products_per_tag('Books')
# list_products_per_tag('Clothes')
    
# list_user_products('Kees')

# list_user_products('Jeroen')

# add_product_to_catalog('Kees', 'sweater')
# list_user_products('Kees')


# update_stock('code Book', 2)

# purchase_product('code Book', 'Kees', 10)
# purchase_product('Espresso machine', 'Jeroen', 1)


