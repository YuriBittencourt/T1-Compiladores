# -*- coding: utf-8 -*-
import sys
import ply.yacc as yacc

# Importar a lista de tokens do analisador léxico
from lex_analyzer import tokens


# Define a regra inicial, por padrão o PLY irá usar a primeira regra definida
def p_program(p):
    '''program : statement
                | epsilon
    '''


# Define a regra vazia
def p_epsilon(p):
    'epsilon :'
    pass


# Define as regras restantes da linguagem
def p_statement(p):
    '''statement : vardecl SEMICOLON
                 | atribstat SEMICOLON
                 | printstat SEMICOLON
                 | readstat SEMICOLON
                 | returnstat SEMICOLON
                 | ifstat
                 | forstat
                 | LBRACES statelist RBRACES
                 | BREAK SEMICOLON
                 | SEMICOLON
    '''


def p_vardecl(p):
    'vardecl : types IDENT integer'


def p_types_int(p):
    'types : INT'


def p_types_float(p):
    'types : FLOAT'


def p_types_string(p):
    'types : STRING'


def p_integer(p):
    '''integer : LBRACKET INTCONST RBRACKET integer
            | epsilon
    '''


def p_atribstat(p):
    '''atribstat : lvalue ATRIB expression
                    | lvalue ATRIB allocexpression
    '''


def p_printstat(p):
    'printstat : PRINT expression'


def p_readstat(p):
    'readstat : READ lvalue'


def p_returnstat(p):
    'returnstat : RETURN'


def p_ifstat(p):
    'ifstat : IF LPAREN expression RPAREN statement else'


def p_else(p):
    '''else : ELSE statement
            | epsilon
    '''


def p_forstat(p):
    'forstat : FOR LPAREN atribstat SEMICOLON expression SEMICOLON atribstat RPAREN statement'


def p_statelist(p):
    '''statelist : statement
                    | statement statelist
    '''


def p_allocexpression(p):
    'allocexpression : NEW types expressions'


def p_expressions(p):
    '''expressions : LBRACKET expression RBRACKET expressions
                    | LBRACKET expression RBRACKET
    '''


def p_expression(p):
    '''expression : numexpression
                    | binaryoperator numexpression
    '''


def p_binaryoperator(p):
    '''binaryoperator : numexpression relationaloperator
                        | epsilon
    '''


def p_relationaloperator(p):
    '''relationaloperator : RELOP'''


def p_numexpression(p):
    '''numexpression : term signedterms'''


def p_signedterms(p):
    '''signedterms : signal term signedterms
                    | epsilon
    '''


def p_signal(p):
    '''signal : SIGNAL'''


def p_term(p):
    '''term : unaryexpr unaryiter'''


def p_unaryiter(p):
    '''unaryiter : unaryop unaryexpr unaryiter
                    | epsilon
    '''


def p_unaryop(p):
    '''unaryop : UNARYOP'''


def p_unaryexpr(p):
    '''unaryexpr : signal factor
                    | factor
    '''


def p_factor(p):
    '''factor : INTCONST
                | FLOATCONST
                | STRCONST
                | NULL
                | lvalue
                | LPAREN expression RPAREN
    '''


def p_lvalue(p):
    '''lvalue : IDENT
                | IDENT expressions
    '''


# Função de erro para erros sintáticos
def p_error(p):
    print("Syntax error in input!", p)
    print("Line: %s, Column: %s" % (p.lineno, p.lexpos ))
    exit(0)


# Inicializa o analisador sintático
parser = yacc.yacc()


# Constrói o analisador sintático
def build_parser(program):
    with open(program, 'r') as target_file:
        return parser.parse(target_file.read())


if __name__ == "__main__":
    build_parser(sys.argv[1])
    print("Success!")
