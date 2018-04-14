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
    purchase_price = Column(DECIMAL)
    sales_price = Column(DECIMAL)
    sku = Column(Text)

