from pyramid.view import view_config

from ..repositories.product_repository import ProductRepository


@view_config(route_name='product_api', request_method='GET', renderer='json')
def products(_):
    products = ProductRepository.get_products(limit=10)
    return products
