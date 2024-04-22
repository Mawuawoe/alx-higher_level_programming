#!/usr/bin/python3
class Myclass:
    def __init__(self, x):
        self.x = x

obj = Myclass(10)
print(hasattr(obj, 'x'))
print(hasattr(obj, 'y'))