#!/usr/bin/python

import lab1 as scanner
import ply.yacc as yacc

from AST import *

tokens = scanner.tokens

precedence = (
    ("nonassoc", 'IFX'),
    ("nonassoc", 'ELSE'),

    ("left", '=', 'ADDASSIGN', 'SUBASSIGN', 'MULASSIGN', 'DIVASSIGN'),
    ("nonassoc", 'LESSEQ', 'MOREEQ', 'NOTEQUAL', 'EQUAL', '<', '>'),

    ("left", '+', '-', 'DOTADD', 'DOTSUB'),
    ("left", '*', '/', 'DOTMUL', 'DOTDIV'),

    ("left", "'"),
    ("right", 'UMINUS'),
)


symtab = {}


def p_error(p):
    if p:
        print("Syntax error at line {0}: LexToken({1}, '{2}')".format(p.lineno, p.type, p.value))
    else:
        print("Unexpected end of input")


def p_program(p):
    """program : instructions_opt"""
    p[0] = Root(p[1])


def p_instructions_opt_1(p):
    """instructions_opt : instructions """
    p[0] = Instructions(p[1])


def p_instructions_opt_2(p):
    """instructions_opt : """


def p_instructions_1(p):
    """instructions : instructions instruction
                    | instruction"""

    if len(p) == 2:
        if p[1] is None:
            p[0] = None
        else:
            p[0] = [p[1]]

    elif len(p) == 3:
        if not p[1] is None:
            p[0] = p[1] + [p[2]]
        else:
            p[0] = [p[2]]


def p_instructions_2(p):
    """instruction : '{' instructions '}' """
    p[0] = p[2]


def p_instruction_3(p):
    """instruction : if
                   | return ';'
                   | BREAK ';'
                   | CONTINUE ';'
                   | for_loop
                   | while_loop
                   | assignment ';'
                   | print"""
    p[0] = p[1]


def p_if(p):
    """if : IF '(' expression ')' instruction %prec IFX
          | IF '(' expression ')' instruction ELSE instruction"""

    if len(p) == 8:
        p[0] = If(p[3], p[5], p[7])
    else:
        p[0] = If(p[3], p[5], None)


def p_while(p):
    """while_loop : WHILE '(' expression ')' instruction """

    if len(p) == 6:
        p[0] = While(p[3], p[5])
    else:
        if type(p[6]) is list:
            p[0] = While(p[3], p[6])
        else:
            p[0] = While(p[3], list(p[6]))


def p_for(p):
    """for_loop : FOR ID '=' expression ':' expression instruction"""

    p[0] = For(Value(p[2]), p[4], p[6], p[7])


def p_return(p):
    """return : RETURN expression
              | RETURN"""

    if len(p) == 3:
        p[0] = Return(p[2])
    else:
        p[0] = Return(None)


def p_print(p):
    """print : PRINT '(' list_for_print ')' ';'
             | PRINT list_for_print ';'"""

    if p[2] == '(':
        p[0] = Print(p[3])
    else:
        p[0] = Print(p[2])


def p_list_for_print(p):
    """list_for_print : expression ',' list_for_print
                      | expression"""
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]


def p_expression_obj(p):
    """expression : var
                  | '(' expression ')'
                  | INTNUM
                  | FLOATNUM
                  | STRING"""
    if isinstance(p[1], Value.__class__):
        p[0] = p[1]
    else:
        p[0] = Value(p[1])


def p_expression_var(p):
    """var : ID"""
    p[0] = Value(p[1])


def p_expression_ref(p):
    """var : ID '[' expression ',' expression ']' """
    p[0] = Ref(Value(p[1]), p[3], p[5])


def p_expression_assignment(p):
    """assignment : var '=' expression
                  | var ADDASSIGN expression
                  | var SUBASSIGN expression
                  | var MULASSIGN expression
                  | var DIVASSIGN expression"""
    p[0] = Assignment(p[1], p[2], p[3])


def p_expression_uniop_left(p):
    """expression : expression "'" """
    if isinstance(p[1], Value.__class__):
        p[0] = UniOpExprLeft(p[2], p[1])
    else:
        p[0] = UniOpExprLeft(p[2], Value(p[1]))


def p_expression_uniop_right(p):
    """expression : '-' expression %prec UMINUS"""
    if isinstance(p[2], Value.__class__):
        p[0] = UniOpExprRight(p[1], p[2])
    else:
        p[0] = UniOpExprRight(p[1], Value(p[2]))


def p_expression_binop(p):
    """expression : expression '+' expression
                  | expression '-' expression
                  | expression '*' expression
                  | expression '/' expression

                  | expression DOTADD expression
                  | expression DOTSUB expression
                  | expression DOTMUL expression
                  | expression DOTDIV expression

                  | expression '<' expression
                  | expression '>' expression
                  | expression LESSEQ expression
                  | expression MOREEQ expression
                  | expression EQUAL expression
                  | expression NOTEQUAL expression
                  """

    p[0] = BinOpExpr(p[2], p[1], p[3])


def p_expression_matrix(p):
    """expression : matrix """
    p[0] = p[1]


def p_matrix(p):
    """matrix : '[' matrix ']'
              | '[' sub_string_1 ']'
              | '[' sub_string_1 ',' matrix ']' """
    if len(p) == 4:
        p[0] = Vector(p[2])
    elif len(p) == 6:
        p[0] = Vector(p[2] + [p[4]])
    else:
        print('ERROR - matrix')
        exit(-1)


def p_sub_matrix(p):
    """sub_string_1 : sub_string_1 ',' expression
                    | expression"""
    if len(p) == 4:
        p[0] = p[1] + [p[3]]
    elif len(p) == 2:
        p[0] = [p[1]]
    else:
        print('ERROR - submatrix')
        exit(-1)


def p_matrix_creation_1(p):
    """expression : matrix_creation '(' expression ')' """
    p[0] = MatrixCreation(p[1], p[3])


def p_matrix_creation(p):
    """matrix_creation : ZEROS
                       | ONES
                       | EYE"""

    p[0] = MatrixFunction(p[1])


parser = yacc.yacc()
