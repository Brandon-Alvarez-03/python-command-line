from peewee import *

db = PostgresqlDatabase('notes', user='brandonalvarez', password='', host='localhost', port=5432)

class BaseModel(Model):
  class Meta:
    database = db

class Note(BaseModel):
  title = CharField()
  note = CharField()