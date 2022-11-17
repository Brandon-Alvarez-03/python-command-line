from model import  Note
from peewee import *
from playhouse.shortcuts import model_to_dict, dict_to_model

def note_taker():
  note_title = input("Note Title: ")
  note_msg = input("Type your note: ")

  new_note = Note(title=f"{note_title}", note=f"{note_msg}")
  new_note.save()
  
  all_notes = input("View notes? (y/n):  ")
  if all_notes.lower() == "y":
    print("\n    Here are all your notes!")
    for note in [model_to_dict(note) for note in Note.select()]:
      print(f"{note['title']}: {note['note']}")
  print("\n Goodbye!")


note_taker()