#!/usr/bin/python3
class Myclass:
    class_var = 10
    def __init__(self, x):
        self.x = x

obj = Myclass(20)
print(Myclass.__dict__)
print(obj.__dict__)