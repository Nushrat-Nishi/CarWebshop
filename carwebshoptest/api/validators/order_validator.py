from datetime import datetime

from carwebshoptest.models.order import Order


class OrderValidator():
    def __init__(self, data_dict):
        self.data_dict = data_dict
        self.errors = []
        self.order = None

    def validate(self):

        id = self.data_dict.get('id')
        shipping_address = self.data_dict.get('shipping_address')
        delivery_date = datetime_object = datetime.strptime(self.data_dict.get('delivery_date'), '%Y-%m-%d')
        delivery_time = self.data_dict.get('delivery_time')
        status = self.data_dict.get('status')

        if shipping_address is None:
            self.errors.append("shipping_address is a required field.")

        if not self.errors:
            order = Order(id=id, shipping_address=shipping_address, delivery_date=delivery_date, delivery_time=delivery_time, status=status)
            self.order = order

    def error_msg(self):
        msg = 'There are errors with your request: \n' + \
              '\n'.join(self.errors)

        return msg
