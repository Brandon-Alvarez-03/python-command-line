from model import db, Note
from peewee import *

db.connect()

db.drop_tables([Note])
db.create_tables([Note])

Note(title='Example Shopping List', note='Eggs, Bacon, Pancake mix, milk, love').save()
Note(title='Example Bacon Pancake Recipe', note='Cook eggs, bacon, and pancakes').save()
Note(title='Example To Do List', note='Make bacon pancakes').save()