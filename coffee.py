price = float(input("Price of one coffee: "))
quantity = int(input("How many coffees? "))
tip_percent = float(input("Tip in percent: "))

subtotal = price * quantity
tip = subtotal * tip_percent / 100
total = subtotal + tip

print(f"Subtotal: {subtotal:.2f}")
print(f"Tip: {tip:.2f}")
print(f"Total: {total:.2f}") 