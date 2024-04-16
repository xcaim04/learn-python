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
        return self.grade


Carlos = Estudiante('Carlos', 19, 12)
print(Carlos.name, Carlos.age, Carlos.grade)