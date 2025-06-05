import typer
from lib.helpers import print_divider
from lib.models import Flower
from lib.database import Session  

app = typer.Typer()

@app.command()
def welcome():
    """Greet the user with a welcome message."""
    print_divider()
    typer.echo(" Welcome to Lush & Bloom ")
    typer.echo("Elegant Blooms, Everyday Joy.")
    print_divider()

@app.command()
def list_flowers():
    """List all flowers currently in the shop."""
    session = Session()
    flowers = session.query(Flower).all()

    if not flowers:
        typer.echo("No flowers found. Please seed the database.")
        return

    for flower in flowers:
        typer.echo(f"{flower.id}. {flower.name} ) - Ksh {flower.price:.2f}")

if __name__ == "__main__":
    app()
