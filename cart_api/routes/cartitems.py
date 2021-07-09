import falcon
from playhouse.shortcuts import model_to_dict
from cart_api.database import DatabaseCartItem


# Exercise 3:
# Using the database model you created in Exercise 1 create a cartitems route
# CartItems should have a responder for POST and GET
# CartItem should have responders for GET DELETE PATCH
# Your API response statuses and bodies should conform to your OpenAPI spec

class CartItems:
    def on_post(self, req, resp):
        data = req.media
        item = DatabaseCartItem(
            name=data['name'],
            quantity=data['quantity'],
            price=data['price']
        )
        item.save()
        resp.media = model_to_dict(item)
        resp.status = falcon.HTTP_201

    def on_get(self, req, resp):
        items = DatabaseCartItem.select()
        items_dicts = []
        for product in items:
            items_dicts.append(model_to_dict(product))
        resp.media = items
        resp.status = falcon.HTTP_200




class CartItem:

    def on_get(self, req, resp, item_id):
        product = DatabaseCartItem.get(id=item_id)
        resp.media = model_to_dict(product)
        resp.status = falcon.HTTP_200

































    def on_patch(self, req, resp, item_id):
        data = req.get_media()
        if "quantity" in data:
            x = DatabaseCartItem.get(id=item_id)
            x.quantity = data['quantity']
            x.save()




        # query = DatabaseCartItem.update(quantity=data["quantity"]).where(DatabaseCartItem.id == item_id)
        # query.execute()
        resp.status = falcon.HTTP_204
