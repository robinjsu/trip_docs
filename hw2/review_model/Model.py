class Model():
    def select(self):
        """
        Gets all entries from the database
        :return: Tuple containing all rows of database
        """
        pass

    def insert(self, name, number, dept, rating, quarter, year, instructor, review):
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
        pass

    def update(self, id, name, number, dept, rating, quarter, year, instructor, review):
        """
        Updates existing entry in database, based on entry id.
        :param id: Integer
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
        pass

    