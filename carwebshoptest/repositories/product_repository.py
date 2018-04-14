
from ..models import Product
from ..factory.db_session_factory import DbSessionFactory


class ProductRepository:
    __car_data = {}

    @classmethod
    def get_all(cls, limit=None):
        session = DbSessionFactory.create_session()

        query = session.query(Product).order_by(Product.name)

        if limit:
            products = query[:limit]
        else:
            products = query.all()

        session.close()

        return products


    @classmethod
    def create(cls, product: Product):
        session = DbSessionFactory.create_session()
        session.add(product)
        session.commit()

        return product


    @classmethod
    def get_one(cls, id):
        session = DbSessionFactory.create_session()
        product = session.query(Product).filter(Product.id == id).first()
        session.close()

        return product


    @classmethod
    def is_exist(cls, id):
        session = DbSessionFactory.create_session()
        exists = session.query(Product.id).filter_by(id=id).scalar()
        session.close()

        return exists


    @classmethod
    def update(cls, id, product: Product):
        session = DbSessionFactory.create_session()

        saved_product = session.query(Product).filter(Product.id == id).first()

        saved_product.name = product.name
        saved_product.description = product.description
        saved_product.brand = product.brand
        saved_product.category = product.category
        saved_product.purchase_price = product.purchase_price
        saved_product.sales_price = product.sales_price
        saved_product.sku = product.sku
        saved_product.stock = product.stock

        session.commit()


    @classmethod
    def delete(cls, id):
        session = DbSessionFactory.create_session()

        saved_product = session.query(Product).filter(Product.id == id).first()

        if not saved_product:
            return

        session.delete(saved_product)
        session.commit()
