
class Node(object):
    pass


class Root(Node):
    def __init__(self, instruction_node):
        self.instruction_node = instruction_node


class Instructions(Node):
    def __init__(self, instructions):
        self.instructions = instructions


class BinOpExpr(Node):
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right


class UniOpExprLeft(Node):
    def __init__(self, op, left):
        self.op = op
        self.left = left


class UniOpExprRight(Node):
    def __init__(self, op, right):
        self.op = op
        self.right = right


class Value(Node):
    def __init__(self, value):
        self.value = value


class If(Node):
    def __init__(self, condition, instruction, instruction_else):
        self.condition = condition
        self.instruction = instruction
        self.instruction_else = instruction_else


class While(Node):
    def __init__(self, condition, instructions):
        self.condition = condition
        self.instructions = instructions


class For(Node):
    def __init__(self, var_id, start_val, end_val, instruction):
        self.var_id = var_id
        self.start_val = start_val
        self.end_val = end_val
        self.instruction = instruction


class Return(Node):
    def __init__(self, value):
        self.value = value


class Print(Node):
    def __init__(self, print_list):
        self.print_list = print_list


class Assignment(Node):
    def __init__(self, var_id, op, value):
        self.var_id = var_id
        self.value = value
        self.op = op


class Vector(Node):
    def __init__(self, elements):
        self.elements = elements


class Ref(Node):
    def __init__(self, var_id, row, col):
        self.var_id = var_id
        self.row = row
        self.col = col


class MatrixCreation(Node):
    def __init__(self, function, value):
        self.function = function
        self.value = value


class MatrixFunction(Node):
    def __init__(self, function):
        self.function = function


# ...
# fill out missing classes
# ...

class Error(Node):
    def __init__(self):
        pass
