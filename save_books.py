# save_books.py: saves the book catalog to a CSV file
import csv

books = [
    {"title": "A Light in the Attic", "price": 51.77, "rating": 3},
    {"title": "Tipping the Velvet", "price": 53.74, "rating": 1},
    {"title": "Soumission", "price": 50.10, "rating": 1},
    {"title": "Sharp Objects", "price": 47.82, "rating": 4},
    {"title": "Sapiens", "price": 54.23, "rating": 5},
    {"title": "The Requiem Red", "price": 22.65, "rating": 1},
]

with open("books.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["title", "price", "rating"])
    writer.writeheader()
    writer.writerows(books)

print(f"Saved {len(books)} books to books.csv") 
# read_books.py: loads books.csv back into Python and analyzes it
import csv

with open("books.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    books = list(reader)

print(f"Loaded {len(books)} books")
print(books[0])

total = 0
high_rated = 0
for book in books:
    price = float(book["price"])
    rating = int(book["rating"])
    total += price
    if rating >= 4:
        high_rated += 1

average = total / len(books)
print(f"Average price: {average:.2f}")
print(f"Books rated 4 or more: {high_rated}")