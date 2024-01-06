class Book:
    def __init__(
            self,
            book_title: str,
            book_author: str,
    ):
        self.book_title = book_title
        self.book_author = book_author
    def __str__(self):
        return f"Название: {self.book_title}, Автор: {self.book_author}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book_title, book_author):
        book = Book(book_title, book_author)
        self.books.append(book)
        return self

    def remove_book(self, title):
        for book in self.books:
            if book.book_title == title:
                self.books.remove(book)
                return self
        return self

    def __contains__(self, title):
        return any(book.book_title == title for book in self.books)

    def __getitem__(self, index):
        return self.books[index]


print("Добавляем книги в библиотеку")

library = Library()
library.add_book("Книга 1", "Автор 1").add_book("Книга 2", "Автор 2").add_book("Книга 3", "Автор 1")

print("Проверяем наличие книг")
print("Книга 1 в библиотеке:", "Книга 1" in library)
print("Книга 2 в библиотеке:", "Книга 2" in library)
print("Книга 3 в библиотеке:", "Книга 3" in library)

print("Удаляем Книгу 2 из библиотеки, и добавляем еще 2 книги")

library.remove_book("Книга 2").add_book("Книга 4", "Автор 4").add_book("Книга 5", "Автор 5")

print("Проверяем наличие книг в библиотеке")
print("Книга 1 в библиотеке:", "Книга 1" in library)
print("Книга 2 в библиотеке:", "Книга 2" in library)
print("Книга 3 в библиотеке:", "Книга 3" in library)
print("Книга 3 в библиотеке:", "Книга 4" in library)
print("Книга 3 в библиотеке:", "Книга 5" in library)

print("Ищем книгу по индексу")

book = library[0]

print(f"Первая книга: {book.book_title}, {book.book_author}")

print("Ищем книги по разрезу")

books = library[2:]

for book in books:
    print(f"Книги с третьей и до конца библиотеки: {book.book_title}, {book.book_author}")

"""
Создайте класс Library, который будет содержать список книг.
Каждая книга должна иметь название и автора.

Реализуйте метод add_book, который добавляет книгу в библиотеку.

Реализуйте метод remove_book, который удаляет книгу из библиотеки по названию.

Используйте магический метод __getitem__ для получения книги по индексу.

Используйте методы __contains__ для проверки, есть ли книга в библиотеке по названию.

Реализуйте методы цепочки для добавления и удаления книг
(например, add_book().remove_book().add_book()).


"""