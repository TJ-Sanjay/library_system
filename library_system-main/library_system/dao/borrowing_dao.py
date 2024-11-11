from db_connection import DatabaseConnection

class BorrowingDAO:
    def __init__(self):
        self.conn = DatabaseConnection().get_connection()

    def add_borrowing(self, book_id, user_id, borrow_date, return_date):
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO Borrowing (BookID, UserID, BorrowDate, ReturnDate, Status) VALUES (%s, %s, %s, %s, 'Borrowed')",
            (book_id, user_id, borrow_date, return_date)
        )
        self.conn.commit()
        cursor.close()

    def get_borrowing_history(self):
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Borrowing")
        borrowings = cursor.fetchall()
        cursor.close()
        return borrowings
