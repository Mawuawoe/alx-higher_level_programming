1. Write a function that prints x number of elements of a list. 
-->my_list can contain any type (integer, string, etc.)
-->x represents the number of elements to print
-->x can be bigger than the length of my_list
--> Returns the real number of elements printed
--> You have to use try: / except:

2. Write a function that prints an integer with "{:d}".format().

-->Prototype: def safe_print_integer(value):
-->value can be any type (integer, string, etc.)
-->The integer should be printed followed by a new line
-->Returns True if value has been correctly printed (it means the value is an integer)
-->Otherwise, returns False
-->You have to use try: / except:
-->You have to use "{:d}".format() to print as integer
-->You are not allowed to import any module
-->You are not allowed to use type()

3. Write a function that prints the first x elements of a list and only integers.

Prototype: def safe_print_list_integers(my_list=[], x=0):
--> my_list can contain any type (integer, string, etc.)
--> All integers have to be printed on the same line followed by a new line - other type of value in the list must be skipped (in silence).
--> x represents the number of elements to access in my_list
--> x can be bigger than the length of my_list - if it’s the case, an exception is expected to occur
--> Returns the real number of integers printed
--> You have to use try: / except:
--> You have to use "{:d}".format() to print an integer
--> You are not allowed to import any module
--> You are not allowed to use len()

4. Write a function that divides 2 integers and prints the result.

--> Prototype: def safe_print_division(a, b):
--> You can assume that a and b are integers
--> The result of the division should print on the finally: section preceded by Inside result:
--> Returns the value of the division, otherwise: None
--> You have to use try: / except: / finally:
--> You have to use "{}".format() to print the result
--> You are not allowed to import any module