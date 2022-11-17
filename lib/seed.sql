TRUNCATE TABLE notes;

ALTER SEQUENCE notes_id_seq RESTART WITH 1;

-- Example Notes
INSERT INTO notes(title, note) VALUES ('Example Shopping List', 'Eggs, Bacon, Pancake mix');
INSERT INTO notes(title, note) VALUES ('Example Bacon Pancake Recipe', 'Cook eggs, bacon, and pancakes');
INSERT INTO notes(title, note) VALUES ('Example To Do List', 'Make bacon pancakes');