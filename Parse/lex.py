import ply.lex as lex
import sys

reserved = {
  'alphabet': 'ALPHABET',
  'states': 'STATES',
  'terminal': 'TERMINAL',
  'state': 'STATE'
}

tokens = [
  'COMMA',
  'COMMENT',
  'CURLY_BRACKET_OPEN',
  'CURLY_BRACKET_CLOSE',
  'SQUARE_BRACKET_OPEN',
  'SQUARE_BRACKET_CLOSE',
  'STR',
  'ARROW',
  'VARIABLE'
] + list(reserved.values())

def t_VARIABLE(t):
  r'[A-Za-z][_0-9A-Za-z]*'
  t.type = reserved.get(t.value, 'VARIABLE')
  return t

def t_STR(t):
  r'"(?:[^\\"]|\\.)*"'
  t.value = t.value[1 : -1]
  return t


t_ignore = ' \t'
t_COMMENT = r'\/\/.*'
t_COMMA = r','
t_CURLY_BRACKET_OPEN = r'\{'
t_CURLY_BRACKET_CLOSE = r'\}'
t_SQUARE_BRACKET_OPEN = r'\['
t_SQUARE_BRACKET_CLOSE = r'\]'
t_ARROW = r'--->'

def t_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)

def t_error(t):
  print("Illegal character '%s'" % t.value[0])
  t.lexer.skip(1)

lexer = lex.lex()

#lexer.input(open(sys.argv[1], 'r').read())
#sys.stdout = open(sys.argv[1] + '.out', 'w')

#while True:
#    tok = lexer.token()
#    if not tok:
#        break
#    print(tok)
