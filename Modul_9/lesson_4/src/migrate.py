from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Author, Book

source_engine = create_engine('sqlite:///source_library.db')
SourceSession = sessionmaker(bind=source_engine)
source_session = SourceSession()

dest_engine = create_engine('sqlite:///destination_library.db')
Base.metadata.create_all(dest_engine)
DestSession = sessionmaker(bind=dest_engine)
dest_session = DestSession()

authors = source_session.query(Author).all()
for author in authors:
    new_author = Author(id=author.id, name=author.name)
    dest_session.add(new_author)

books = source_session.query(Book).all()
for book in books:
    new_book = Book(id=book.id, title=book.title, author_id=book.author_id)
    dest_session.add(new_book)

dest_session.commit()