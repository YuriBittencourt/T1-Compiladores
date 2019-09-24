# -*- coding: utf-8 -*-
from ply import lex


# List of token names.   This is always required
tokens = [
  'INT',
  'FLOAT',
  'STRING',
  'SEMICOLON',
  'BREAK',
  'LBRACES',
  'RBRACES',
  'PRINT',
  'IDENT',
  'RETURN',
  'READ',
  'IF',
  'ELSE',
  'FOR',
  'NEW',
  'RELOP',
  'SIGNAL',
  'UNARYOP',
  'LBRACKET',
  'RBRACKET',
  'INTCONST',
  'FLOATCONST',
  'STRCONST',
  'NULL',
  'LPAREN',
  'RPAREN',
  'ATRIB',
]

# Regular expression rules for simple tokens
t_SEMICOLON = r'\;'
t_LBRACES = r'\{'
t_RBRACES = r'\}'
t_RELOP = r'((<|>)(=)?|(=|!)=)'
t_SIGNAL = r'(\+|\-)'
t_UNARYOP = r'(\%|\\|\*)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
#t_INTCONST = r'\d+'
#t_FLOATCONST = r'[0-9]+\.[0-9]+'
t_STRCONST = r'\"(.)*\"'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_ATRIB = r'\='

reserved = {
    'int': 'INT',
    'float': 'FLOAT',
    'string': 'STRING',
    'break': 'BREAK',
    'print': 'PRINT',
    'return': 'RETURN',
    'read': 'READ',
    'if': 'IF',
    'else': 'ELSE',
    'for': 'FOR',
    'new': 'NEW',
    'null': 'NULL',
}

# A regular expression rule with some action code
def t_FLOATCONST(t):
    r'[0-9]+\.[0-9]+'
    t.value = float(t.value)
    return t

def t_INTCONST(t):
   r'\d+'
   t.value = int(t.value)
   return t

def t_IDENT(t):
   r'[a-z_]([A-Za-z_0-9])*'
   t.type = reserved.get(t.value, 'IDENT')
   return t

# Define a rule so we can track line numbers
def t_newline(t):
   r'\n+'
   t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
   print("Illegal character '%s'" % t.value[0])
   print("Line: %s, Column: %s" % (t.lexer.lineno, t.lexer.lexpos + 1))
   #esse + 1 é para contar a partir da posição 1 e não zero
   exit(0)

# Build the lexer
lexer = lex.lex()
token_list = []
with open('examples/ex1.ccc','r') as target_file:
    for line in target_file:
        lexer.input(line)
        # Tokenize
        while True:
            tok = lexer.token()
            if not tok:
                break      # No more input
            token_list.append(tok)

print(token_list)