def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('products_api', '/products')
    config.add_route('product_api', '/products/{id}')
    config.add_route('cart_api', '/cart/{product_id}')
    config.add_route('orders_api', '/orders')
    config.add_route('order_api', '/orders/{order_id}')
    config.add_route('status_update_api', '/orders/{order_id}/status')