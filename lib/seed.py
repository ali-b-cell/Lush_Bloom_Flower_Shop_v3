from lib.models import Flower, Customer, Order, OrderItem
from lib.database import Session, Base, engine

def seed_data():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    session = Session()

    
    flower1 = Flower(name="Rose", price=59.99)
    flower2 = Flower(name="Tulip", price=99.99)
    flower3 = Flower(name="Lily", price=129.99)
    session.add_all([flower1, flower2, flower3])
    session.commit()
    print("Seeded flowers successfully!")

    
    customer1 = Customer(name="Marie", email="marie@outlook.com")
    customer2 = Customer(name="Isaack", email="izzie@gmail.com")
    customer3 = Customer(name="Lucinda", email="lc_nder@yahoo.com")
    session.add_all([customer1, customer2, customer3])
    session.commit()
    print("Seeded customers successfully!")

    
    order1 = Order(customer_id=customer1.id)
    order2 = Order(customer_id=customer2.id)
    order3 = Order(customer_id=customer3.id)
    session.add_all([order1, order2, order3])
    session.commit()
    print("Seeded orders successfully!")

    
    item1 = OrderItem(order_id=order1.id, flower_id=flower1.id, quantity=2)
    item2 = OrderItem(order_id=order2.id, flower_id=flower2.id, quantity=8)
    item3 = OrderItem(order_id=order3.id, flower_id=flower3.id, quantity=4)
    session.add_all([item1, item2, item3])
    session.commit()
    print("Seeded order items successfully!")

    session.close()

if __name__ == "__main__":
    seed_data()
