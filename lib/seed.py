from faker import Faker
from random import randint, choice as rc, sample
from datetime import datetime

from lib.models import Customer, Flower, Order, OrderItem
from lib.database import Session

fake = Faker()
session = Session()

FLOWER_NAMES = [
    "Rose", "Tulip", "Lily", "Daisy", "Orchid", "Sunflower", "Spring Mix",
    "Carnation", "Peony", "Chrysanthemum", "Lavender", "Marigold",
    "Gardenia", "Begonia", "Zinnia", "Geranium", "Hibiscus", "Iris",
    "Daffodil", "Magnolia"
]

def seed_data():
    print("Seeding database...")


    session.query(OrderItem).delete()
    session.query(Order).delete()
    session.query(Flower).delete()
    session.query(Customer).delete()

    
    customers = []
    for _ in range(10):
        first, last = fake.first_name(), fake.last_name()
        customers.append(
            Customer(
                name=f"{first} {last}",
                email=f"{first.lower()}.{last.lower()}@example.com"
            )
        )
    session.add_all(customers)

    
    for name in sample(FLOWER_NAMES, 10):
        session.add(
            Flower(
                name=name,
                price=round(fake.pyfloat(left_digits=2, right_digits=2, positive=True), 2),
                stock_quantity=randint(10, 100)
            )
        )

    session.flush()                 
    flowers = session.query(Flower).all()

    
    for _ in range(10):
        customer = rc(customers)
        order = Order(customer=customer, date=fake.date_this_year(), total_price=0)
        session.add(order)
        session.flush()

        total = 0
        for _ in range(randint(1, 3)):
            flower = rc(flowers)
            quantity = randint(1, 5)
            total += flower.price * quantity

            session.add(OrderItem(order=order, flower=flower, quantity=quantity))

        order.total_price = round(total, 2)

    session.commit()
    print("Done seeding!")

if __name__ == "__main__":
    seed_data()
