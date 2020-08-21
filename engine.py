# this file to parse the code and return whether true or false
import ast


class Field():
    def __init__(self, name):
        self.name = name
        self.value = 'there is no attention'


def isIncluded(field, string):
    return field.value.contains(string)


def run(code):
    a = yield exec(code, globals())
    print(a)
    return a
