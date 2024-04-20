from note import Note
from note_manager import NoteManager
from ui import UI
from datetime import datetime

class NoteApp:
    def __init__(self, file_path):
        self.note_manager = NoteManager(file_path)

    def add_note(self):
        title, body = UI.input_note_details()
        timestamp = datetime.now().isoformat()
        note_id = len(self.note_manager.load_notes()) + 1
        note = Note(note_id, title, body, timestamp, timestamp)
        notes = self.note_manager.load_notes()
        notes.append(note)
        self.note_manager.save_notes(notes)
        print("Заметка успешно добавлена!")

    def view_notes(self):
        notes = self.note_manager.load_notes()
        UI.display_notes(notes)

    def edit_note(self):
        note_id = UI.input_note_id()
        note = self.note_manager.get_note_by_id(note_id)
        if note:
            print(f"Текущая заметка {note.id}:")
            print(f"Заголовок: {note.title}")
            print(f"Текст: {note.body}")
            print(f"Дата создания: {note.timestamp}")
            print(f"Дата последнего изменения: {note.last_modified}")

            new_title, new_body = UI.input_note_details()
            if new_title or new_body:
                note.title = new_title if new_title else note.title
                note.body = new_body if new_body else note.body
                note.last_modified = datetime.now().isoformat()
                self.note_manager.save_notes(self.note_manager.load_notes())
                print("Заметка успешно отредактирована!")
            else:
                print("Изменения не внесены.")
        else:
            print("Заметка с указанным ID не найдена.")

    def delete_note(self):
        note_id = UI.input_note_id()
        notes = self.note_manager.load_notes()
        for note in notes:
            if note.id == note_id:
                notes.remove(note)
                self.note_manager.save_notes(notes)
                print("Заметка успешно удалена!")
                return
        print("Заметка с указанным ID не найдена.")

    def view_note_by_id(self):
        note_id = UI.input_note_id()
        note = self.note_manager.get_note_by_id(note_id)
        if note:
            print(f"Заметка {note.id}:")
            print(f"Заголовок: {note.title}")
            print(f"Текст: {note.body}")
            print(f"Дата создания: {note.timestamp}")
            print(f"Дата последнего изменения: {note.last_modified}")
        else:
            print("Заметка с указанным ID не найдена.")

    def run(self):
        while True:
            print("\nВыберите действие:")
            print("1. Добавить заметку")
            print("2. Просмотреть все заметки")
            print("3. Редактировать заметку")
            print("4. Удалить заметку")
            print("5. Просмотреть отдельную заметку по ID")
            print("6. Выход")
            choice = input("Ваш выбор: ")

            if choice == '1':
                self.add_note()
            elif choice == '2':
                self.view_notes()
            elif choice == '3':
                self.edit_note()
            elif choice == '4':
                self.delete_note()
            elif choice == '5':
                self.view_note_by_id()
            elif choice == '6':
                print("Выход из программы.")
                break
            else:
                print("Некорректный ввод. Попробуйте еще раз.")

if __name__ == "__main__":
    app = NoteApp('notes.json')
    app.run()
