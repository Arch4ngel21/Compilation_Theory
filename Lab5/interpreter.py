
import AST
import SymbolTable
from memory import *
from exceptions import  *
from visit import *
import sys

sys.setrecursionlimit(10000)


def mat_add(a, b):
    for i in range(len(a)):
        for j in range(len(a[0])):
            a[i][j] += b[i][j]


def mat_sub(a, b):
    for i in range(len(a)):
        for j in range(len(a[0])):
            a[i][j] -= b[i][j]


def mat_mul(a, b):
    for i in range(len(a)):
        for j in range(len(a[0])):
            a[i][j] *= b[i][j]


def mat_div(a, b):
    for i in range(len(a)):
        for j in range(len(a[0])):
            a[i][j] /= b[i][j]


def transpose(a):
    return [[a[j][i] for j in range(len(a))] for i in range(len(a[0]))]


operations = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y,
    '<': lambda x, y: x < y,
    '>': lambda x, y: x > y,
    '<=': lambda x, y: x <= y,
    '>=': lambda x, y: x >= y,
    '==': lambda x, y: x == y,
    '!=': lambda x, y: x != y,
    '.+': lambda x, y: mat_add(x, y),
    '.-': lambda x, y: mat_sub(x, y),
    '.*': lambda x, y: mat_mul(x, y),
    './': lambda x, y: mat_div(x, y)
}


class Interpreter(object):
    @on('node')
    def visit(self, node):
        pass

    @when(AST.Root)
    def visit(self, node: AST.Root):
        self.memory = MemoryStack()
        self.memory.push('global')
        node.instruction_node.accept(self)

    @when(AST.Instructions)
    def visit(self, node: AST.Instructions):
        for instruction in node.instructions:
            instruction.accept(self)

    @when(AST.BinOpExpr)
    def visit(self, node: AST.BinOpExpr):
        r1 = node.left.accept(self)
        r2 = node.right.accept(self)

        # print(r1, node.op, r2, 'memory:', self.memory.stack[-1].memory)
        return operations[node.op](r1, r2)

    @when(AST.UniOpExprLeft)
    def visit(self, node: AST.UniOpExprLeft):
        r1 = node.left.accept(self)
        return transpose(r1)

    @when(AST.UniOpExprRight)
    def visit(self, node: AST.UniOpExprRight):
        r2 = node.right.accept(self)
        return -r2

    @when(AST.Id)
    def visit(self, node: AST.Id):

        return self.memory.get(node.name)

    @when(AST.ValueInt)
    def visit(self, node: AST.ValueInt):
        return int(node.value)

    @when(AST.ValueFloat)
    def visit(self, node: AST.ValueFloat):
        return float(node.value)

    @when(AST.ValueString)
    def visit(self, node: AST.ValueString):
        return str(node.value)

    @when(AST.If)
    def visit(self, node: AST.If):
        condition = node.condition.accept(self)
        if condition:
            self.memory.push('if')
            for instruction in node.instruction:
                instruction.accept(self)
            self.memory.pop()
        else:
            if node.instruction_else:
                self.memory.push('else')
                node.instruction_else.accept(self)
                self.memory.pop()

    @when(AST.While)
    def visit(self, node: AST.While):
        self.memory.push("while")
        while node.condition.accept(self):
            try:
                if isinstance(node.instructions, list):
                    for instruction in node.instructions:
                        instruction.accept(self)
                else:
                    node.instructions.accept(self)
            except ContinueException:
                continue
            except BreakException:
                break
        self.memory.pop()

    @when(AST.For)
    def visit(self, node: AST.For):
        iterator = node.var_id
        start = node.start_val.accept(self)
        end = node.end_val.accept(self)
        self.memory.push("for")
        self.memory.set(iterator.name, start)
        while self.memory.get(iterator.name) <= end:
            try:
                if isinstance(node.instruction, list):
                    for instruction in node.instruction:
                        instruction.accept(self)
                else:
                    node.instruction.accept(self)
            except ContinueException:
                continue
            except BreakException:
                break
            finally:
                self.memory.set(iterator.name, self.memory.get(iterator.name) + 1)
        self.memory.pop()

    @when(AST.Return)
    def visit(self, node: AST.Return):
        raise ReturnValueException(node.value.accept(self))

    @when(AST.Break)
    def visit(self, node: AST.Break):
        raise BreakException()

    @when(AST.Continue)
    def visit(self, node: AST.Continue):
        raise ContinueException

    @when(AST.Print)
    def visit(self, node: AST.Print):
        to_print = [element.accept(self) for element in node.print_list]
        print(*to_print, sep=' ')

    @when(AST.Assignment)
    def visit(self, node: AST.Assignment):
        if not isinstance(node.value, AST.Ref):
            if node.op == '=':
                self.memory.set(node.var_id.name, node.value.accept(self))
            else:
                self.memory.set(node.var_id.name, operations[node.op[0]](self.memory.get(node.var_id.name), node.value.accept(self)))
        else:
            matrix = self.memory.get(node.var_id.name)
            x = node.value.indices[0].accept(self)
            y = node.value.indices[1].accept(self)

            if node.op == '=':
                matrix[x][y] = node.value.accept(self)
            else:
                matrix[x][y] = operations[node.op[0]](matrix[x][y], node.value.accept(self))

            self.memory.set(node.var_id.name, matrix)
        # print(f'after {node.var_id.name} assignment:', self.memory.stack[-1].memory)

    @when(AST.Vector)
    def visit(self, node: AST.Vector):
        return [element.accept(self) for element in node.elements]

    @when(AST.Ref)
    def visit(self, node: AST.Ref):
        matrix = self.memory.get(node.var_id.name)

        # Tylko dla macierzy 2x2
        x = node.indices[0].accept(self)
        y = node.indices[1].accept(self)

        return matrix[x][y]

    @when(AST.MatrixCreation)
    def visit(self, node: AST.MatrixCreation):
        func = node.function.accept(self)
        args = [dim.accept(self) for dim in node.dims]

        # Tylko dla macierzy 2x2
        if func == 'zeros':
            if len(args) == 2:
                return [[0 for _ in range(args[0])] for _ in range(args[1])]
            else:
                return [0 for _ in range(args[0])]
        elif func == 'ones':
            if len(args) == 2:
                return [[1 for _ in range(args[0])] for _ in range(args[1])]
            else:
                return [1 for _ in range(args[0])]
        elif func == 'eye':
            if len(args) == 2:
                return [[1 if i == j else 0 for i in range(args[0])] for j in range(args[0])]
            else:
                return [1 for _ in range(args[0])]

    @when(AST.MatrixFunction)
    def visit(self, node: AST.MatrixFunction):
        return node.function

