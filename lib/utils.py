from datetime import datetime

def format_price(price):
    """Format price to 2 decimal places with currency."""
    return f"Ksh {price:.2f}"

def print_divider():
    """Print a styled divider for the CLI."""
    print("\n" + "-" * 40 + "\n")

def validate_email(email):
    """Very basic email validation."""
    return "@" in email and "." in email

def current_date():
    """Returns current date as a string (YYYY-MM-DD)."""
    return datetime.now().strftime("%Y-%m-%d")