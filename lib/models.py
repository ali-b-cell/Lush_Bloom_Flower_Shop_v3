from sqlalchemy import Column, Date, ForeignKey, Integer, String, Float,Date
from sqlalchemy.orm import relationship
from lib.database import Base

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    orders = relationship("Order", back_populates="customer")

class Flower(Base):
    __tablename__ = 'flowers'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)
    stock_quantity = Column(Integer)
    order_items = relationship("OrderItem", back_populates="flower")

class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    date = Column(Date)
    total_price = Column(Float)
    customer = relationship("Customer", back_populates="orders")
    items = relationship("OrderItem", back_populates="order")

class OrderItem(Base):
    __tablename__ = 'order_items'

    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.id'))
    flower_id = Column(Integer, ForeignKey('flowers.id'))
    quantity = Column(Integer)

    order = relationship("Order", back_populates="items")
    flower = relationship("Flower", back_populates="order_items")

