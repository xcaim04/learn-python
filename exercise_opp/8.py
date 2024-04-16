class Estudiante:

    def __init__(self, name) -> None:
        pass

    def calculate_media(self, list_notes, grade):
        self.grade = grade
        self.media = sum(list_notes) / len(list_notes)

    @staticmethod
    def filter_notes(notes):
        for subject, note in notes.items():
            if note < 5:
                print(f"Subject: {subject}, Note: {note}")


if __name__ ==  '__main__':
    student = Estudiante("John")
    notes = {"Matemáticas": 6, "Historia": 3, "Ciencias": 7, "Literatura": 4}
    student.filter_notes(notes)