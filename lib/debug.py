from database import Session
from lib.utils import print_divider
from models import Flower

session = Session()

def test_flowers():
    print_divider()
    print(" Current Flowers in DB:")
    flowers = session.query(Flower).all()
    for flower in flowers:
        print(f"{flower.id}. {flower.name}) - Ksh {flower.price:.2f}")
    print_divider()

if __name__ == "__main__":
    test_flowers()
    session.close()
