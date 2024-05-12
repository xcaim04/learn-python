import unittest
class Estudiante:

    school = 'MIT'

    def __init__(self, name):
        self.name = name

    def _student_attendance(self, attendance) -> int:
        res = 3
        for mes, attendance in attendance.items():
            if attendance < 4:
                res = min(res, 1)
            elif 4 <= attendance < 8:
                res = min(res, 2)
            else: res = min(res, 3)
        return res

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

student = Estudiante('Carlos')

def test_1():
    attendance = {"Enero": 6, "Febrero": 3, "Marzo": 8}
    test = student.get_students_attendances(attendance)
    print(attendance, 'Value expected: 1 ', f'Value received: {test}')
    try:
        assert test == 1
        print('\t> Test 1: Accepted\n')
    except:
        print('\t> Test 1: Wrong Answer\n')

def test_2():
    attendance = {"Enero": 6, "Febrero": 10, "Marzo": 8}
    test = student.get_students_attendances(attendance)
    print(attendance, 'Value expected: 2 ', f'Value received: {test}')
    try:
        assert test == 2
        print('\t> Test 2: Accepted\n')
    except:
        print('\t> Test 2: Wrong Answer\n')

def test_3():
    attendance = {"Enero": 60, "Febrero": 10, "Marzo": 18}
    test = student.get_students_attendances(attendance)
    print(attendance, 'Value expected: 1 ', f'Value received: {test}')
    try:
        assert test == 3
        print('\t> Test 3: Accepted\n')
    except:
        print('\t> Test 3: Wrong Answer\n')

test_1()
test_2()
test_3()