# Um parser que recebe a lista de tokens e tipos e retorna a árvore sintática
pilha = []
saida = []

def vazia(pilha):
    return pilha == []

def empilhar(pilha, item):
    return pilha.append(item)

def topo(pilha):
    return pilha[-1]

def tamanho(pilha):
    return len(pilha)

def posicao(pilha, item):
    indice = len(pilha) - 1 - pilha[::-1].index(item)
    return indice

def terminal(item):
    for i in regras_struct:
        if item in regras_struct[i]:
            return True

input = open("scanner/result.text", "r")
tokens_line = input.read().split('\n')
tokens = []
for token_line in tokens_line:
    tokens.append(token_line.split())

print("Tokens: ", tokens)

simbolos = {
    0 : "Function", 
    1 : "ArgList", 
    2 : "Arg", 
    3 : "Declaration", 
    4 : "Type", 
    5 : "IdentList", 
    6 : "Stmt", 
    7 : "ForStmt", 
    8 : "OptExpr", 
    9 : "whileStmt", 
    10 : "IfStmt", 
    11 : "ElsePart", 
    12 : "CompoundStmt", 
    13 : "StmtList", 
    14 : "Expr", 
    15 : "Rvalue", 
    16 : "Compare", 
    17 : "Mag", 
    18 : "Mag'",
    19 : "Term", 
    20 : "Term'",
    21 : "Factor"
}

tokens_struct = {
    0 : "identifier",
    1 : "number",
    2 : "int",
    3 : "float",
    4 : "if",
    5 : "else",
    6 : "for",
    7 : "while",
    8 : ",",
    9 : ".",
    10 : ";",
    11 : "{",
    12 : "}",
    13 : "(",
    14 : ")",
    15 : "=",
    16 : "==",
    17 : "<",
    18 : ">",
    19 : "<=",
    20 : ">=",
    21 : "!=",
    22 : "-",
    23 : "+",
    24 : "*",
    25 : "/"
}

regras_struct = {
    "Function": {
        "identifier": '', "number": '', "int": 'Type identifier ( ArgList ) CompoundStmt', "float": 'Type identifier ( ArgList ) CompoundStmt', "if": '', "else": '', "for": '', "while": '', ",": '', ".": '', ";": '', "{": '', "}": '',
         "(": '', ")": '', "=": '', "==": '', "<": '', ">": '', "<=": '', ">=": '', "!=": '', "-": '', "+": '', "*": '', "/": ''
    },
    "ArgList": {
        "identifier": '', "number": '', "int": '', "float": '', "if": '', "else": '', "for": '', "while": '', ",": '', ".": '', ";": '', "{": '', "}": '',
         "(": '', ")": '', "=": '', "==": '', "<": '', ">": '', "<=": '', ">=": '', "!=": '', "-": '', "+": '', "*": '', "/": ''
    },
    "Arg": {
        "identifier": '', "number": '', "int": '', "float": '', "if": '', "else": '', "for": '', "while": '', ",": '', ".": '', ";": '', "{": '', "}": '',
         "(": '', ")": '', "=": '', "==": '', "<": '', ">": '', "<=": '', ">=": '', "!=": '', "-": '', "+": '', "*": '', "/": ''
    },
    "Declaration": {
        "identifier": '', "number": '', "int": '', "float": '', "if": '', "else": '', "for": '', "while": '', ",": '', ".": '', ";": '', "{": '', "}": '',
         "(": '', ")": '', "=": '', "==": '', "<": '', ">": '', "<=": '', ">=": '', "!=": '', "-": '', "+": '', "*": '', "/": ''
    },
    "Type": {
        "identifier": '', "number": '', "int": 'int', "float": 'float', "if": '', "else": '', "for": '', "while": '', ",": '', ".": '', ";": '', "{": '', "}": '',
         "(": '', ")": '', "=": '', "==": '', "<": '', ">": '', "<=": '', ">=": '', "!=": '', "-": '', "+": '', "*": '', "/": ''
    },
    "IdentList": {
        "identifier": '', "number": '', "int": '', "float": '', "if": '', "else": '', "for": '', "while": '', ",": '', ".": '', ";": '', "{": '', "}": '',
         "(": '', ")": '', "=": '', "==": '', "<": '', ">": '', "<=": '', ">=": '', "!=": '', "-": '', "+": '', "*": '', "/": ''
    },
    "Stmt": {
        "identifier": '', "number": '', "int": '', "float": '', "if": '', "else": '', "for": '', "while": '', ",": '', ".": '', ";": '', "{": '', "}": '',
         "(": '', ")": '', "=": '', "==": '', "<": '', ">": '', "<=": '', ">=": '', "!=": '', "-": '', "+": '', "*": '', "/": ''
    },
    "ForStmt": {
        "identifier": '', "number": '', "int": '', "float": '', "if": '', "else": '', "for": '', "while": '', ",": '', ".": '', ";": '', "{": '', "}": '',
         "(": '', ")": '', "=": '', "==": '', "<": '', ">": '', "<=": '', ">=": '', "!=": '', "-": '', "+": '', "*": '', "/": ''
    },
    "OptExpr": {
        "identifier": '', "number": '', "int": '', "float": '', "if": '', "else": '', "for": '', "while": '', ",": '', ".": '', ";": '', "{": '', "}": '',
         "(": '', ")": '', "=": '', "==": '', "<": '', ">": '', "<=": '', ">=": '', "!=": '', "-": '', "+": '', "*": '', "/": ''
    },
    "WhileStmt": {
        "identifier": '', "number": '', "int": '', "float": '', "if": '', "else": '', "for": '', "while": '', ",": '', ".": '', ";": '', "{": '', "}": '',
         "(": '', ")": '', "=": '', "==": '', "<": '', ">": '', "<=": '', ">=": '', "!=": '', "-": '', "+": '', "*": '', "/": ''
    },
    "IfStmt": {
        "identifier": '', "number": '', "int": '', "float": '', "if": '', "else": '', "for": '', "while": '', ",": '', ".": '', ";": '', "{": '', "}": '',
         "(": '', ")": '', "=": '', "==": '', "<": '', ">": '', "<=": '', ">=": '', "!=": '', "-": '', "+": '', "*": '', "/": ''
    },
    "ElsePart": {
        "identifier": '', "number": '', "int": '', "float": '', "if": '', "else": '', "for": '', "while": '', ",": '', ".": '', ";": '', "{": '', "}": '',
         "(": '', ")": '', "=": '', "==": '', "<": '', ">": '', "<=": '', ">=": '', "!=": '', "-": '', "+": '', "*": '', "/": ''
    },
    "CompoundStmt": {
        "identifier": '', "number": '', "int": '', "float": '', "if": '', "else": '', "for": '', "while": '', ",": '', ".": '', ";": '', "{": '', "}": '',
         "(": '', ")": '', "=": '', "==": '', "<": '', ">": '', "<=": '', ">=": '', "!=": '', "-": '', "+": '', "*": '', "/": ''
    },
    "StmtList": {
        "identifier": '', "number": '', "int": '', "float": '', "if": '', "else": '', "for": '', "while": '', ",": '', ".": '', ";": '', "{": '', "}": '',
         "(": '', ")": '', "=": '', "==": '', "<": '', ">": '', "<=": '', ">=": '', "!=": '', "-": '', "+": '', "*": '', "/": ''
    },
    "Expr": {
        "identifier": '', "number": '', "int": '', "float": '', "if": '', "else": '', "for": '', "while": '', ",": '', ".": '', ";": '', "{": '', "}": '',
         "(": '', ")": '', "=": '', "==": '', "<": '', ">": '', "<=": '', ">=": '', "!=": '', "-": '', "+": '', "*": '', "/": ''
    },
    "Rvalue": {
        "identifier": '', "number": '', "int": '', "float": '', "if": '', "else": '', "for": '', "while": '', ",": '', ".": '', ";": '', "{": '', "}": '',
         "(": '', ")": '', "=": '', "==": '', "<": '', ">": '', "<=": '', ">=": '', "!=": '', "-": '', "+": '', "*": '', "/": ''
    },
    "Compare": {
        "identifier": '', "number": '', "int": '', "float": '', "if": '', "else": '', "for": '', "while": '', ",": '', ".": '', ";": '', "{": '', "}": '',
         "(": '', ")": '', "=": '', "==": '', "<": '', ">": '', "<=": '', ">=": '', "!=": '', "-": '', "+": '', "*": '', "/": ''
    },
    "Mag": {
        "identifier": '', "number": '', "int": '', "float": '', "if": '', "else": '', "for": '', "while": '', ",": '', ".": '', ";": '', "{": '', "}": '',
         "(": '', ")": '', "=": '', "==": '', "<": '', ">": '', "<=": '', ">=": '', "!=": '', "-": '', "+": '', "*": '', "/": ''
    },
    "Mag'": {
        "identifier": '', "number": '', "int": '', "float": '', "if": '', "else": '', "for": '', "while": '', ",": '', ".": '', ";": '', "{": '', "}": '',
         "(": '', ")": '', "=": '', "==": '', "<": '', ">": '', "<=": '', ">=": '', "!=": '', "-": '', "+": '', "*": '', "/": ''
    },
    "Term": {
        "identifier": '', "number": '', "int": '', "float": '', "if": '', "else": '', "for": '', "while": '', ",": '', ".": '', ";": '', "{": '', "}": '',
         "(": '', ")": '', "=": '', "==": '', "<": '', ">": '', "<=": '', ">=": '', "!=": '', "-": '', "+": '', "*": '', "/": ''
    },
    "Term'": {
        "identifier": '', "number": '', "int": '', "float": '', "if": '', "else": '', "for": '', "while": '', ",": '', ".": '', ";": '', "{": '', "}": '',
         "(": '', ")": '', "=": '', "==": '', "<": '', ">": '', "<=": '', ">=": '', "!=": '', "-": '', "+": '', "*": '', "/": ''
    },
    "Factor": {
        "identifier": '', "number": '', "int": '', "float": '', "if": '', "else": '', "for": '', "while": '', ",": '', ".": '', ";": '', "{": '', "}": '',
         "(": '', ")": '', "=": '', "==": '', "<": '', ">": '', "<=": '', ">=": '', "!=": '', "-": '', "+": '', "*": '', "/": ''
    }
}


empilhar(pilha, '$')
empilhar(pilha, simbolos[0])
print("Pilha inicial:", pilha)
token_index = 0
token_atual = tokens[token_index]

while token_atual[1] != '$':
    print("Token atual: ", token_atual[1])

    if not terminal(topo(pilha)): 
        print("Topo da pilha:", topo(pilha))
        regra_atual = regras_struct[topo(pilha)][token_atual[1]]
        print("Regra atual:", regra_atual)

        pilha.pop()

        vector_regra_atual = regra_atual.split()
        for r in reversed(vector_regra_atual):
            empilhar(pilha, r)
        print("Pilha atualizada:", pilha)
    else:
        if topo(pilha) == token_atual[1]:
            pilha.pop()
            saida.append(token_atual)
            print("It's a Match!! Token", token_atual[1], "removed")
            token_index += 1
            token_atual = tokens[token_index]
            print("Next token will be:", token_atual, "\n")

print("Saída: ", saida)