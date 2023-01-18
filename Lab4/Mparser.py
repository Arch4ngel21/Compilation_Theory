#!/usr/bin/python

import lab1 as scanner
import ply.yacc as yacc

from AST import *

lexer = scanner.lexer
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
    p[0] = Root(p[1], lineno=lexer.lineno)


def p_instructions_opt_1(p):
    """instructions_opt : instructions """
    p[0] = Instructions(p[1], lineno=lexer.lineno)


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
                   | if ';'
                   | return
                   | return ';'
                   | break
                   | break ';'
                   | continue
                   | continue ';'
                   | for_loop
                   | for_loop ';'
                   | while_loop
                   | while_loop ';'
                   | assignment
                   | assignment ';'
                   | print
                   | print ';'
                   """
    p[0] = p[1]


def p_if(p):
    """if : IF '(' expression ')' instruction %prec IFX
          | IF '(' expression ')' instruction ELSE instruction"""

    if len(p) == 8:
        p[0] = If(p[3], p[5], p[7], lineno=lexer.lineno)
    else:
        p[0] = If(p[3], p[5], None, lineno=lexer.lineno)


def p_break(p):
    """break : BREAK"""
    p[0] = Break(lineno=lexer.lineno)


def p_continue(p):
    """continue : CONTINUE"""
    p[0] = Continue(lineno=lexer.lineno)


def p_while(p):
    """while_loop : WHILE '(' expression ')' instruction """

    if len(p) == 6:
        p[0] = While(p[3], p[5], lineno=lexer.lineno)
    else:
        if type(p[6]) is list:
            p[0] = While(p[3], p[6], lineno=lexer.lineno)
        else:
            p[0] = While(p[3], list(p[6]), lineno=lexer.lineno)


def p_for(p):
    """for_loop : FOR id '=' expression ':' expression instruction"""

    p[0] = For(p[2], p[4], p[6], p[7], lineno=lexer.lineno)


def p_return(p):
    """return : RETURN expression
              | RETURN"""

    if len(p) == 3:
        p[0] = Return(p[2], lineno=lexer.lineno)
    else:
        p[0] = Return(None, lineno=lexer.lineno)


def p_print(p):
    """print : PRINT '(' list_for_print ')'
             | PRINT list_for_print"""

    if p[2] == '(':
        p[0] = Print(p[3], lineno=lexer.lineno)
    else:
        p[0] = Print(p[2], lineno=lexer.lineno)


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
                  | int
                  | float
                  | string"""
    p[0] = p[1]


def p_expression_int(p):
    """int : INTNUM """
    p[0] = ValueInt(p[1], lineno=lexer.lineno)


def p_expression_float(p):
    """float : FLOATNUM """
    p[0] = ValueFloat(p[1], lineno=lexer.lineno)


def p_expression_string(p):
    """string : STRING """
    p[0] = ValueString(p[1], lineno=lexer.lineno)


def p_expression_var(p):
    """var : id"""
    p[0] = p[1]


def p_id(p):
    """id : ID"""
    p[0] = Id(p[1], lineno=lexer.lineno)


def p_expression_ref(p):
    """var : id '[' mat_func_args ']' """
    p[0] = Ref(p[1], p[3], lineno=lexer.lineno)


def p_expression_assignment(p):
    """assignment : var '=' expression
                  | var ADDASSIGN expression
                  | var SUBASSIGN expression
                  | var MULASSIGN expression
                  | var DIVASSIGN expression"""
    p[0] = Assignment(p[1], p[2], p[3], lineno=lexer.lineno)


def p_expression_uniop_left(p):
    """expression : expression "'" """
    p[0] = UniOpExprLeft(p[2], p[1], lineno=lexer.lineno)


def p_expression_uniop_right(p):
    """expression : '-' expression %prec UMINUS"""
    p[0] = UniOpExprRight(p[1], p[2], lineno=lexer.lineno)


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

    p[0] = BinOpExpr(p[2], p[1], p[3], lineno=lexer.lineno)


def p_expression_matrix(p):
    """expression : matrix """
    p[0] = p[1]


def p_matrix(p):
    """matrix : '[' matrix ']'
              | '[' sub_string_1 ']'
              | '[' sub_string_1 ',' matrix ']' """
    if len(p) == 4:
        p[0] = Vector(p[2], lineno=lexer.lineno)
    elif len(p) == 6:
        p[0] = Vector(p[2] + [p[4]], lineno=lexer.lineno)
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
    """expression : matrix_creation '(' mat_func_args ')' """
    p[0] = MatrixCreation(p[1], p[3], lineno=lexer.lineno)


def p_matrix_function_args(p):
    """mat_func_args : mat_func_args ',' expression
                     | expression"""
    p[0] = [p[1]] if len(p) == 2 else p[1] + [p[3]]


def p_matrix_creation(p):
    """matrix_creation : ZEROS
                       | ONES
                       | EYE"""

    p[0] = MatrixFunction(p[1], lineno=lexer.lineno)


parser = yacc.yacc()
