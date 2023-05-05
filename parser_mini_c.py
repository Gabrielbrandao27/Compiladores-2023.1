# Um parser que recebe a lista de tokens e tipos e retorna a árvore sintática

tokens = [['(', '('], [')', ')'], ['{', '{'], ['}', '}'], [',', ','], ['.', '.'], [';', ';'], 
         ['=', '='], ['==', '=='], ['<', '<'], ['>', '>'], ['<=', '<='], ['>=', '>='], 
         ['!=', '!='], ['+', '+'], ['-', '-'], ['*', '*'], ['/', '/'], ['1234', 'int'], 
         ['12.34', 'float'], ['for', 'for'], ['while', 'while'], ['if', 'if'], 
         ['else', 'else'], ['var1', 'identifier'], ['123', 'number']]

simbolos = {
    0: "Function",
    1: "ArgList",
    2: "Arg",
    3: "Declaration",
    4: "Type",
    5: "IdentList",
    6: "Stmt",
    7: "ForStmt",
    8: "OptExpr",
    9: "whileStmt",
    10: "IfStmt",
    11: "ElsePart",
    12: "CompoundStmt",
    13: "StmtList",
    14: "Expr",
    15: "Rvalue",
    16: "Compare",
    17: "Mag",
    18: "Term",
    19: "Factor"
}

tokens_struct = {
    0: "identifier",
    1: "number",
    2: "int",
    3: "float",
    4: "if",
    5: "else",
    6: "for",
    7: "while",
    8: ",",
    9: ".",
    10: ";",
    11: "{",
    12: "}",
    13: "(",
    14: ")",
    15: "=",
    16: "==",
    17: "<",
    18: ">",
    19: "<=",
    20: ">=",
    21: "!=",
    22: "-",
    23: "+",
    24: "*",
    25: "/",
}

lista_regras = [[None] * len(tokens_struct) for i in range(len(simbolos))]

for i in range(len(simbolos)):
    for j in range(len(tokens_struct)):
        lista_regras[i][j] = "ok"

#print(lista_regras)

pilha = []

def vazia(pilha):
    return pilha == []

def empilhar(pilha, item):
    return pilha.append(item)

def remover(pilha, item):
    return pilha.pop(item)

def topo(pilha):
    return pilha[-1]

def tamanho(pilha):
    return len(pilha)

def posicao(pilha, item):
    indice = len(pilha) - 1 - pilha[::-1].index(item)
    return indice

def terminal(item):
    if item in tokens_struct:
        return True

empilhar(pilha, '$')
empilhar(pilha, simbolos[0])
print(pilha)

for token in tokens:
    token_atual = token

    while topo(pilha) != '$' and pilha[posicao(topo(pilha))-1] == '$':
        if terminal(topo(pilha)) and token_atual 
