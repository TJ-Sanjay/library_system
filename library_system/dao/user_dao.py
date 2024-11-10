from library_system import db_connection

class UserDAO:
    def __init__(self):
        self.conn = db_connection.DatabaseConnection().get_connection()

    def add_user(self, name, email, membership_id):
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO Users (Name, Email, MembershipID) VALUES (%s, %s, %s)",
            (name, email, membership_id)
        )
        self.conn.commit()
        cursor.close()

    def get_users(self):
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Users")
        users = cursor.fetchall()
        cursor.close()
        return users
