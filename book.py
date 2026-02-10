class Book:
    def __init__(self,name,price,author):
        self.name=name
        self.price=price
        self.author=author
    def bookInfo(self):
        return f"{self.name} written by {self.author}, price:{self.price}"
b1=Book("indulekha",199,"chandu menon")
print(b1.bookInfo())


