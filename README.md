# CarWebshop
[![N|Solid](https://trypyramid.com/img/pyramid-60x60.png)]()

Webshop is a web based software developed using the RESTful pattern. Python Pyramid Framework is used here.

## Features!
The users can have the following facilities by this software:
  - A database with all their products
  - Their clients are able to add products to their virtual shopping cart
  - Their clients are able to change the contents of their cart
  - Their clients are able to place an order
  - Their clients are able to supply a preferred date and time of delivery

## Limitation of current version
For the sake of simplicity and time constraint:
  - Login isn't implemented. Anonymous user can order the product.
  - Currently there is no authentication & authorization
  - I didn't maintain any stock assuming car parts aren't in the inventory.
  - The cart is managed in client side using cookie
  - Payment system hasn't been added.

## Tech
Webshop uses a number of open source projects to work properly:
* Python Pyramid Framework
* MySQL

## Prerequisite
  - Python 3.6 - sudo add-apt-repository ppa:jonathonf/python-3.6  + sudo apt-get install python3.6
  - Install pip - sudo apt install python-pip
  - Install pyramid - pip install pyramid
  - Python Dev - sudo apt-get install python3-dev
  - MySQL client - sudo apt-get install libmysqlclient-dev + venv/bin/pip install mysqlclient

## Getting Started!
```
git clone https://github.com/Nushrat-Nishi/CarWebshop
cd CarWebshop
venv/bin/pserve development.ini
```

## API Documentation
Download postman collection from [here](https://github.com/Nushrat-Nishi/CarWebshop/blob/master/CarWebshop.postman_collection.json)

##### POST Create Product - http://localhost:6543/products
```
Body:
{
"name": "BMW Wheel",
"description": "BMW Wheel",
"brand": "BMW",
"category": "Wheel",
"sales_price":1.2,
"sku": "mn1"
}
```
```
Output:
{
    "id": 1,
    "name": "BMW Wheel",
    "description": "BMW Wheel",
    "brand": "BMW",
    "category": "Wheel",
    "sales_price": "1.20",
    "sku": "mn1"
}
```

##### GET All Product - http://localhost:6543/products
```
[
    {
        "id": 1,
        "name": "BMW Wheel",
        "description": "BMW Wheel",
        "brand": "BMW",
        "category": "Wheel",
        "sales_price": "1.20",
        "sku": "mn1"
    }
]
```

##### GET Product By Id - http://localhost:6543/products/1
```
{
    "id": 1,
    "name": "BMW Wheel",
    "description": "BMW Wheel",
    "brand": "BMW",
    "category": "Wheel",
    "sales_price": "1.20",
    "sku": "mn1"
}
```

##### PUT Update Product - http://localhost:6543/products/1
```
{
"name": "BMW Wheel Updated",
"description": "BMW Wheel",
"brand": "BMW",
"category": "Wheel",
"sales_price":1.2,
"sku": "mn1"
}
```
##### DELETE Delete Product - http://localhost:6543/products/1
```
{
"name": "BMW Wheel Updated",
"description": "BMW Wheel",
"brand": "BMW",
"category": "Wheel",
"sales_price":1.2,
"sku": "mn1"
}
```
##### POST Add To Cart - http://localhost:6543/cart/1
```
{
"quantity": 6
}
```
##### GET Show added products in the Cart - http://localhost:6543/cart
```
[
    {
        "product_id": 1,
        "quantity": 6
    }
]
```

##### DELETE Product from the Cart - http://localhost:6543/cart/1

##### POST Create an order - http://localhost:6543/orders
```
Body:
{
"shipping_address": "Amsterdam",
"delivery_date": "1987-07-21",
"delivery_time": "18:00",
"status":"open"
}
```
```
Output:
{
    "id": 1,
    "shipping_address": "Amsterdam",
    "delivery_date": "1987-07-21 00:00:00",
    "delivery_time": "18:00",
    "status": "open"
}
```

##### GET All the orders made - http://localhost:6543/orders
```
[
    {
        "id": 1,
        "shipping_address": "Amsterdam",
        "delivery_date": "1987-07-21 00:00:00",
        "delivery_time": "18:00",
        "status": "open",
        "odered_product": [
            {
                "product_id": 1,
                "quantity": 6
            }
        ]
    }
]
```
##### GET Order by Order Id - http://localhost:6543/orders/1
```
{
    "id": 1,
    "shipping_address": "Amsterdam",
    "delivery_date": "1987-07-21 00:00:00",
    "delivery_time": "18:00",
    "status": "open",
    "odered_product": [
        {
            "product_id": 1,
            "quantity": 6
        }
    ]
}
```
##### PUT Update Order Status - http://localhost:6543/orders/1/status
```
{
"status":"close new"
}
```