def includeme(config):

    config.add_route('products_api', '/products')
    config.add_route('product_api', '/products/{id}')
    config.add_route('cart_api', '/cart/{product_id}')
    config.add_route('orders_api', '/orders')
    config.add_route('order_api', '/orders/{order_id}')
    config.add_route('status_update_api', '/orders/{order_id}/status')
    config.add_route('mycart_api', '/cart')