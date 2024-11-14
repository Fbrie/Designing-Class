# main.py

from book import Book, SpecialEditionBook
from polymorphism import Car, Plane, Boat, demonstrate_move

# Testing Assignment 1 (Book)
book = Book("The Great Controversy", "Ellen G. White", 15.99)
book.display_details()
book.apply_discount(10)

special_book = SpecialEditionBook("The Great Controversy", "Ellen G. White", 30.00, "Leather cover, Signed by author")
special_book.display_details()
special_book.apply_discount(10)

# Testing Assignment 2 (Polymorphism)
car = Car()
plane = Plane()
boat = Boat()

# Demonstrating polymorphism
demonstrate_move(car)    # Output: Driving 🚗
demonstrate_move(plane)  # Output: Flying ✈️
demonstrate_move(boat)   # Output: Sailing 🚤
