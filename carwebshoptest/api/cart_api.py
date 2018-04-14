from pyramid.request import Request
from pyramid.response import Response
from pyramid.view import view_config

from ..repositories.product_repository import ProductRepository


@view_config(route_name='cart_api', request_method='POST', renderer='json')
def add_to_cart(request: Request):
    product_id = int(request.matchdict['product_id'])

    is_exist = ProductRepository.is_exist(product_id)

    if is_exist is None:
        return Response(status=404, json_body={'error': "The product with id '{}' is not found.".format(product_id)})

    try:
        cart_json = request.json_body
    except Exception as ex:
        return Response(status=400, body='Bad input.')

    quantity = int(cart_json.get('quantity'))

    errors = []
    if quantity is None:
        errors.append("quantity is a required field.")
    elif quantity < 0:
        errors.append("quantity must be non-negative.")
    elif quantity == 0:
        return Response(status=204)

    if errors:
        return Response(status=400, body='There are errors with your request: \n' + '\n'.join(errors))

    cart_cookie = request.cookies.get('Cart')

    if cart_cookie is None:
        cart = [{'product_id': product_id, 'quantity': quantity}]
    else:
        cart = eval(cart_cookie)
        cart_item = product_already_in_cart(cart, product_id)
        if cart_item is None:
            cart.append({'product_id': product_id, 'quantity': quantity})
        else:
            cart_item['quantity'] = quantity


    response = Response(status=200)
    response.set_cookie('Cart', str(cart), max_age=31536000)  # max_age = year
    return response


def product_already_in_cart(cart, product_id):
    for cart_item in cart:
        if cart_item['product_id'] == product_id:
            return cart_item