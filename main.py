class Person:
    def __init__(self, name, age):
 main-modifier-branch-01
        self.__name = name
        self.__age = age


    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age

            
person = Person("Theekshana", 30)

print(person.get_name())
person.set_age(31)
print(person.get_age())

