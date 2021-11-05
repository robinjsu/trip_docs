from .Model import Model
from google.cloud import datastore

class model(Model):
    def __init__(self):
        self.client = datastore.Client('cloud-f21-robin-su-robisu')

    def select(self):
        pass
    
    def select_one(self, id):
        pass

    def insert(self, name, number, dept, quarter, year, instructor, rating, review):
        pass

    def update(self, name, number, dept, quarter, year, instructor, rating, review):
        pass
