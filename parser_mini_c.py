# Um parser que recebe a lista de tokens e tipos e retorna a árvore sintática

tokens = [['(', '('], [')', ')'], ['{', '{'], ['}', '}'], [',', ','], ['.', '.'], [';', ';'], 
         ['=', '='], ['==', '=='], ['<', '<'], ['>', '>'], ['<=', '<='], ['>=', '>='], 
         ['!=', '!='], ['+', '+'], ['-', '-'], ['*', '*'], ['/', '/'], ['1234', 'int'], 
         ['12.34', 'float'], ['for', 'for'], ['while', 'while'], ['if', 'if'], 
         ['else', 'else'], ['var1', 'identifier'], ['123', 'number']]

simbolos = {
    "Function": 0,
    "ArgList": 1,
    "Arg": 2,
    "Declaration": 3,
    "Type": 4,
    "IdentList": 5,
    "Stmt": 6,
    "ForStmt": 7,
    "OptExpr": 8,
    "whileStmt": 9,
    "IfStmt": 10,
    "ElsePart": 11,
    "CompoundStmt": 12,
    "StmtList": 13,
    "Expr": 14,
    "Rvalue": 15,
    "Compare": 16,
    "Mag": 17,
    "Term": 18,
    "Factor": 19,
}

tokens_struct = {
    "identifier": 0,
    "number": 1,
    "int": 2,
    "float": 3,
    "if": 4,
    "else": 5,
    "for": 6,
    "while": 7,
    ",": 8,
    ".": 9,
    ";": 10,
    "{": 11,
    "}": 12,
    "(": 13,
    ")": 14,
    "=": 15,
    "==": 16,
    "<": 17,
    ">": 18,
    "<=": 19,
    ">=": 20,
    "!=": 21,
    "-": 22,
    "+": 23,
    "*": 24,
    "/": 25
}

lista_regras = []



for i in simbolos:
    for j in tokens_struct:
        lista_regras[i][j]

print(lista_regras)

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

