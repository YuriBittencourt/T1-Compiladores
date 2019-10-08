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
    p[0] = ('program', p[1])


# Define a regra vazia
def p_epsilon(p):
    'epsilon :'
    p[0] = ('epsilon')


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
    p[0] = (tuple(['statement'] + p[1:]))


def p_vardecl(p):
    'vardecl : types IDENT integer'
    p[0] = ('vardecl', p[1], p[2], p[3])


def p_types_int(p):
    'types : INT'
    p[0] = ('type', p[1])


def p_types_float(p):
    'types : FLOAT'
    p[0] = ('type', p[1])


def p_types_string(p):
    'types : STRING'
    p[0] = ('type', p[1])


def p_integer(p):
    '''integer : LBRACKET INTCONST RBRACKET integer
            | epsilon
    '''
    p[0] = (tuple(['integer'] + p[1:]))


def p_atribstat(p):
    '''atribstat : lvalue ATRIB expression
                    | lvalue ATRIB allocexpression
    '''
    p[0] = (tuple(['atribstat'] + p[1:]))


def p_printstat(p):
    'printstat : PRINT expression'
    p[0] = (tuple(['printstat'] + p[1:]))


def p_readstat(p):
    'readstat : READ lvalue'
    p[0] = (tuple(['readstat'] + p[1:]))


def p_returnstat(p):
    'returnstat : RETURN'
    p[0] = ('returnstat', p[1])


def p_ifstat(p):
    'ifstat : IF LPAREN expression RPAREN statement else'
    p[0] = (tuple(['ifstat'] + p[1:]))


def p_else(p):
    '''else : ELSE statement
            | epsilon
    '''
    p[0] = (tuple(['else'] + p[1:]))


def p_forstat(p):
    'forstat : FOR LPAREN atribstat SEMICOLON expression SEMICOLON atribstat RPAREN statement'
    p[0] = (tuple(['forstat'] + p[1:]))


def p_statelist(p):
    '''statelist : statement
                    | statement statelist
    '''
    p[0] = (tuple(['statelist'] + p[1:]))


def p_allocexpression(p):
    'allocexpression : NEW types expressions'
    p[0] = (tuple(['allocexpression'] + p[1:]))


def p_expressions(p):
    '''expressions : LBRACKET expression RBRACKET expressions
                    | LBRACKET expression RBRACKET
    '''
    p[0] = (tuple(['expressions'] + p[1:]))


def p_expression(p):
    '''expression : numexpression
                    | binaryoperator numexpression
    '''
    p[0] = (tuple(['expression'] + p[1:]))


def p_binaryoperator(p):
    '''binaryoperator : numexpression relationaloperator
                        | epsilon
    '''
    p[0] = (tuple(['binaryoperator'] + p[1:]))


def p_relationaloperator(p):
    '''relationaloperator : RELOP'''
    p[0] = ('relationaloperator', p[1])


def p_numexpression(p):
    '''numexpression : term signedterms'''
    p[0] = (tuple(['numexpression'] + p[1:]))


def p_signedterms(p):
    '''signedterms : signal term signedterms
                    | epsilon
    '''
    p[0] = (tuple(['signedterms'] + p[1:]))


def p_signal(p):
    '''signal : SIGNAL'''
    p[0] = ('signal', p[1])


def p_term(p):
    '''term : unaryexpr unaryiter'''
    p[0] = (tuple(['term'] + p[1:]))


def p_unaryiter(p):
    '''unaryiter : unaryop unaryexpr unaryiter
                    | epsilon
    '''
    p[0] = (tuple(['unaryiter'] + p[1:]))


def p_unaryop(p):
    '''unaryop : UNARYOP'''
    p[0] = ('unaryop', p[1])


def p_unaryexpr(p):
    '''unaryexpr : signal factor
                    | factor
    '''
    p[0] = (tuple(['unaryexpr'] + p[1:]))


def p_factor(p):
    '''factor : INTCONST
                | FLOATCONST
                | STRCONST
                | NULL
                | lvalue
                | LPAREN expression RPAREN
    '''
    p[0] = (tuple(['factor'] + p[1:]))


def p_lvalue(p):
    '''lvalue : IDENT
                | IDENT expressions
    '''
    p[0] = (tuple(['lvalue'] + p[1:]))


# Função de erro para erros sintáticos
def p_error(p):
    print("Syntax error in input!", p)
    print("Line: %s, Column: %s" % (p.lineno, p.lexpos ))
    raise SyntaxError


# Inicializa o analisador sintático
parser = yacc.yacc()


# Constrói o analisador sintático
def build_parser(program):
    with open(program, 'r') as target_file:
        return parser.parse(target_file.read())


if __name__ == "__main__":
    l = build_parser(sys.argv[1])
    print("Success!")
    print(l)
