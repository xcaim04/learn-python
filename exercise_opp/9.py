class Estudiante:

    school = 'MIT'

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_school(cls, school_name):
        cls.school = school_name

    @staticmethod
    def filter_notes(notes):
        for subject, note in notes.items():
            if note < 5:
                print(f"Subject: {subject}, Note: {note}")

    def calculate_media(self, list_notes, grade):
        self.grade = grade
        self.media = sum(list_notes) / len(list_notes)


if __name__ ==  '__main__':

    student = Estudiante("John")
    print(student.school)

    Estudiante.change_school("Harvard")

    student1 = Estudiante("Carlos")
    print(student1.school)