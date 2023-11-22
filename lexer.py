import ply.lex as lex

# Lista de tokens
tokens = (
    'ID',
    'EQUALS',
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'IF',
    'ELSE',
    'WHILE',
    'DO',
    'FOR',
    'FUNCTION',
    'COMMA',
    'SEMI',
)

# Definición de patrones de expresiones regulares
t_EQUALS = r'='
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r','
t_IF = r'if'
t_ELSE = r'else'
t_WHILE = r'while'
t_DO = r'do'
t_FOR = r'for'
t_FUNCTION = r'function'

# Ignorar espacios y tabulaciones
t_ignore = ' \t'

# Expresiones regulares para tokens más complejos
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    return t

def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value)
    return t

# Manejo de errores
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Crear el lexer
lexer = lex.lex()

# Ejemplo de uso
data = "x = 10 + y * 5"
lexer.input(data)

# Imprimir los tokens generados
while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)
