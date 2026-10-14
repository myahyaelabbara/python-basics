# functions.py: small reusable machines

def celsius_to_fahrenheit(c):
    """Convert a temperature from Celsius to Fahrenheit."""
    return c * 9 / 5 + 32


def apply_discount(price, pct=10):
    """Return the price after a discount of pct percent."""
    return price * (1 - pct / 100)


def describe_book(book):
    """Return one sentence describing a book dictionary."""
    return f"{book['title']} costs {book['price']:.2f} and is rated {book['rating']} out of 5."

# Testing each machine with three inputs
print(celsius_to_fahrenheit(0))
print(celsius_to_fahrenheit(100))
print(celsius_to_fahrenheit(-40))

print(apply_discount(100))
print(apply_discount(100, 25))
print(apply_discount(80, pct=20))

books = [
    {"title": "A Light in the Attic", "price": 51.77, "rating": 3},
    {"title": "Sharp Objects", "price": 47.82, "rating": 4},
    {"title": "Sapiens", "price": 54.23, "rating": 5},
]
for book in books:
    print(describe_book(book)) 