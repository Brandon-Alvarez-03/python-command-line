from model import  Note
from flask import Flask, jsonify, request
from peewee import *
from playhouse.shortcuts import model_to_dict, dict_to_model

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
  note_list = []
  for note in Note.select():
    note_list.append(model_to_dict(note))
  return jsonify(note_list)
@app.route('/note/<id>', methods=['GET', 'PUT', 'DELETE'])
def endpoint(id=None):
  if request.method == 'GET':
    if id:
        return jsonify(model_to_dict(Note.get(Note.id == id)))
    else:
        note_list = []
        for note in Note.select():
            note_list.append(model_to_dict(note))
        return jsonify(note_list)

  if request.method =='PUT':
    body = request.get_json()
    Note.update(body).where(Note.id == id).execute()
    return "Note " + str(id) + " has been updated."

  if request.method == 'POST':
    new_note = dict_to_model(Note, request.get_json())
    new_note.save()
    return jsonify({"success": True})

  if request.method == 'DELETE':
    Note.delete().where(Note.id == id).execute()
    return "Note " + str(id) + " deleted."

app.run(debug=True, port=9000)

def note_taker():
  note_title = input("Note Title: ")
  note_msg = input("Type your note: ")

  new_note = Note(title=f"{note_title}", message=f"{note_msg}")
  new_note.save()
  
  all_notes = input("View notes? (y/n):  ")
  if all_notes.lower() == "y":
    print("\n    Here are all your notes!")
    for note in [model_to_dict(note) for note in Note.select()]:
      print(f"{note['title']}: {note['message']}")
  print("\n Goodbye!")


note_taker()
