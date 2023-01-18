from __future__ import print_function
import AST


def addToClass(cls):

    def decorator(func):
        setattr(cls, func.__name__, func)
        return func
    return decorator


class TreePrinter:

    @addToClass(AST.Node)
    def printTree(self, indent=0):
        raise Exception("printTree not defined in class " + self.__class__.__name__)

    @addToClass(AST.Error)
    def printTree(self, indent=0):
        pass
        # fill in the body

    @addToClass(AST.Root)
    def printTree(self: AST.Root, indent=0):
        self.instruction_node.printTree()

    @addToClass(AST.Instructions)
    def printTree(self: AST.Instructions, indent=0):
        for instruction in self.instructions:
            instruction.printTree()

    @addToClass(AST.Id)
    def printTree(self: AST.Id, indent=0):
        print('| ' * indent, self.name)

    @addToClass(AST.ValueInt)
    def printTree(self: AST.ValueInt, indent=0):
        print('| '*indent, self.value)

    @addToClass(AST.ValueFloat)
    def printTree(self: AST.ValueFloat, indent=0):
        print('| '*indent, self.value)

    @addToClass(AST.ValueString)
    def printTree(self: AST.ValueString, indent=0):
        print('| '*indent, self.value)

    @addToClass(AST.BinOpExpr)
    def printTree(self: AST.BinOpExpr, indent=0):
        print('| '*indent, self.op)
        self.left.printTree(indent+1)
        self.right.printTree(indent+1)

    @addToClass(AST.UniOpExprLeft)
    def printTree(self: AST.UniOpExprLeft, indent=0):
        print('| '*indent, 'TRANSPOSE')
        self.left.printTree(indent+1)

    @addToClass(AST.UniOpExprRight)
    def printTree(self: AST.UniOpExprRight, indent=0):
        print('| '*indent, self.op)
        self.right.printTree(indent+1)

    @addToClass(AST.Assignment)
    def printTree(self: AST.Assignment, indent=0):
        print('| '*indent, self.op)
        self.var_id.printTree(indent+1)
        self.value.printTree(indent+1)

    @addToClass(AST.If)
    def printTree(self: AST.If, indent=0):
        print('| '*indent, 'IF')
        self.condition.printTree(indent+1)
        print('| '*indent, 'THEN')
        self.instruction.printTree(indent+1)
        if self.instruction_else is not None:
            print('| '*indent, 'ELSE')
            self.instruction_else.printTree(indent+1)

    @addToClass(AST.While)
    def printTree(self: AST.While, indent=0):
        print('| '*indent, 'WHILE')
        self.condition.printTree(indent+1)
        for instruction in self.instructions:
            instruction.printTree(indent+1)

    @addToClass(AST.For)
    def printTree(self: AST.For, indent=0):
        print("| "*indent, 'FOR')
        self.var_id.printTree(indent+1)
        print("| "*(indent+1), 'RANGE')
        self.start_val.printTree(indent+2)
        self.end_val.printTree(indent+2)

        if isinstance(self.instruction, list):
            for instruction in self.instruction:
                instruction.printTree(indent+1)
        else:
            self.instruction.printTree(indent+1)

    @addToClass(AST.Return)
    def printTree(self: AST.Return, indent=0):
        print('| '*indent, 'RETURN')
        if not self.value is None:
            self.value.printTree(indent+1)

    @addToClass(AST.Break)
    def printTree(self: AST.Break, indent=0):
        pass

    @addToClass(AST.Continue)
    def printTree(self: AST.Continue, indent=0):
        pass

    @addToClass(AST.Print)
    def printTree(self: AST.Print, indent=0):
        print('| '*indent, 'PRINT')
        for element in self.print_list:
            element.printTree(indent+1)

    @addToClass(AST.Ref)
    def printTree(self: AST.Ref, indent=0):
        print('| '*indent, 'REF')
        self.var_id.printTree(indent+1)

        for index in self.indices:
            index.printTree(indent+1)
        # self.row.printTree(indent+1)
        # self.col.printTree(indent+1)

    @addToClass(AST.Vector)
    def printTree(self: AST.Vector, indent=0):
        print('| '*indent, 'VECTOR')
        for element in self.elements:
            try:
                element.printTree(indent+1)
            except AttributeError:
                print(self.elements)
                exit(-1)

    @addToClass(AST.MatrixFunction)
    def printTree(self: AST.MatrixFunction, indent=0):
        print('| '*indent, self.function)

    @addToClass(AST.MatrixCreation)
    def printTree(self: AST.MatrixCreation, indent=0):
        self.function.printTree(indent)

        for value in self.dims:
            value.printTree(indent+1)


    # define printTree for other classes
    # ...

