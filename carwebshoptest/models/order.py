from sqlalchemy import (
    Column,
    Integer,
    Text,
    DateTime,
)

from .meta import Base


class Order(Base):
    __tablename__ = 'order'
    id = Column(Integer, primary_key=True)
    shipping_address = Column(Text, nullable=False)
    delivery_date = Column(DateTime)
    delivery_time = Column(Text)
    status = Column(Text, nullable=False)


    def to_dict(self):
        return {
            'id': self.id,
            'shipping_address': self.shipping_address,
            'delivery_date': str(self.delivery_date),
            'delivery_time': self.delivery_time,
            'status': str(self.status)
        }