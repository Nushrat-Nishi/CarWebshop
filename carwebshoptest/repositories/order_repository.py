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


    @classmethod
    def get_one(cls, id):
        session = DbSessionFactory.create_session()
        order = session.query(Order).filter(Order.id == id).first()
        session.close()

        return order


    @classmethod
    def is_exist(cls, id):
        session = DbSessionFactory.create_session()
        exists = session.query(Order.id).filter_by(id=id).scalar()
        session.close()

        return exists


    @classmethod
    def update(cls, id, status):
        session = DbSessionFactory.create_session()

        saved_order = session.query(Order).filter(Order.id == id).first()

        saved_order.status = status

        session.commit()