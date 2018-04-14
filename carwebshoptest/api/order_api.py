from pyramid.request import Request
from pyramid.response import Response
from pyramid.view import view_config

from carwebshoptest.api.validators.order_validator import OrderValidator
from carwebshoptest.models.ordered_product import OrderedProduct
from ..repositories.order_repository import OrderRepository
from ..repositories.ordered_product_repository import OrderedProductRepository


@view_config(route_name='orders_api', request_method='GET', renderer='json')
def products(_):
    # TODO: implement pagination
    orders = OrderRepository.get_all(limit=50)

    order_json_list = []
    for order in orders:
        order_dict = order.to_dict()

        ordered_products_dict_list = []
        ordered_products = OrderedProductRepository.get_by_order_id(order.id)
        for ordered_product in ordered_products:
            ordered_products_dict_list.append({'product_id': ordered_product.product_id, 'quantity': ordered_product.quantity})
        order_dict['odered_product'] = ordered_products_dict_list
        order_json_list.append(order_dict)

    return order_json_list


@view_config(route_name='orders_api', request_method='POST', renderer='json')
def create_order(request: Request):
    try:
        order_json = request.json_body
    except Exception as ex:
        print(ex)
        return Response(status=400, body='Bad input.')

    order_validator = OrderValidator(order_json)
    order_validator.validate()

    if order_validator.errors:
        return Response(status=400, body=order_validator.error_msg())

    try:
        order = OrderRepository.create(order_validator.order)

        cart_cookie = request.cookies.get('Cart')
        if cart_cookie is None:
            return Response(status=400, body='Cart is empty.')
        else:
            cart = eval(cart_cookie)
            for cart_item in cart:
                ordered_product = OrderedProduct(odrer_id=order.id,
                                                 product_id=cart_item['product_id'],
                                                 quantity=cart_item['quantity'])
                OrderedProductRepository.create(ordered_product)
            response = Response(status=201, json_body=order.to_dict())
            response.delete_cookie('Cart')
        return response
    except Exception as ex:
        return Response(status=500, body='Something bad happened, call admin!')

@view_config(route_name='order_api', request_method='GET', renderer='json')
def order(request: Request):
    order_id = request.matchdict['order_id']

    order = OrderRepository.get_one(order_id)

    order_dict = order.to_dict()

    ordered_products_dict_list = []
    ordered_product = OrderedProductRepository.get_by_order_id(order_id)

    for ordered_product in ordered_product:
        ordered_products_dict_list.append({'product_id': ordered_product.product_id, 'quantity': ordered_product.quantity})

    order_dict['odered_product'] = ordered_products_dict_list


    return order_dict

@view_config(route_name='status_update_api', request_method='PUT')
def update_status(request: Request):
    id = request.matchdict['order_id']

    is_exist = OrderRepository.is_exist(id)

    if is_exist is None:
        return Response(status=404, json_body={'error': "The order with id '{}' is not found.".format(id)})

    try:
        status_json = request.json_body
        status = status_json.get('status')
        OrderRepository.update(id, status)
        return Response(status=204)
    except Exception as ex:
        return Response(status=500, body='Something bad happened, call admin!')