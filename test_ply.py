# -*- coding: utf-8 -*-
from ply import lex
from ply import yacc

data = '''
{
{
  float x;
  float z;
  int i;
  int max;
  x = 0;
  max = 10000;
  for (i = 1; i <= max; i = i + 1){
    print x;
    x = x + 0.001;
    z = x;
    if (z != x){
      print "Erro numérico na atribuição de números na notação ponto flutuante!";
      break;
    }
  }
}


{
  int y;
  int j;
  int i;
  y = new int[10];
  j = 0;
  for (i = 0; i < 20; i = i + 1)
    if (i % 2 == 0){
      y[j] = i + 1;
      j = j + 1;
    }
    else
      print 0;

  for (i = 0; i < 10; i = i + 1)
    print y[i];

  return;
}
}
'''

# List of token names.   This is always required
tokens = (
  'NUMBER',
  'PLUS',
  'MINUS',
  'TIMES',
  'DIVIDE',
  'LPAREN',
  'RPAREN',
)

# Regular expression rules for simple tokens
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'

 # A regular expression rule with some action code
def t_NUMBER(t):
   r'\d+'
   t.value = int(t.value)
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
   t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

lexer.input(data)

# Tokenize
while True:
   tok = lexer.token()
   if not tok:
       break      # No more input
   print(tok)

