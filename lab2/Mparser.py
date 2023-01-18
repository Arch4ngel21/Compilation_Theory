#!/usr/bin/python

import lab1 as scanner
import ply.yacc as yacc

tokens = scanner.tokens

precedence = (
    ("left", '+', '-'),
    ("left", '*', '/'),
    ("left", 'DOTADD', 'DOTSUB'),
    ("left", 'DOTMUL', 'DOTDIV'),

    ("left", '=', 'ADDASSIGN', 'SUBASSIGN', 'MULASSIGN', 'DIVASSIGN'),
    ("nonassoc", 'LESSEQ', 'MOREEQ', 'NOTEQUAL', 'EQUAL', '<', '>'),

    ("left", "'")
)

symtab = {}


def p_error(p):
    if p:
        print("Syntax error at line {0}: LexToken({1}, '{2}')".format(p.lineno, p.type, p.value))
    else:
        print("Unexpected end of input")


def p_program(p):
    """program : instructions_opt"""


def p_instructions_opt_1(p):
    """instructions_opt : instructions """


def p_instructions_opt_2(p):
    """instructions_opt : """


def p_instructions_1(p):
    """instructions : instructions instruction
                    | instruction"""


def p_instructions_2(p):
    """instruction : '{' instruction '}' """


def p_instruction_3(p):
    """instruction : if
                   | return ';'
                   | BREAK ';'
                   | CONTINUE ';'
                   | for_loop
                   | while_loop
                   | assignment ';'
                   | print"""


def p_if(p):
    """if : IF '(' expression ')' instruction ELSE instruction
          | IF '(' expression ')' instruction
          | IF '(' expression ')' instruction ELSE if"""


def p_while(p):
    """while_loop : WHILE '(' expression ')' instruction
                  | WHILE '(' expression ')' '{' instruction '}'
                  | WHILE '(' expression ')' '{' instructions '}'"""


def p_for(p):
    """for_loop : FOR ID '=' expression ':' expression instruction"""


def p_return(p):
    """return : RETURN expression
              | RETURN"""


def p_print(p):
    """print : PRINT '(' list_for_print ')' ';'
             | PRINT list_for_print ';'"""


def p_list_for_print(p):
    """list_for_print : expression ',' list_for_print
                      | expression"""


def p_expression_obj(p):
    """expression : var
                  | '(' expression ')'
                  | INTNUM
                  | FLOATNUM
                  | STRING"""


def p_expression_var(p):
    """var : ID"""


def p_expression_ref(p):
    """var : ID '[' expression ',' expression ']' """


def p_expression_assignment(p):
    """assignment : var '=' expression
                  | var ADDASSIGN expression
                  | var SUBASSIGN expression
                  | var MULASSIGN expression
                  | var DIVASSIGN expression"""


def p_expression_uniop_left(p):
    """expression : expression "'" """


def p_expression_uniop_right(p):
    """expression : '-' expression """


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


def p_expression_matrix(p):
    """expression : matrix """


def p_matrix(p):
    """matrix : '[' matrix ']'
              | '[' sub_string_1 ']'
              | '[' sub_string_1 ',' matrix ']' """


def p_sub_matrix(p):
    """sub_string_1 : sub_string_1 ',' expression
                    | expression"""


def p_matrix_creation_1(p):
    """expression : matrix_creation '(' expression ')' """


def p_matrix_creation(p):
    """matrix_creation : ZEROS
                       | ONES
                       | EYE"""


parser = yacc.yacc()
