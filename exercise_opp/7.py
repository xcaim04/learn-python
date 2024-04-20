class Estudiante:


    def __init__(self, name, age, grade) -> None:
        self.name = name
        self.age = age
        self.grade = grade

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_grade(self):
        return f'Carlos\' note: {self.grade}'

    def update_grade(self, rantings) -> None:
        self.grade = sum(rantings) / len(rantings)

if __name__ == '__main__':

    student = Estudiante("Carlos", 18, 9)
    student.update_grade([8.2, 9, 10, 9, 7.5, 8, 8.5])
    print(student.get_grade())