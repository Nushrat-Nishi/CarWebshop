from decimal import Decimal

from carwebshoptest.models import Product


class ProductValidator():
    def __init__(self, data_dict):
        self.data_dict = data_dict
        self.errors = []
        self.product = None

    def validate(self):

        id = self.data_dict.get('id')
        name = self.data_dict.get('name')
        description = self.data_dict.get('description')
        brand = self.data_dict.get('brand')
        category = self.data_dict.get('category')
        sales_price = Decimal(self.data_dict.get('sales_price'))
        sku = self.data_dict.get('sku')

        if not name:
            self.errors.append("name is a required field.")

        if sales_price is None:
            self.errors.append("sales_price is a required field.")
        elif sales_price < 0:
            self.errors.append("sales_price must be non-negative.")

        if sku is None:
            self.errors.append("sku is a required field.")

        if not self.errors:
            product = Product(id=id, name=name, description=description, brand=brand, category=category,
                              sales_price=sales_price, sku=sku)
            self.product = product

    def error_msg(self):
        msg = 'There are errors with your request: \n' + \
              '\n'.join(self.errors)

        return msg