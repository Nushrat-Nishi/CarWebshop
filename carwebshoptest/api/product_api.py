from pyramid.request import Request
from pyramid.response import Response
from pyramid.view import view_config
import logbook


from carwebshoptest.api.validators.product_validator import ProductValidator
from ..repositories.product_repository import ProductRepository

log = logbook.Logger("API/Auto")

@view_config(route_name='products_api', request_method='GET', renderer='json')
def products(_):
    # TODO: implement pagination
    products = ProductRepository.get_all(limit=50)

    product_json_list = []
    for product in products:
        product_json_list.append(product.to_dict())

    return product_json_list


@view_config(route_name='products_api', request_method='POST', renderer='json')
def create_product(request: Request):
    try:
        product_json = request.json_body
    except Exception as ex:
        return Response(status=400, body='Bad input.')

    product_validator = ProductValidator(product_json)
    product_validator.validate()
    if product_validator.errors:
        return Response(status=400, body=product_validator.error_msg())

    try:
        product = ProductRepository.create(product_validator.product)
        return Response(status=201, json_body=product.to_dict())
    except Exception as ex:
        return Response(status=500, body='Something bad happened, call admin!')


@view_config(route_name='product_api', request_method='GET', renderer='json')
def get_product(request: Request):
    id = request.matchdict['id']
    product = ProductRepository.get_one(id)

    if not product:
        return Response(status=404, json_body={'error': "The product with id '{}' is not found.".format(id)})

    return product.to_dict()


@view_config(route_name='product_api', request_method='PUT')
def update_product(request: Request):
    id = request.matchdict['id']

    is_exist = ProductRepository.is_exist(id)

    if is_exist is None:
        return Response(status=404, json_body={'error': "The product with id '{}' is not found.".format(id)})

    try:
        product_json = request.json_body
    except Exception as ex:
        return Response(status=400, body='Bad input.')

    product_validator = ProductValidator(product_json)
    product_validator.validate()
    if product_validator.errors:
        return Response(status=400, body=product_validator.error_msg)

    try:
        product = product_validator.product
        ProductRepository.update(id, product)

        return Response(status=204)
    except Exception as ex:
        return Response(status=500, body='Something bad happened, call admin!')


@view_config(route_name='product_api', request_method='DELETE')
def delete_product(request: Request):
    id = request.matchdict['id']

    is_exist = ProductRepository.is_exist(id)

    if is_exist is None:
        return Response(status=404, json_body={'error': "The product with id '{}' is not found.".format(id)})

    try:
        ProductRepository.delete(id)
        return Response(status=204)
    except Exception as ex:
        return Response(status=500, body='Something bad happened, call admin!')
