# read_books.py: reads the catalog back from CSV and analyzes it
import csv

with open("books.csv", "r", encoding="utf-8") as f:
    books = list(csv.DictReader(f))

print(f"Loaded {len(books)} books")
print(books[0])

total = 0
high_rated = 0
for book in books:
    total += float(book["price"])
    if int(book["rating"]) >= 4:
        high_rated += 1

print(f"Average price: {total / len(books):.2f}")
print(f"Books rated 4 or more: {high_rated}") 