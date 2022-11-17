# python-command-line-note-taker

## Model/Schema

- Running model.py connects to the PostgreSQL database and updates the schema for entering new notes

## Seeding

- Running seed.py connects to the PostgreSQL database and seeds several example notes for the user to view

## Using the app via command line

- Running notes_command_line.py takes new notes via CLI inputs and allows user to view their notes int he command line

## Using the browser to view notes as json files

- Flask was implemented using peewee and playhouse shortcuts to enable the user to view their notes in the browser
- by running notes-browser.py the user will have all notes presented by default and can view individual notes using endpoint ```'/note/<id>'```

