# OOP Polymorphism and Inheritance Challenge - Book and Vehicle Example

This repository demonstrates two Object-Oriented Programming (OOP) concepts:
- **Inheritance**: Creating classes that inherit attributes and methods from other classes.
- **Polymorphism**: Defining the same method in different ways for different classes.

## Assignment 1: Design Your Own Class - Book Example
- This assignment demonstrates how to create a base class and a subclass using inheritance.
- Example: A `Book` class with methods for displaying details and applying a discount. A `SpecialEditionBook` class that inherits from `Book` and overrides the `display_details()` and `apply_discount()` methods.

### Usage:
```python
from book import Book, SpecialEditionBook

# Create a Book object
book = Book("The Great Contoversy", "Ellen G.White", 15.99)
book.display_details()
book.apply_discount(10)

# Create a SpecialEditionBook object
special_book = SpecialEditionBook("The Great Contoversy", "Ellen G.White", 30.00, "Leather cover, Signed by author")
special_book.display_details()
special_book.apply_discount(10)
