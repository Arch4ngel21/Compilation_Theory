import sys
import ply.yacc as yacc
from Mparser import parser, scanner
from TreePrinter import TreePrinter
from TypeChecker import TypeChecker

if __name__ == '__main__':

    try:
        filename = sys.argv[1] if len(sys.argv) > 1 else "opers.txt"
        file = open(filename, "r")
    except IOError:
        print("Cannot open {0} file".format(filename))
        sys.exit(0)

    # Mparser = Mparser()
    # parser = yacc.yacc(module=Mparser)
    text = file.read()

    ast = parser.parse(text, lexer=scanner.lexer)
    # ast.printTree()

    # Below code shows how to use visitor
    typeChecker = TypeChecker()
    typeChecker.visit(ast)  # or alternatively ast.accept(typeChecker)
