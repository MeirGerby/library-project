class Book:
    def __init__(self, title: str, author: str, isbn: int):
        self.title: str = title
        self.author: str = author
        self.isbn: int = isbn
        self.available: bool = True

    def __str__(self):
        print(f'Book: title {self.title}, author{self.author}')

