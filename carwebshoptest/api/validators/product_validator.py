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
        purchase_price = Decimal(self.data_dict.get('purchase_price'))
        sales_price = Decimal(self.data_dict.get('sales_price'))
        sku = self.data_dict.get('sku')
        stock = int(self.data_dict.get('stock', 0))

        if not name:
            self.errors.append("name is a required field.")

        if purchase_price is None:
            self.errors.append("purchase_price is a required field.")
        elif purchase_price < 0:
            self.errors.append("purchase_price must be non-negative.")

        if sales_price is None:
            self.errors.append("sales_price is a required field.")
        elif sales_price < 0:
            self.errors.append("sales_price must be non-negative.")

        if sku is None:
            self.errors.append("sku is a required field.")

        if not self.errors:
            product = Product(id=id, name=name, description=description, brand=brand, category=category,
                              purchase_price=purchase_price, sales_price=sales_price, sku=sku, stock=stock)
            self.product = product