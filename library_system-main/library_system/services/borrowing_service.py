from dao_factory import DAOFactory

class BorrowingService:
    def __init__(self):
        self.borrowing_dao = DAOFactory.get_dao("BorrowingDAO")

    def borrow_book(self, book_id, user_id, borrow_date, return_date):
        self.borrowing_dao.add_borrowing(book_id, user_id, borrow_date, return_date)

    def list_borrowing_history(self):
        return self.borrowing_dao.get_borrowing_history()
