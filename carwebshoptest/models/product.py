from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
)

from .meta import Base
from decimal import Decimal


class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    description = Column(Text)
    brand = Column(Text)
    category = Column(Text)
    purchase_price = Column(Decimal)
    sales_price = Column(Decimal)
    sku = Column(Text)


Index('product_brand_index', Product.brand, mysql_length=255)
Index('product_category_index', Product.category, mysql_length=255)
