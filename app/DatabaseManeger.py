from sqlite3 import connect

from .enums import Status


class DatabaseManeger:
    def __init__(self, path) -> None:
        self.path = path
        self.conn = self.init_conn()
        self.init_db()

    def init_db(self):
        with open("./app/tables.sql", "r") as tables:
            tables = tables.read()
        tables = tables.split(";")
        for table in tables:
            c = self.conn.cursor()
            c.execute(table)
            self.conn.commit()

    def init_conn(self):
        conn = connect(self.path, check_same_thread=False)
        return conn

    def creat_user(self, phone, name, description):
        query = """INSERT INTO users (phone, name, description) VALUES (?,?,?) """
        c = self.conn.cursor()
        c.execute(query, (phone, name, description))
        self.conn.commit()

    def add_message(self, user_phone, messsage, receipt_date):
        query = """INSERT INTO messsages (user_phone, message, receipt_date) VALUES (?,?,?) """
        c = self.conn.cursor()
        c.execute(query, (user_phone, messsage, receipt_date))
        self.conn.commit()

    def creat_coversation(self, user_phone):
        status = Status.start
        query = """INSERT INTO conversations (user_phone, status) VALUES (?,?)"""
        c = self.conn.cursor()
        c.execute(query, (user_phone, status))
        self.conn.commit()

    def update_status(self, user_phone, status):
        query = """ UPDATE users SET status = ? WHERE user_phone = ?"""
        c = self.conn.cursor()
        c.execute(query, (user_phone, status))
        self.conn.commit()

    def check_regsitration(self, phone):
        query = "SELECT phone FROM users WHERE phone = ?"
        c = self.conn.cursor()
        c.execute(query, (phone))
        if c.fetchone():
            return True
        else:
            return False

    def get_new_messages(self):
        query = """SELECT * FROM messages WHERE processed = 0"""
        c = self.conn.cursor()
        c.execute(query)
        new_messages = c.fetchone()
        return new_messages

    def mark_processed(self, phone):
        query = """ UPDATE messages SET processed = 1 WHERE user_phone = ?"""
        c = self.conn.cursor()
        c.execute(query, (phone))
        self.conn.commit()

    def check_conversation_progress(self, phone):
        query = """SELECT status FROM conversations WHERE phone = ? """
        c = self.conn.cursor()
        c.execute(query,(phone))
        status = c.fetchone()
        if status:
            if status != 'finished':
                return True
        else:
            return False 
    def update_conversation_status(self,user_phone, status):
        query = """ UPDATE conversations SET status = ? WHERE user_phone = ?"""
        c = self.conn.cursor()
        c.execute(query, (status, user_phone))
        self.conn.commit()
