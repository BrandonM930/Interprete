import ply.yacc as yacc

# Importar los tokens desde el lexer
from lexer import tokens

# Reglas de inicio
def p_statement_assign(p):
    'statement : ID EQUALS expression'
    p[0] = ('assign', p[1], p[3])

# Reglas para expresiones aritméticas
def p_expression_binop(p):
    '''
    expression : expression PLUS expression
               | expression MINUS expression
               | expression TIMES expression
               | expression DIVIDE expression
    '''
    p[0] = (p[2], p[1], p[3])

# Reglas para condicionales
def p_statement_conditional(p):
    '''
    statement : IF expression statement
              | IF expression statement ELSE statement
    '''
    if len(p) == 4:
        p[0] = ('if', p[2], p[3])
    else:
        p[0] = ('if-else', p[2], p[3], p[5])

# Reglas para ciclos
def p_statement_while(p):
    'statement : WHILE expression statement'
    p[0] = ('while', p[2], p[3])

def p_statement_do_while(p):
    'statement : DO statement WHILE expression'
    p[0] = ('do-while', p[2], p[4])

def p_statement_for(p):
    'statement : FOR LPAREN statement SEMI expression SEMI statement RPAREN'
    p[0] = ('for', p[3], p[5], p[7])

# Reglas para llamadas a funciones con parámetros
def p_expression_function_call(p):
    'expression : FUNCTION ID LPAREN param_list RPAREN'
    p[0] = ('function-call', p[2], p[4])

def p_param_list(p):
    'param_list : expression COMMA param_list'
    p[0] = [p[1]] + p[3]

def p_param_list_single(p):
    'param_list : expression'
    p[0] = [p[1]]

# Regla para expresiones con paréntesis
def p_expression_paren(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

# Regla para números e identificadores
def p_expression_num_id(p):
    '''
    expression : NUMBER
               | ID
    '''
    p[0] = p[1]

# Manejo de errores
def p_error(p):
    print(f"Error de sintaxis en '{p.value}'")

# Crear el analizador
parser = yacc.yacc()

# Función para analizar datos
def parse(data):
    return parser.parse(data)

# Ejemplo de uso
data = "x = 10 + y * 5"
result = parser.parse(data)
print(result)
