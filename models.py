from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Author(Base):
    __tablename__ = 'author'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

    def __str__(self):
        return self.name


class Genre(Base):
    __tablename__ = 'genre'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

    def __str__(self):
        return self.name


class Books(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    genre_id = Column(ForeignKey('genre.id'), nullable=False)
    author_id = Column(ForeignKey('author.id'), nullable=False)
    year = Column(Integer, nullable=False)

    genre_obj = relationship("Genre")
    author_obj = relationship("Author")

    def __str__(self):
        return self.name


