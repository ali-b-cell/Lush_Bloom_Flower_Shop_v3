from datetime import datetime

def format_price(price):

    return f"Ksh {price:.2f}"

def print_divider():

    print("\n" + "-" * 40 + "\n")

def validate_email(email):
    
    return "@" in email and "." in email

def current_date():
    
    return datetime.now().strftime("%Y-%m-%d")