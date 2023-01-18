#!/usr/bin/python
import AST

from SymbolTable import SymbolTable, VariableSymbol


operations_return_type_check = {
    '+': {
        ('int', 'int'): 'int',
        ('int', 'float'): 'float',
        ('float', 'int'): 'float',
        ('float', 'float'): 'float',
        ('vector', 'vector'): 'vector',
        ('str', 'str'): 'str',
    },
    '-': {
        ('int', 'int'): 'int',
        ('int', 'float'): 'float',
        ('float', 'int'): 'float',
        ('float', 'float'): 'float',
        ('vector', 'vector'): 'vector',
        ('str', 'str'): 'str',
    },
    '*': {
        ('int', 'int'): 'int',
        ('int', 'float'): 'float',
        ('float', 'int'): 'float',
        ('float', 'float'): 'float',
        ('vector', 'vector'): 'vector',
        ('str', 'int'): 'str',
        ('int', 'str'): 'str',
    },
    '/': {
        ('int', 'int'): 'int',
        ('int', 'float'): 'float',
        ('float', 'int'): 'float',
        ('float', 'float'): 'float',
        ('vector', 'vector'): 'vector',
    },
    '>': {
        ('int', 'int'): 'bool',
        ('int', 'float'): 'bool',
        ('float', 'int'): 'bool',
        ('float', 'float'): 'bool',
    },
    '<': {
        ('int', 'int'): 'bool',
        ('int', 'float'): 'bool',
        ('float', 'int'): 'bool',
        ('float', 'float'): 'bool',
    },
    '>=': {
        ('int', 'int'): 'bool',
        ('int', 'float'): 'bool',
        ('float', 'int'): 'bool',
        ('float', 'float'): 'bool',
    },
    '<=': {
        ('int', 'int'): 'bool',
        ('int', 'float'): 'bool',
        ('float', 'int'): 'bool',
        ('float', 'float'): 'bool',
    },
    '==': {
        ('int', 'int'): 'bool',
        ('int', 'float'): 'bool',
        ('float', 'int'): 'bool',
        ('float', 'float'): 'bool',
        ('bool', 'bool'): 'bool',
    },
    '!=': {
        ('int', 'int'): 'bool',
        ('int', 'float'): 'bool',
        ('float', 'int'): 'bool',
        ('float', 'float'): 'bool',
        ('bool', 'bool'): 'bool',
    },
    '.+': {
        ('int', 'int'): 'int',
        ('int', 'float'): 'float',
        ('float', 'int'): 'float',
        ('float', 'float'): 'float',
        ('str', 'str'): 'str',
    },
    '.-': {
        ('int', 'int'): 'int',
        ('int', 'float'): 'float',
        ('float', 'int'): 'float',
        ('float', 'float'): 'float',
    },
    '.*': {
        ('int', 'int'): 'int',
        ('int', 'float'): 'float',
        ('float', 'int'): 'float',
        ('float', 'float'): 'float',
    },
    './': {
        ('int', 'int'): 'int',
        ('int', 'float'): 'float',
        ('float', 'int'): 'float',
        ('float', 'float'): 'float',
    }
}


class NodeVisitor(object):
    def __init__(self):
        self.symbol_table = SymbolTable(None, "global")
        self.current_scope = self.symbol_table
        self.loop_indent = 0

    def visit(self, node):
        method = 'visit_' + node.__class__.__name__
        visitor = getattr(self, method, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):  # Called if no explicit visitor function exists for a node.
        if isinstance(node, list):
            for elem in node:
                self.visit(elem)
        else:
            for child in node.children:
                if isinstance(child, list):
                    for item in child:
                        if isinstance(item, AST.Node):
                            self.visit(item)
                elif isinstance(child, AST.Node):
                    self.visit(child)


class TypeChecker(NodeVisitor):

    def visit_Root(self, node: AST.Root):
        self.visit(node.instruction_node)

    def visit_Instructions(self, node: AST.Instructions):
        for instruction in node.instructions:
            self.visit(instruction)

    def visit_BinOpExpr(self, node: AST.BinOpExpr):
        # alternative usage,
        # requires definition of accept method in class Node
        type1 = self.visit(node.left)  # type1 = node.left.accept(self)
        type2 = self.visit(node.right)  # type2 = node.right.accept(self)
        op = node.op

        if (type1, type2) not in operations_return_type_check[op]:
            print(f"{node.lineno} Type error: {type1} {op} {type2} is not defined")
            return None

        if type1 == 'vector' or type2 == 'vector':
            if isinstance(node.left, AST.Id):
                left_dims = self.symbol_table.vector_dims[node.left.name]
            elif isinstance(node.left, AST.BinOpExpr):
                left_dims = node.left.vector_res_dims
            else:
                print("Unhandled case in TypeChecker.visit_BinOpExpr")
                exit(1)

            if isinstance(node.right, AST.Id):
                right_dims = self.symbol_table.vector_dims[node.right.name]
            elif isinstance(node.right, AST.BinOpExpr):
                right_dims = node.right.vector_res_dims
            else:
                print("Unhandled case in TypeChecker.visit_BinOpExpr")
                exit(1)

            for i in range(len(left_dims)):
                if left_dims[i] != right_dims[i]:
                    print(f"{node.lineno} Type error: Vector dimensions must be equal")
                    return None

            node.vector_res_dims = left_dims

        return operations_return_type_check[op][(type1, type2)]

    def visit_UniOpExprLeft(self, node: AST.UniOpExprLeft):
        return self.visit(node.left)

    def visit_UniOpExprRight(self, node: AST.UniOpExprRight):
        return self.visit(node.right)

    def visit_Id(self, node: AST.Id):
        return self.symbol_table.get(node.name)

    def visit_ValueInt(self, node: AST.ValueInt):
        return 'int'

    def visit_ValueFloat(self, node: AST.ValueFloat):
        return 'float'

    def visit_ValueStr(self, node: AST.ValueString):
        return 'str'

    def visit_If(self, node: AST.If):
        self.symbol_table = self.symbol_table.pushScope("if")

        self.visit(node.condition)
        self.visit(node.instruction)

        self.symbol_table = self.symbol_table.popScope()
        if node.instruction_else is not None:
            self.symbol_table = self.symbol_table.pushScope("else")
            self.visit(node.instruction_else)
            self.symbol_table = self.symbol_table.popScope()

    def visit_While(self, node: AST.While):
        self.symbol_table = self.symbol_table.pushScope("while")
        self.loop_indent += 1

        self.visit(node.condition)
        self.visit(node.instructions)

        self.symbol_table = self.symbol_table.popScope()
        self.loop_indent -= 1

    def visit_For(self, node: AST.For):
        self.symbol_table = self.symbol_table.pushScope("for")
        self.loop_indent += 1

        type1 = self.visit(node.start_val)
        type2 = self.visit(node.end_val)

        if type1 is None or type2 is None:
            print(f"{node.lineno} Type error: left operand type is not same as right")
            self.symbol_table.put(node.var_id.name, None)
        elif type1 != type2:
            print(f"{node.lineno} Type error: {type1} is not same as {type2}")
            self.symbol_table.put(node.var_id.name, None)
        else:
            self.symbol_table.put(node.var_id.name, type1)

        self.visit(node.instruction)
        self.symbol_table = self.symbol_table.popScope()
        self.loop_indent -= 1

    def visit_Return(self, node: AST.Return):
        return self.visit(node.value)

    def visit_Break(self, node: AST.Break):
        if self.loop_indent == 0:
            print(f"{node.lineno} Break outside of loop")

    def visit_Continue(self, node: AST.Continue):
        if self.loop_indent == 0:
            print(f"{node.lineno} Continue outside of loop")

    def visit_Print(self, node: AST.Print):
        for print_value in node.print_list:
            self.visit(print_value)

    def visit_Assignment(self, node: AST.Assignment):
        value_type = self.visit(node.value)

        if value_type is None:
            return None

        if node.op == '=':
            self.symbol_table.put(node.var_id.name, value_type)

            if value_type == 'vector':
                self.symbol_table.vector_dims[node.var_id.name] = node.value.dims
                self.symbol_table.vector_type[node.var_id.name] = node.value.vector_type
        else:
            # TODO - Dimensions of matrices
            var_type = self.symbol_table.get(node.var_id)

            if var_type == 'vector' and value_type == 'vector':
                var_dims = self.symbol_table.vector_dims[node.var_id.name]
                val_dims = node.value.dims

                if len(var_dims) != len(val_dims):
                    print(f"{node.lineno} Type error: {node.var_id.name} and {node.value} have different dimensions")
                    return None

                for i in range(len(var_dims)):
                    if var_dims[i] != val_dims[i]:
                        print(f"{node.lineno} Type error: {node.var_id.name} and {node.value} have different dimensions")
                        return None

            if (var_type, value_type) in operations_return_type_check:
                assign_type = operations_return_type_check[(var_type, value_type)]
                return assign_type
            else:
                print(f"{node.lineno} Type error: {var_type} {node.op} {value_type} is not defined")
                return None

    def visit_Vector(self, node: AST.Vector):
        if isinstance(node.elements[0], AST.Vector):
            dims = node.elements[0].dims
        elif isinstance(node.elements[0], list):
            dims = [len(node.elements[0])]
        else:
            dims = [1]

        for element in node.elements:
            if isinstance(element, AST.Vector):
                self.visit(element)
                element_dims = element.dims
            elif isinstance(element, list):
                element_dims = [len(element)]
            else:
                element_dims = [1]

            for i in range(len(dims)):
                if dims[i] != element_dims[i]:
                    print(f"{node.lineno} Type error: Vector size mismatch")
                    return None

    def visit_Ref(self, node: AST.Ref):
        dims = self.symbol_table.vector_dims[node.var_id.name]

        if len(dims) != len(node.indices):
            print(f"{node.lineno} Type error: Vector size mismatch")
            return None

        for i in range(len(node.indices)):
            if str(self.visit(node.indices[i])) != 'int':
                print(f"{node.lineno} Type error: Matrix index must be int")
                return None

            if node.indices[i].value >= dims[i].value:
                print(f"{node.lineno} Type error: Matrix index out of bounds")
                return None

        return self.symbol_table.vector_type[node.var_id.name]

    def visit_MatrixCreation(self, node: AST.MatrixCreation):
        for value in node.dims:
            if str(self.visit(value)) != 'int':
                print(f"{node.lineno} Type error: Matrix size must be int")
                return None
        return 'vector'

    def visit_MatrixFunction(self, node: AST.MatrixFunction):
        return

