import falcon
from playhouse.shortcuts import model_to_dict
from cart_api.database import DatabaseProducts


class Product:
    def on_get(self, req, resp, product_id):
        product = DatabaseProducts.get(id=product_id)
        resp.media = model_to_dict(product)
        resp.status = falcon.HTTP_200

    def on_delete(self, req, resp, product_id):
        DatabaseProducts.delete_by_id(product_id)
        resp.status = falcon.HTTP_204


# Excercise 2:
# Products route should respond to GET and POST requests
# GET products returns a list of every product in the database
# POST products creates a product and returns the data it created


class Products:
    def on_get(self, req, resp):
        products = DatabaseProducts.select()
        products_dicts = []
        for product in products:
            products_dicts.append(model_to_dict(product))
        resp.media = products_dicts
        resp.status = falcon.HTTP_200

    def on_post(self, req, resp):
        data = req.get_media()
        new_product = DatabaseProducts(
            name=data.get('name'),
            description=data.get('description'),
            image_url=data.get('image_url'),
            price=data.get('price'),
            is_on_sale=data.get('is_on_sale'),
            sale_price=data.get('sale_price')
        )
        new_product.save()
        resp.status = falcon.HTTP_201
        resp.media = model_to_dict(new_product)
