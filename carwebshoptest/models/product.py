from sqlalchemy import (
    Column,
    Integer,
    Text,
    DECIMAL,
)

from .meta import Base


class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    description = Column(Text)
    brand = Column(Text(70), index=True)
    category = Column(Text(70), index=True)
    purchase_price = Column(DECIMAL(5,2))
    sales_price = Column(DECIMAL(5,2))
    sku = Column(Text)
    stock = Column(Integer, server_default="0")

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'brand': self.brand,
            'category': self.category,
            'purchase_price': str(self.purchase_price),
            'sales_price': str(self.sales_price),
            'sku': self.sku,
            'stock': self.stock
        }

