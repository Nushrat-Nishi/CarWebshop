def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('products_api', '/products')
    config.add_route('product_api', '/products/{id}')
    config.add_route('cart_api', '/cart/{product_id}')