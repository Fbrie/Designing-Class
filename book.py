# Base class: Book
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_details(self):
        print(f"Book: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: ${self.price}")

    def apply_discount(self, discount_percentage):
        self.price = self.price - (self.price * discount_percentage / 100)
        print(f"New price after discount: ${self.price:.2f}")


# Subclass: SpecialEditionBook (inherits from Book)
class SpecialEditionBook(Book):
    def __init__(self, title, author, price, special_features):
        super().__init__(title, author, price)
        self.special_features = special_features

    def display_details(self):
        super().display_details()
        print(f"Special Features: {self.special_features}")

    def apply_discount(self, discount_percentage):
        discount_percentage = discount_percentage - 5  # Apply 5% less discount
        super().apply_discount(discount_percentage)
