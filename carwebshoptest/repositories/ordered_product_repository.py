from ..factory.db_session_factory import DbSessionFactory
from ..models.ordered_product import OrderedProduct


class OrderedProductRepository:

    @classmethod
    def get_by_order_id(cls, order_id):
        session = DbSessionFactory.create_session()

        query = session.query(OrderedProduct).filter(OrderedProduct.odrer_id == order_id)
        ordered_products = query.all()

        session.close()

        return ordered_products


    @classmethod
    def create(cls, ordered_product: OrderedProduct):
        session = DbSessionFactory.create_session()
        session.add(ordered_product)
        session.commit()

        return ordered_product