from sqlalchemy import (
    Column,
    Integer,
)

from .meta import Base


class OrderedProduct(Base):
    __tablename__ = 'ordered_product'
    id = Column(Integer, primary_key=True)
    odrer_id = Column(Integer, nullable=False)
    product_id = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'order_id': self.odrer_id,
            'product_id': self.product_id,
            'quantity': self.quantity
        }