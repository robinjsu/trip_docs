class Model():
    def select(self):
        """
        Gets all entries from the database
        :return: list of dictionaries containing all rows of database
        """
        pass

    def select_one(self, id):
        """
        Retrieve a single database entry, based on rowid
        :param id: Integer
        """
        pass

    def insert(self, trip_details):
        """
        Inserts entry into database
        :param trip_details: dictionary of trip title, date range, and location information
        """
        pass

    def update(self, trip_details):
        """
        Updates existing entry in database, based on entry id.
        :param trip_details: dictionary of trip title, date range, location, and entry id
        """
        pass

    
