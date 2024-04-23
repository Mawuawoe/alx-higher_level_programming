#!/usr/bin/python3
"""
This is a class Student that defines a student
"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Return the __dict__ of an object
        """
        if (type(attrs) is list and
                all(type(ele) is str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs
                    if hasattr(self, k)}

        return self.__dict__

    def reload_from_json(self, json):
        "this is a mothod that replaces all attributes of a student obj"
        for key, value in json.items():
            setattr(self, key, value)
