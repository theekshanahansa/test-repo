class Person:
    def __init__(self, name, age):
        self.__name = name  # Private attribute
        self.__age = age  # Private attribute

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age


# Creating an instance of the Person class
person = Person("Alice", 30)


# Accessing and modifying private attributes using getter and setter methods
print(person.get_name())  # Output: Alice
person.set_age(31)
print(person.get_age())  # Output: 31
