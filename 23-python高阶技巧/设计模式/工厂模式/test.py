class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age):
        super().__init__(name, age)


class Teacher(Person):
    def __init__(self, name, age):
        super().__init__(name, age)


class Worker(Person):
    def __init__(self, name, age):
        super().__init__(name, age)


class PersonFactory:
    def get_person(self, p_type, name, age):
        if p_type == 'Student':
            return Student(name, age)
        elif p_type == 'Teacher':
            return Teacher(name, age)
        elif p_type == 'Worker':
            return Worker(name, age)


pf = PersonFactory()
stu = pf.get_person('Student', "richenyv", 18)
tea = pf.get_person('Teacher', "richenyv", 21)
worker = pf.get_person('Worker', "richenyv", 38)
print(f"{stu.name},{stu.age}")
print(f"{tea.name},{tea.age}")
print(f"{worker.name},{worker.age}")
