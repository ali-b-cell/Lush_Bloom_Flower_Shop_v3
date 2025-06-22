import typer
from datetime import datetime
from lib.utils import print_divider
from lib.seed import seed_data
from lib.models import Flower, Order, OrderItem, Customer
from lib.database import Base, Session, engine

app = typer.Typer()


Base.metadata.create_all(engine)

@app.command()
def seed():
    """Seed the database with sample data."""
    seed_data()
    print("Database seeded.")

@app.command()
def welcome():
    """Greet the user with a welcome message."""
    print_divider()
    typer.echo("Welcome to Lush & Bloom")
    typer.echo("Elegant Blooms, Everyday Joy.")
    print_divider()

@app.command()
def reset_db():
    """Drop and recreate all tables."""
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    print("Database reset.")

@app.command()
def list_flowers():
    """List all flowers currently in the shop."""
    session = Session()
    flowers = session.query(Flower).all()

    if not flowers:
        typer.echo("No flowers found. Please seed the database.")
    else:
        print_divider()
        for flower in flowers:
            typer.echo(
                f"{flower.id}. {flower.name} — Ksh {flower.price:.2f} — Stock: {flower.stock_quantity}"
            )
        print_divider()
    session.close()

@app.command()
def buy_flower(customer_id: int, flower_id: int, quantity: int):
    """
    Place a new flower order for a customer.
    Requires valid customer_id, flower_id, and available stock.
    """
    session = Session()

    customer = session.query(Customer).filter_by(id=customer_id).first()
    if not customer:
        typer.echo("Customer not found.")
        return

    flower = session.query(Flower).filter_by(id=flower_id).first()
    if not flower:
        typer.echo("Flower not found.")
        return

    if flower.stock_quantity < quantity:
        typer.echo(f"Not enough stock. Only {flower.stock_quantity} available.")
        return

    order = Order(
        customer_id=customer.id,
        date=datetime.now(),
        total_price=round(flower.price * quantity, 2),
    )
    session.add(order)
    session.commit()

    item = OrderItem(
        order_id=order.id,
        flower_id=flower.id,
        quantity=quantity,
    )
    session.add(item)

    flower.stock_quantity -= quantity
    session.commit()

    typer.echo(f"Order placed: {quantity} x {flower.name} for {customer.name} — Total: Ksh {order.total_price:.2f}")
    session.close()

if __name__ == "__main__":
    app()
