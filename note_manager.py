import json
from note import Note

class NoteManager:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_notes(self):
        try:
            with open(self.file_path, 'r') as file:
                data = json.load(file)
                return [Note(note_id=note_data["id"],
                             title=note_data["title"],
                             body=note_data["body"],
                             timestamp=note_data["timestamp"],
                             last_modified=note_data["last_modified"]) for note_data in data]
        except FileNotFoundError:
            return []

    def save_notes(self, notes):
        data = [vars(note) for note in notes]
        with open(self.file_path, 'w') as file:
            json.dump(data, file, indent=4)

    def get_note_by_id(self, note_id):
        notes = self.load_notes()
        for note in notes:
            if note.id == note_id:
                return note
        return None
