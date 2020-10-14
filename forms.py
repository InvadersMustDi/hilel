from sqlalchemy.orm import sessionmaker, scoped_session
from wtforms.ext.sqlalchemy.orm import model_form
from models import Books, Author, Genre

from db import engine

session = scoped_session(sessionmaker(bind=engine))

BooksForm = model_form(Books, db_session=session)
AuthorFrom = model_form(Author)
GenreForm = model_form(Genre)
