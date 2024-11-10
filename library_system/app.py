from flask import Flask, render_template, request, redirect, url_for

from library_system.db_connection import DatabaseConnection
from services.book_service import BookService
from services.user_service import UserService
from services.borrowing_service import BorrowingService

app = Flask(__name__)

@app.route('/')
def index():
    book_service = BookService()
    books = book_service.list_books()
    user_service = UserService()
    users = user_service.list_users()
    return render_template('index.html', books=books, users=users)

@app.route('/add_book', methods=['POST'])
def add_book():
    title = request.form['title']
    isbn = request.form['isbn']
    author_id = request.form['author']
    category_id = request.form['category']
    publication_year = request.form['publicationYear']
    
    book_service = BookService()
    book_service.add_book(title, isbn, author_id, category_id, publication_year)
    
    return redirect(url_for('index'))

@app.route('/add_user', methods=['POST'])
def add_user():
    name = request.form['userName']
    email = request.form['email']
    membership_id = request.form['membershipID']
    
    user_service = UserService()
    user_service.add_user(name, email, membership_id)
    
    return redirect(url_for('index'))

@app.route('/borrow_book', methods=['POST'])
def borrow_book():
    book_id = request.form['borrowBookID']
    user_id = request.form['borrowUserID']
    borrow_date = request.form['borrowDate']
    return_date = request.form['returnDate']
    
    borrowing_service = BorrowingService()
    borrowing_service.borrow_book(book_id, user_id, borrow_date, return_date)
    
    return redirect(url_for('index'))

# Clean up the singleton connection when the app stops
@app.teardown_appcontext
def close_connection(exception):
    db_connection = DatabaseConnection()
    db_connection.close_connection()

if __name__ == '__main__':
    app.run(debug=True)
