from ..factory.db_session_factory import DbSessionFactory
from ..models.order import Order


class OrderRepository:

    @classmethod
    def get_all(cls, limit=None):
        session = DbSessionFactory.create_session()

        query = session.query(Order).order_by(Order.id.desc())

        if limit:
            orders = query[:limit]
        else:
            orders = query.all()

        session.close()

        return orders

    @classmethod
    def create(cls, order: Order):
        session = DbSessionFactory.create_session()
        session.add(order)
        session.commit()

        return order