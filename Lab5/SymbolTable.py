#!/usr/bin/python

class Symbol:
    pass


class VariableSymbol(Symbol):

    def __init__(self, name, type):
        self.name = name
        self.type = type


class SymbolTable(object):

    def __init__(self, parent, name):
        self.parent_scope = parent
        self.name = name
        self.symbols = {}
        self.vector_dims = {}
        self.vector_type = {}

    def put(self, name, symbol):
        self.symbols[name] = symbol

    def get(self, name): # get variable symbol or fundef from <name> entry
        if name in self.symbols:
            return self.symbols[name]
        elif self.parent_scope is not None:
            return self.parent_scope.symbols[name]
        else:
            print("Symbol not found: " + name, f'Scope {self.name}: ', self.symbols)
            raise ValueError("Symbol not found")

    def getParentScope(self):
        return self.parent_scope

    def pushScope(self, name):
        return SymbolTable(self, name)

    def popScope(self):
        return self.parent_scope

