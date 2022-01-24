__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"


import models 
from datetime import datetime

# lees ook de help text a.u.b ik zit een beetje vast.

def search(term):
    term = term.lower()
    query = models.product.select().where(models.Product.name.contains(term) | models.Product.description.contains(term))
    if query:
        for product in query:
            print(product.name)
    else:
        print('No products matched your search term.')


def list_user_products(user_id):
    query = models.Product.select().where(models.Product.owner == user_id)

    if query:
        user = models.User.get_by_id(user_id)
        print(f"{user.name}  products:")
        for product in query:
            print(product.name)
    else:
        print('Either the user has no products or no valid id was given.')


def list_products_per_tag(tag_id):
    query = models.Product.select().join(models.Product_Tag).join(models.Tag).where(models.Tag.id == tag_id)

    if query:
        tag = models.Tag.get_by_id(tag_id)
        print(f'All products associated with {tag.name}:')
        for product in query:
            print(product.name)
    else:
        print('Either the tag has no associated products or no valid id was given.')


def add_product_to_catalog(user_id, product):
    product_to_get = product.select().where(product.name == product)
    new_owner = models.User.select().where(models.User == user_id)

    if product_to_get and new_owner:
        added_product = models.Product.create(owner=user_id, product=product, quantity=1, tags=product.tags
        )
        print('New product added.')
        return added_product
    else:
        print('Person or product not found.')


def update_stock(product_id, new_quantity):
    product = models.Product.get_by_id(product_id)
    old_stock = product.quantity
    product.quantity = new_quantity
    product.save()
    print(f'{product.name}  used to have  {old_stock}  in stock. New stock is:  {product.quantity} ')


def purchase_product(product_id, buyer_id, quantity):
    product = models.Product.get_by_id(product_id)
    buyer = models.User.get_by_id(buyer_id)
    if buyer.id == product.owner:
        print(f'You cannot buy products from yourself { buyer.name}')
        return
    if quantity >= product.quantity:
        print(f'Not enough of  { product.name} in stock.')
        return

    total_price = round(product.price * quantity, 2)
    transaction = models.Transaction.create(
        buyer = buyer.id,
        bought_product = product.id,
        quantity = quantity,
        total_price = total_price,
        bought_at = datetime.now()
    )
    
    print(f'At (transaction.bought_at)  { buyer.name}  bought (transaction.quantity) { product.name} at a total price of: € (transaction.total_price) ')

    new_quantity = product.quantity - quantity

    update_stock(product.id, new_quantity)


def remove_product(product_id):
    product = models.Product.get_by_id(product_id)
    print(f'Deleting { product.name} from the database.')
    product.delete_instance()


if __name__ == '__main__':
    pass
   
    
    
    
  