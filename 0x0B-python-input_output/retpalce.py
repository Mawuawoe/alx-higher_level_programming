#!/usr/bin/python3
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    def __str__(self):
        return self.__class__.__name__
    def reloead_from_json(self, json_data):
        for key, value in json_data.items():
            if hasattr(self, key):
                setattr(self, key, value)
            else:
                raise AttributeError

Alice = Student("Alice", 12, "3rd")
print((Alice))
print(Alice.__dict__)
print(getattr(Alice, "age"))
json_data = {"name": "Bob", "age": 16, "grade": "A"}
Alice.reloead_from_json(json_data)
print((Alice))
print(Alice.__dict__)
print(getattr(Alice, "age"))