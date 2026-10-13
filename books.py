# a small catalog, stored as a list of dictionaries
books = [
    {"title": "A Light in the Attic", "price": 51.77, "rating": 3},
    {"title": "Tipping the Velvet", "price": 53.74, "rating": 1},
    {"title": "Soumission", "price": 50.10, "rating": 1},
    {"title": "Sharp Objects", "price": 47.82, "rating": 4},
    {"title": "Sapiens", "price": 54.23, "rating": 5},
]

print(f"Books in the catalog: {len(books)}")
print(f"First book: {books[0]['title']}")
print(f"Last book: {books[-1]['title']}")
print(f"Price of the third book: {books[2]['price']}")

books.append({"title": "The Requiem Red", "price": 22.65, "rating": 1})
print(f"After adding one: {len(books)} books")

total = 0
for book in books:
    total += book["price"]
print(f"Average price: {total / len(books):.2f}")


high_rated = 0
for book in books:
    if book["rating"] >= 4:
        high_rated += 1
print(f"Books rated 4 or more: {high_rated}")

most_expensive = books[0]
for book in books:
    if book["price"] > most_expensive["price"]:
        most_expensive = book
print(f"Most expensive: {most_expensive['title']} ({most_expensive['price']:.2f})")

print()
print(f"{'Title':<25}{'Price':>8}{'Rating':>8}")
for book in books:
    print(f"{book['title']:<25}{book['price']:>8.2f}{book['rating']:>8}")




  