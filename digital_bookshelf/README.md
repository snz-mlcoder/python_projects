# Digital Bookshelf 📚

A small Python project to demonstrate the use of magic methods (`__str__`, `__len__`, `__getitem__`, etc.) in object-oriented programming.

## Features
- Create and store books with title, author, and page count
- Combine multiple bookshelves with `+`
- Indexing and searching with Pythonic syntax
- Print-friendly output and debugging info

## Example
```python
shelf = Bookshelf()
shelf.add_book(Book("1984", "George Orwell", 328))
print(shelf[0])
print("1984" in shelf)
