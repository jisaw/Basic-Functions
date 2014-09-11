""" define the following functions
... getValue()
... read an integer input from console and assign to local variable"""
def getValue():
    intInputValue = input("Please insert an integer value: ")
    return int(intInputValue)

"""
... validateValue(value)
... validate the value to be number"""
def validateValue(value):
    if isinstance(value, int):
        return True
    else:
        print("The number you entered is not of type Integer")
        return False
"""
... findArea(var1, var2)
... var1 and var2 are values collected from console and validated
... return the product of var1 and var2 as area
"""
def findArea(var1, var2):
    return var1 * var2
"""
...
...create the functions, save as modules, import the module and test.
"""