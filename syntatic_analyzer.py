# -*- coding: utf-8 -*-
import sys
import ply.yacc as yacc

# Importar a lista de tokens do analisador léxico
from lex_analyzer import tokens

global_tree = []

# Define a regra inicial, por padrão o PLY irá usar a primeira regra definida

def p_program(p):
    '''program : statement
                | epsilon
    '''
    global_tree.append(('program', p[1]))


# Define a regra vazia
def p_epsilon(p):
    'epsilon :'
    global_tree.append(('epsilon'))


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
    global_tree.append((tuple(['statement'] + p[1:])))


def p_vardecl(p):
    'vardecl : types IDENT integer'
    global_tree.append(('vardecl', p[1], p[2], p[3]))


def p_types_int(p):
    'types : INT'
    global_tree.append(('type', p[1]))


def p_types_float(p):
    'types : FLOAT'
    global_tree.append(('type', p[1]))


def p_types_string(p):
    'types : STRING'
    global_tree.append(('type', p[1]))


def p_integer(p):
    '''integer : LBRACKET INTCONST RBRACKET integer
            | epsilon
    '''
    global_tree.append((tuple(['integer'] + p[1:])))


def p_atribstat(p):
    '''atribstat : lvalue ATRIB expression
                    | lvalue ATRIB allocexpression
    '''
    global_tree.append((tuple(['atribstat'] + p[1:])))


def p_printstat(p):
    'printstat : PRINT expression'
    global_tree.append((tuple(['printstat'] + p[1:])))


def p_readstat(p):
    'readstat : READ lvalue'
    global_tree.append((tuple(['readstat'] + p[1:])))


def p_returnstat(p):
    'returnstat : RETURN'
    global_tree.append(('returnstat', p[1]))


def p_ifstat(p):
    'ifstat : IF LPAREN expression RPAREN statement else'
    global_tree.append((tuple(['ifstat'] + p[1:])))


def p_else(p):
    '''else : ELSE statement
            | epsilon
    '''
    global_tree.append((tuple(['else'] + p[1:])))


def p_forstat(p):
    'forstat : FOR LPAREN atribstat SEMICOLON expression SEMICOLON atribstat RPAREN statement'
    global_tree.append((tuple(['forstat'] + p[1:])))


def p_statelist(p):
    '''statelist : statement
                    | statement statelist
    '''
    global_tree.append((tuple(['statelist'] + p[1:])))


def p_allocexpression(p):
    'allocexpression : NEW types expressions'
    global_tree.append((tuple(['allocexpression'] + p[1:])))


def p_expressions(p):
    '''expressions : LBRACKET expression RBRACKET expressions
                    | LBRACKET expression RBRACKET
    '''
    global_tree.append((tuple(['expressions'] + p[1:])))


def p_expression(p):
    '''expression : numexpression
                    | binaryoperator numexpression
    '''
    global_tree.append((tuple(['expression'] + p[1:])))


def p_binaryoperator(p):
    '''binaryoperator : numexpression relationaloperator
                        | epsilon
    '''
    global_tree.append((tuple(['binaryoperator'] + p[1:])))


def p_relationaloperator(p):
    '''relationaloperator : RELOP'''
    global_tree.append(('relationaloperator', p[1]))


def p_numexpression(p):
    '''numexpression : term signedterms'''
    global_tree.append((tuple(['numexpression'] + p[1:])))


def p_signedterms(p):
    '''signedterms : signal term signedterms
                    | epsilon
    '''
    global_tree.append((tuple(['signedterms'] + p[1:])))


def p_signal(p):
    '''signal : SIGNAL'''
    global_tree.append(('signal', p[1]))


def p_term(p):
    '''term : unaryexpr unaryiter'''
    global_tree.append((tuple(['term'] + p[1:])))


def p_unaryiter(p):
    '''unaryiter : unaryop unaryexpr unaryiter
                    | epsilon
    '''
    global_tree.append((tuple(['unaryiter'] + p[1:])))


def p_unaryop(p):
    '''unaryop : UNARYOP'''
    global_tree.append(('unaryop', p[1]))


def p_unaryexpr(p):
    '''unaryexpr : signal factor
                    | factor
    '''
    global_tree.append((tuple(['unaryexpr'] + p[1:])))


def p_factor(p):
    '''factor : INTCONST
                | FLOATCONST
                | STRCONST
                | NULL
                | lvalue
                | LPAREN expression RPAREN
    '''
    global_tree.append((tuple(['factor'] + p[1:])))


def p_lvalue(p):
    '''lvalue : IDENT
                | IDENT expressions
    '''
    global_tree.append((tuple(['lvalue'] + p[1:])))


# Função de erro para erros sintáticos
def p_error(p):
    print("Syntax error in input! Token: %s" % (p,))
    print("Line: %s, Column: %s" % (p.lineno, p.lexpos))

    if len(global_tree) == 0:
        print("Error production: %s" % (parser.productions[1],))
    else:
        print("Error production: %s" % (global_tree[-1],))
        for prod in parser.productions:
            if prod.name == global_tree[-1][0]:
                print(prod)
                break

    exit(1)


# Inicializa o analisador sintático
parser = yacc.yacc()

# Constrói o analisador sintático


def build_parser(program):
    with open(program, 'r') as target_file:
        return parser.parse(target_file.read())


if __name__ == "__main__":
    l = build_parser(sys.argv[1])
    print("Success!")
