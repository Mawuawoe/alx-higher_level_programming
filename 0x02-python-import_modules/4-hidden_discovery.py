#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    all = dir()
    for i in all:
        if i[0] == '_' and i[1] == '_':
            continue
        else:
            print(i)
