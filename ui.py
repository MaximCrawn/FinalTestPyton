class UI:
    @staticmethod
    def display_notes(notes):
        for note in notes:
            print(f"{note.id}. {note.title} - {note.timestamp}")

    @staticmethod
    def input_note_details():
        title = input("Введите заголовок заметки: ")
        body = input("Введите текст заметки: ")
        return title, body

    @staticmethod
    def input_note_id():
        return int(input("Введите ID заметки: "))
