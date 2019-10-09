# -*- coding: utf-8 -*-
import sys
from ply import lex

# Lista de todos os tokens
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

# Palavras reservadas da linguagem
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

# Expressões regulares para os tokens
t_SEMICOLON = r'\;'
t_LBRACES = r'\{'
t_RBRACES = r'\}'
t_RELOP = r'((<|>)(=)?|(=|!)=)'
t_SIGNAL = r'(\+|\-)'
t_UNARYOP = r'(\%|\\|\*)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_STRCONST = r'\"(.)*\"'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_ATRIB = r'\='

# função especial para fazer cast dos valores dos tokens FLOATCONST e
# INTCONST e também definir sua expressão regular
def t_FLOATCONST(t):
    r'[0-9]+\.[0-9]+'
    t.value = float(t.value)
    return t

def t_INTCONST(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Função especial para o token IDENT, pois precisa verificar se o token não se trata de uma palavra reservada.
# essa é a forma que o PLY disponibiliza e encoraja para tratar essa
# precedência
def t_IDENT(t):
    r'[a-z_]([A-Za-z_0-9])*'
    t.type = reserved.get(t.value, 'IDENT')
    return t

# Define a regra para contar os números de linha
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# String de caracteres ignorados, espaços e tabs
t_ignore = ' \t'

# Regra de tratamento de erro:
# Imprime a caractere inválida, sua linha e coluna.
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    print("Line: %s, Column: %s" % (t.lexer.lineno, t.lexer.lexpos + 1))
    # esse + 1 é para contar a partir da posição 1 e não zero
    exit(0)

# inicializa o analisador léxico
lexer = lex.lex()

# constroi o análisador léxico
def build_lexer(program):
    token_lst = []
    with open(program, 'r') as target_file:
        for line in target_file:
            lexer.input(line)
            # Tokeniza
            while True:
                tok = lexer.token()
                if not tok:
                    break      # Não há mais entradas
                token_lst.append(tok)
    return token_lst

if __name__ == "__main__":
    token_list = build_lexer(sys.argv[1])
    print([(x.type, x.value, x.lineno, x.lexpos) for x in token_list])
