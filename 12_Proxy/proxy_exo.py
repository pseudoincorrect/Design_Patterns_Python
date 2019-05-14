class Person:
    def __init__(self, age):
        self.age = age

    def drink(self):
        return 'drinking'

    def drive(self):
        return 'driving'

    def drink_and_drive(self):
        return 'driving while drunk'


class ResponsiblePerson:
    def __init__(self, person):
        self.person = person

    @property
    def age(self):
        return self.person.age
        
    @age.setter 
    def age(self, age):
        self.person.age = age
        
    def drink(self):
        if self.person.age < 18:
            return "too young"
        else:
            return self.person.drink()

    def drive(self):
        if self.person.age < 16:
            return "too young"
        else:
            return self.person.drive()

    def drink_and_drive(self):
        return "dead"