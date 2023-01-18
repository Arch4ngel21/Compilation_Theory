
class Node(object):
    def accept(self, visitor):
        return visitor.visit(self)


class Root(Node):
    def __init__(self, instruction_node, lineno):
        self.instruction_node = instruction_node
        self.lineno = lineno


class Instructions(Node):
    def __init__(self, instructions, lineno):
        self.instructions = instructions
        self.lineno = lineno


class BinOpExpr(Node):
    def __init__(self, op, left, right, lineno):
        self.op = op
        self.left = left
        self.right = right
        self.vector_res_dims = None
        self.lineno = lineno


class UniOpExprLeft(Node):
    def __init__(self, op, left, lineno):
        self.op = op
        self.left = left
        self.lineno = lineno


class UniOpExprRight(Node):
    def __init__(self, op, right, lineno):
        self.op = op
        self.right = right
        self.lineno = lineno


class Id(Node):
    def __init__(self, name, lineno):
        self.name = name
        self.lineno = lineno


class ValueInt(Node):
    def __init__(self, value, lineno):
        self.value = value
        self.lineno = lineno


class ValueFloat(Node):
    def __init__(self, value, lineno):
        self.value = value
        self.lineno = lineno


class ValueString(Node):
    def __init__(self, value, lineno):
        self.value = value
        self.lineno = lineno


class If(Node):
    def __init__(self, condition, instruction, instruction_else, lineno):
        self.condition = condition
        self.instruction = instruction
        self.instruction_else = instruction_else
        self.lineno = lineno


class While(Node):
    def __init__(self, condition, instructions, lineno):
        self.condition = condition
        self.instructions = instructions
        self.lineno = lineno


class For(Node):
    def __init__(self, var_id, start_val, end_val, instruction, lineno):
        self.var_id = var_id
        self.start_val = start_val
        self.end_val = end_val
        self.instruction = instruction
        self.lineno = lineno


class Return(Node):
    def __init__(self, value, lineno):
        self.value = value
        self.lineno = lineno


class Break(Node):
    def __init__(self, lineno):
        self.lineno = lineno


class Continue(Node):
    def __init__(self, lineno):
        self.lineno = lineno


class Print(Node):
    def __init__(self, print_list, lineno):
        self.print_list = print_list
        self.lineno = lineno


class Assignment(Node):
    def __init__(self, var_id, op, value, lineno):
        self.var_id = var_id
        self.value = value
        self.op = op
        self.lineno = lineno


class Vector(Node):
    def __init__(self, elements, lineno):
        self.elements = elements
        self.lineno = lineno
        self.dims = [len(elements)]
        self.vector_type = None

        if isinstance(elements[0], Vector):
            self.dims += elements[0].dims
        elif isinstance(elements[0], list):
            self.dims += [len(elements[0])]

        curr_dim = elements
        while isinstance(curr_dim, list) or isinstance(curr_dim, Vector):
            if isinstance(curr_dim, list):
                curr_dim = curr_dim[0]
            else:
                curr_dim = curr_dim.elements[0]

        if type(curr_dim) == int:
            self.vector_type = 'int'
        elif type(curr_dim) == float:
            self.vector_type = 'float'
        elif type(curr_dim) == str:
            self.vector_type = 'string'


class Ref(Node):
    def __init__(self, var_id, indices, lineno):
        self.var_id = var_id
        self.indices = indices
        self.lineno = lineno


class MatrixCreation(Node):
    def __init__(self, function, dims, lineno):
        self.function = function
        self.dims = dims
        self.lineno = lineno
        self.vector_type = 'float'


class MatrixFunction(Node):
    def __init__(self, function, lineno):
        self.function = function
        self.lineno = lineno


# ...
# fill out missing classes
# ...

class Error(Node):
    def __init__(self):
        pass
