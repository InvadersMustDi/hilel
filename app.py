from flask import Flask, render_template, request
from sqlalchemy.orm import sessionmaker

from db import engine
from forms import GenreForm, BooksForm, session, AuthorFrom
from models import Genre, Books, Author

app = Flask(__name__, template_folder='templates')


def create_form_handler(form_class, model_class, title):
    form = form_class()
    success = False
    if request.method == 'POST':
        form = form_class(request.form)
        if form.validate():
            obj = model_class()
            form.populate_obj(obj)
            session.add(obj)
            session.commit()
            success = True
            print(obj)

    return render_template(
        'create_model.html', **{
            'form': form,
            'title': title,
            'success': success
        }
    )


@app.route('/')
def home():
    books = session.query(Books).all()
    return render_template(
        'templates_index.html', **{'books': books}
    )


@app.route('/create/', methods=['GET', 'POST'])
def create_books():
    return create_form_handler(BooksForm, Books, "Add Books")


@app.route('/add/author/', methods=['GET', 'POST'])
def add_author():
    return create_form_handler(AuthorFrom, Author, 'Add Author')


@app.route('/add/genre/', methods=['GET', 'POST'])
def add_genre():
    return create_form_handler(GenreForm, Genre, 'Add Genre')


if __name__ == '__main__':
    app.run(debug=True)
