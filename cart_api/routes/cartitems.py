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
        new_item = DatabaseCartItem(
            name=data["name"],
            price=data['price'],
            quantity=data['quantity']
        )
        new_item.save()
        resp.media = model_to_dict(new_item)
        resp.status = falcon.HTTP_201

    def on_get(self, req, resp):
        all = DatabaseCartItem.select()
        response = []
        for product in all:
            response.append(model_to_dict(product))
        resp.media = response
        resp.status = falcon.HTTP_200


class CartItem:
    def on_get(self, req, resp, item_id):
        item = DatabaseCartItem.get(id=item_id)
        resp.media = model_to_dict(item)
        resp.status = falcon.HTTP_200

    def on_delete(self, req, resp, item_id):
        DatabaseCartItem.delete_by_id(item_id)
        resp.status = falcon.HTTP_204

    def on_patch(self, req, resp, item_id):
        item = DatabaseCartItem.get(id=item_id)
        if "quantity" in req.media:
            item.quantity = req.media['quantity']
            item.save()
        resp.status = falcon.HTTP_204
