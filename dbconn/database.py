import sqlite3
import logging
import time
import sys

# sys.stdout = open('../log.txt', 'w')


class Database(logging.Handler):
    """sqlite3 database class that holds testers jobs"""
    DB_LOCATION = "../db.sqlite"

    def __init__(self):
        """Initialize db class variables"""
        logging.Handler.__init__(self)
        self.db = Database.DB_LOCATION
        self.connection = sqlite3.connect(self.db)
        self.cur = self.connection.cursor()

        self.log()

    def close(self):
        """close sqlite3 connection"""
        self.connection.close()

    def execute(self, query):
        """execute a row of data to current cursor"""
        self.cur.execute(query)

        self.log()

    def commit(self):
        """commit changes to database"""
        self.connection.commit()

        self.log()

    def log(self):
        self.connection.set_trace_callback(print)
