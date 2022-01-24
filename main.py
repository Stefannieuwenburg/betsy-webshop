__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"


import models 
from datetime import datetime


def search(term):
    term = term.lower()
    query = models.product.select().where(models.product.name.contains(term) | models.product.description.contains(term))

    if query:
        for product in query:
            print(product.name)
    else:
        print('No products matched your search term.')


def list_user_products(user_id):
    query = models.product.select().where(models.product.owner == user_id)

    if query:
        user = models.User.get_by_id(user_id)
        print(user.name + "'s products:")
        for product in query:
            print(product.name)
    else:
        print('Either the user has no products or no valid id was given.')


def list_products_per_tag(tag_id):
    query = models.product.select().join(models.product_tag).join(models.Tag).where(models.tag.id == tag_id)

    if query:
        tag = models.tag.get_by_id(tag_id)

        print('All products associated with ' + tag.name + ':')

        for product in query:
            print(product.name)
    else:
        print('Either the tag has no associated products or no valid id was given.')

# nog na kijken 
def add_product_to_catalog(user_id, product):
    user = models.user.get_by_id(user_id)
    product.owner = user
    product.save()
    print(product.name + ' with the id of ' + (product.id) + ' owned by ' + user.name + ' was stored in the database.')


def update_stock(product_id, new_quantity):
    product = models.product.get_by_id(product_id)
    old_stock = product.quantity
    product.quantity = new_quantity
    product.save()
    print(product.name + ' used to have ' + (old_stock) + ' in stock. New stock is: ' + (product.quantity) + '.')


def purchase_product(product_id, buyer_id, quantity):
    product = models.Product.get_by_id(product_id)
    buyer = models.User.get_by_id(buyer_id)

    if buyer.id == product.owner:
        print('You cannot buy products from yourself ' + buyer.name + '.')
        return

    if quantity >= product.quantity:
        print('Not enough of ' + product.name + ' in stock.')
        return

    total_price = round(product.price * quantity, 2)

    transaction = models.Transaction.create(
        buyer = buyer.id,
        bought_product = product.id,
        quantity = quantity,
        total_price = total_price,
        bought_at = datetime.now()
    )
    # vervangen naar print(f'{}')
    print('At ' + (transaction.bought_at) + ', ' + buyer.name + ' bought ' + (transaction.quantity) + ' of ' + product.name + ' at a total price of: €' + (transaction.total_price) + '.')

    new_quantity = product.quantity - quantity

    update_stock(product.id, new_quantity)


def remove_product(product_id):
    product = models.Product.get_by_id(product_id)
    print('Deleting ' + product.name + ' from the database.')
    product.delete_instance()


def main():
    
   
    # Search
    search('sweater')
    

    #>List User Products
    
    # list_user_products(1)
    # list_user_products(2)
    

    #> List all products tagged with '??'
    
    # list_products_per_tag(1)
    

    # # starts selling 
    
    # product = models.Product(name='Olive Oil', description='Fresh olive oil from the farm', price=6.50, quantity=10)
    # add_product_to_catalog(2, product)
    

    #> List User Products again
    
    #list_user_products(1)
   

    #> Now there's only 5 thinks left in the webshop
    
    # update_stock(5, 5)
    

    #> Let's make a transaction
    
    # purchase_product(1, 2, 2)
   

    #> And remove a product
    
    # remove_product(6)
  


if __name__ == '__main__':
    main()
   
    
    
    
  