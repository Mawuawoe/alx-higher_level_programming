#!/usr/bin/python3
import sys

def add(args):
    try:
        total = 0
        for arg in args:
            total += int(arg)
        return(total)
    except ValueError:
        print("pls enter a valid number")

if __name__ == "__main__":
    args = sys.argv[1:]
    result = add(args)
    print("sum is: {}".format(result))