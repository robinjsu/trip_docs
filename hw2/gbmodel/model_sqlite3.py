"""
A basic web application for submitting and reading course reviews.
Uses a Flask MVP framework, with sqlite3 as a database backend 
supporting create and read operations with update and delete as stretch goals.

"""
from datetime import date
from .Model import Model
import sqlite3
DB_FILE = 'entries.db'    # file for our Database

class model(Model):
    def __init__(self):
        # Make sure our database exists
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        try:
            cursor.execute("select count(rowid) from reviews")
        except sqlite3.OperationalError:
            cursor.execute("create table reviews (name, number, dept, quarter, year, instructor, rating, review)")
        cursor.close()

    def select(self):
        """
        Gets all rows from the database
        Each row contains: name, number, dept, quarter, year, instructor, rating, review
        :return: List of lists containing all rows of database
        """
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM reviews")
        return cursor.fetchall()

    def insert(self, name, number, dept, quarter, year, instructor, rating, review):
        """
        Inserts entry into database
        :param name: String
        :param number: String
        :param dept: String
        :param rating: Integer
        :param quarter: String
        :param year: Integer
        :param instructor: String
        :param review: String
        :return: none
        :raises: Database errors on connection and insertion
        """
        params = {'name':name, 'number':number, 'dept':dept, 'quarter':quarter, 'year':year, 'instructor': instructor, 'rating':rating, 'review':review}
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("insert into reviews (name, number, dept, quarter, year, instructor, rating, review) VALUES (:name, :number, :dept, :quarter, :year, :instructor, :rating, :review)", params)

        connection.commit()
        cursor.close()
        return True
