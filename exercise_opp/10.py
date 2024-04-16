class Estudiante:

    school = 'MIT'

    def __init__(self, name):
        self.name = name

    def _student_attendance(self, attendance) -> int:
        for mes, attendance in attendance.items():
            if attendance < 4:
                return 1
            elif 4 <= attendance < 8:
                return 2
            return 3

    # Encapsulacion del metodo privado
    def get_students_attendances(self, list_subject_attendances) -> int:
        return self._student_attendance(list_subject_attendances)

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
    asistencias1 = {"Enero": 3, "Febrero": 6, "Marzo": 8}

    attendance = student.get_students_attendances(asistencias1)
    print(attendance)