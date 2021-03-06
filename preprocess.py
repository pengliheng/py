import re
import ast
import astunparse


def warp_function(code):
    """
    case 1:
    input
    F_MT700_7 = Field('F_MT700_7')
    return inEmpty(F_MT700_7)

    output
    def warp_function():
        F_MT700_7 = Field('F_MT700_7')
        return inEmpty(F_MT700_7)

    @param {string} code
    @return {string}
    """
    tree = ast.parse(code)
    temp = tree.body
    tree.body = [ast.parse('def warp_function():\ta')]
    tree.body[0].body[0].body = temp
    return astunparse.unparse(tree)


def un_warp_function(code):
    """
    case 1:
    input
    def warp_function():
        F_MT700_7 = Field('F_MT700_7')
        return inEmpty(F_MT700_7)

    output
    F_MT700_7 = Field('F_MT700_7')
    return inEmpty(F_MT700_7)

    @param {string} code
    @return {string}
    """
    tree = ast.parse(code)
    tree.body = tree.body[0].body
    return astunparse.unparse(tree)


def remove_field_declaration(code):
    """
    case 1:
    input
    F_MT700_7 = Field('F_MT700_7')
    return inEmpty(F_MT700_7)

    output
    return inEmpty(F_MT700_7)

    @param {string} code
    @return {string}
    """
    tree = ast.parse(code)
    analyzer = Analyzer()
    analyzer.visit(tree)

    def filter_node(node):
        return not(isinstance(node, ast.Assign) and node.targets[0].id in analyzer.name)
    tree.body = filter(filter_node, tree.body)
    return astunparse.unparse(tree)


def add_field_declaration(code):
    """
    case 1:
    input
    return inEmpty(F_MT700_7)

    output
    F_MT700_7 = Field('F_MT700_7')
    return inEmpty(F_MT700_7)

    @param {string} code
    @return {string}
    """
    tree = ast.parse(code)
    analyzer = Analyzer()
    analyzer.visit(tree)
    for field in analyzer.name:
        tree.body.insert(0, ast.parse('%s = Field("%s")'%(field, field)).body[0])
    return astunparse.unparse(tree)


class Analyzer(ast.NodeVisitor):
    def __init__(self):
        self.name = []

    def visit_Name(self, node):
        if re.match(r"((AINS)|(BINS)|F)_\w+_\w+", node.id):
            self.name.append(node.id)
