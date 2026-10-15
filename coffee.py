# coffee.py: a coffee order calculator

def ask_number(question):
    """Keep asking until the answer is a valid number."""
    while True:
        answer = input(question)
        try:
            return float(answer)
        except ValueError:
            print("That's not a number. Use a dot for decimals, like 3.5.")


price = ask_number("Price of one coffee: ")
quantity = int(ask_number("How many coffees? "))
tip_percent = ask_number("Tip in percent: ")

subtotal = price * quantity
tip = subtotal * tip_percent / 100
total = subtotal + tip

print(f"Subtotal: {subtotal:.2f}")
print(f"Tip: {tip:.2f}")
print(f"Total: {total:.2f}")