
from ..models import Product
from ..factory.db_session_factory import DbSessionFactory


class ProductRepository:
    __car_data = {}

    @classmethod
    def get_products(cls, limit=None):
        session = DbSessionFactory.create_session()

        query = session.query(Product).order_by(Product.name)

        if limit:
            products = query[:limit]
        else:
            products = query.all()

        session.close()

        return products


    @classmethod
    def create_product(cls, product: Product):
        session = DbSessionFactory.create_session()
        session.add(product)
        session.commit()

        return product


    @classmethod
    def get_product(cls, id):
        session = DbSessionFactory.create_session()
        product = session.query(Product).filter(Product.id == id).first()
        session.close()

        return product