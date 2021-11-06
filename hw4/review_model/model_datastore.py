from .Model import Model
from google.cloud import datastore

KIND = 'CourseReview'
PROJECT = 'cloud-f21-robin-su-robisu'

class model(Model):
    def __init__(self):
        self.client = datastore.Client(PROJECT)

    def select(self):
        query_kind = self.client.query(kind=KIND)
        query_iter = query_kind.fetch()
        entries = []
        for item in query_iter:
            entry = [item['name'], item['number'], item['dept'], item['quarter'], item['year'], item['instructor'], item['rating'], item['review'], item.key.id]
            entries.append(entry)
    
        return entries
        
    def select_one(self, id):      
        key =self.client.key(KIND, int(id))
        review = self.client.get(key)

        entry = [review['name'], review['number'], review['dept'], review['quarter'], review['year'], review['instructor'], review['rating'], review['review'], review.key.id]

        return entry
        

    def insert(self, name, number, dept, quarter, year, instructor, rating, review):
        key = self.client.key(KIND)
        course = datastore.Entity(key)
        course.update(
            {
                'name': name,
                'number': number,
                'dept': dept,
                'quarter': quarter,
                'year': year,
                'instructor': instructor,
                'rating': rating,
                'review': review
            }
        )
        self.client.put(course)

        return True
        

    def update(self, id, name, number, dept, quarter, year, instructor, rating, review):
        key = self.client.key(KIND, int(id))
        entity = datastore.Entity(key)
        entity.update(
            {
                'name': name,
                'number': number,
                'dept': dept,
                'quarter': quarter,
                'year': year,
                'instructor': instructor,
                'rating': rating,
                'review': review
            }
        )

        self.client.put(entity)

        return True