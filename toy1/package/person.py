class Person:
    _NO_NAME = 'UNKNOWN'
    _NO_AGE = -1

    def get_no_name(self):
        return self._NO_NAME

    def get_no_age(self):
        return self._NO_AGE

    def __init__(self, name, age):
        if name and isinstance(name, str) and len(name) > 0:
            self.name = name
        else:
            self.name = Person._NO_NAME

        if age and isinstance(age, int) and age > 0:
            self.age = age
        else:
            self.age = Person._NO_AGE

    def __str__(self):
        return "My name is " + self.name + " and my age is " + str(self.age)
