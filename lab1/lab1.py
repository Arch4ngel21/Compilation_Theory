# Michał Szafarczyk

import ply.lex as lex

reserved = {
    'if' : 'IF',
    'else' : 'ELSE',
    'for' : 'FOR',
    'while' : 'WHILE',
    'break' : 'BREAK',
    'continue' : 'CONTINUE',
    'return' : 'RETURN',
    'print' : 'PRINT'
}

tokens = ['ID',
          'INTNUM',
          'FLOATNUM',
          'STRING',
          'EYE', 'ZEROS', 'ONES',
          'ADDASSIGN', 'SUBASSIGN', 'MULASSIGN', 'DIVASSIGN',
          'LESSEQ', 'MOREEQ', 'NOTEQUAL', 'EQUAL',
          'DOTADD', 'DOTSUB', 'DOTMUL', 'DOTDIV'
          ] + list(reserved.values())

literals = ['-', '+', '*', '/', '=',
            ',', ';', ':', '\'',
            '(', ')', '[', ']', '{', '}',
            '<', '>'
            ]

t_ignore = ' \t'
t_ignore_comment = r'\#.*\n'


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    print("Illegal character '%s'" %t.value)
    t.lexer.skip(1)


def t_FLOATNUM(t):
    # r'\d+\.\d*(E\d+)?|\.\d+(E\d+)?'
    r'(\d+\.(\d+((E|e)\d+)?)?)|(\.\d+((E|e)/d+)?)'
    return t


def t_INTNUM(t):
    r'\d+'
    return t


def t_STRING(t):
    r'(\'.*\')|(\".*\")'
    return t


def t_EYE(t):
    r'eye'
    return t


def t_ZEROS(t):
    r'zeros'
    return t


def t_ONES(t):
    r'ones'
    return t


t_ADDASSIGN = r'\+='
t_SUBASSIGN = r'-='
t_MULASSIGN = r'\*='
t_DIVASSIGN = r'\/='

t_LESSEQ = r'<='
t_MOREEQ = r'>='
t_NOTEQUAL = r'!='
t_EQUAL = r'=='

t_DOTADD = r'\.\+'
t_DOTSUB = r'\.-'
t_DOTMUL = r'\.\*'
t_DOTDIV = r'\.\/'


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t


def t_COMMENT(t):
    r'\#.*'


lexer = lex.lex()
