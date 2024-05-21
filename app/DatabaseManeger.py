from mimetypes import init
from sqlite3 import connect

class DatabaseManeger:
    def __init__(self,path) -> None:
        self.path = path
        self.conn = self.init_conn()

    def init_db(self):
        with open(".app/tables.sql", "r") as tables:
            tables = tables.read()
        tables = tables.split(';')
    def init_conn(self):
        conn = connect(self.path)
        return conn