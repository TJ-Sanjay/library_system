from library_system.dao_factory import DAOFactory

class BookService:
    def __init__(self):
        self.book_dao = DAOFactory.get_dao("BookDAO")

    def add_book(self, title, isbn, author_id, category_id, publication_year):
        self.book_dao.add_book(title, isbn, author_id, category_id, publication_year)

    def list_books(self):
        return self.book_dao.get_books()
