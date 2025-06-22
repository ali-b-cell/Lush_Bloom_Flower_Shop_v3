

from faker import Faker
from random import randint, choice as rc
from datetime import datetime

from lib.models import Customer, Flower, Order, OrderItem
from lib.database import Session

fake = Faker()
session = Session()

def seed_data():
    print(" Seeding database...")

    
    session.query(OrderItem).delete()
    session.query(Order).delete()
    session.query(Flower).delete()
    session.query(Customer).delete()

    
    customers = []
    for _ in range(10):
        customer = Customer(
            name=fake.name(),
            email=fake.email()
        )
        customers.append(customer)
    session.add_all(customers)

    
    flowers = []
    for _ in range(10):
        flower = Flower(
            name=fake.word().capitalize(),
            price=round(fake.pyfloat(left_digits=2, right_digits=2, positive=True), 2),
            stock_quantity=randint(10, 100)
        )
        flowers.append(flower)
    session.add_all(flowers)

    
    for _ in range(10):
        customer = rc(customers)
        order = Order(
            customer=customer,
            date=fake.date_this_year(),
            total_price=0  
        )
        session.add(order)
        session.flush() 

        num_items = randint(1, 3)
        total = 0

        for _ in range(num_items):
            flower = rc(flowers)
            quantity = randint(1, 5)
            total += flower.price * quantity

            order_item = OrderItem(
                order=order,
                flower=flower,
                quantity=quantity
            )
            session.add(order_item)

        order.total_price = round(total, 2)

    session.commit()
    print("Done seeding!")

if __name__ == '__main__':
    seed_data()
