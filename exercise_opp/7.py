class Estudiante:

    def __init__(self, name) -> None:
        pass

    def calculate_media(self, list_notes, grade):
        self.grade = grade
        self.media = sum(list_notes) / len(list_notes)


if __name__ ==  '__main__':
    student = Estudiante("John")

    # Media arithmetic -> float
    student.calculate_media([2, 1, 3], '12th')

    print(student.grade, student.media)