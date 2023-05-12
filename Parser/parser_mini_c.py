pilha = []
saida = []
regras = []

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
        "identifier": '', "number": '', "int": 'Arg', "float": 'Arg', "if": '', "else": '', "for": '', "while": '', ",": '', ".": '', ";": '', "{": '', "}": '',
         "(": '', ")": '', "=": '', "==": '', "<": '', ">": '', "<=": '', ">=": '', "!=": '', "-": '', "+": '', "*": '', "/": ''
    },
    "Arg": {
        "identifier": '', "number": '', "int": 'Type identifier', "float": 'Type identifier', "if": '', "else": '', "for": '', "while": '', ",": '', ".": '', ";": '', "{": '', "}": '',
         "(": '', ")": '', "=": '', "==": '', "<": '', ">": '', "<=": '', ">=": '', "!=": '', "-": '', "+": '', "*": '', "/": ''
    },
    "Declaration": {
        "identifier": '', "number": '', "int": 'Type IdentList ;', "float": 'Type IdentList ;', "if": '', "else": '', "for": '', "while": '', ",": '', ".": '', ";": '', "{": '', "}": '',
         "(": '', ")": '', "=": '', "==": '', "<": '', ">": '', "<=": '', ">=": '', "!=": '', "-": '', "+": '', "*": '', "/": ''
    },
    "Type": {
        "identifier": '', "number": '', "int": 'int', "float": 'float', "if": '', "else": '', "for": '', "while": '', ",": '', ".": '', ";": '', "{": '', "}": '',
         "(": '', ")": '', "=": '', "==": '', "<": '', ">": '', "<=": '', ">=": '', "!=": '', "-": '', "+": '', "*": '', "/": ''
    },
    "IdentList": {
        "identifier": 'identifier', "number": '', "int": '', "float": '', "if": '', "else": '', "for": '', "while": '', ",": '', ".": '', ";": '', "{": '', "}": '',
         "(": '', ")": '', "=": '', "==": '', "<": '', ">": '', "<=": '', ">=": '', "!=": '', "-": '', "+": '', "*": '', "/": ''
    },
    "Stmt": {
        "identifier": 'Expr ;', "number": 'Expr ;', "int": 'Declaration', "float": 'Declaration', "if": 'IfStmt', "else": '', "for": 'ForStmt', "while": 'WhileStmt', ",": '', ".": '', ";": ';', "{": 'CompoundStmt', "}": '',
         "(": 'Expr ;', ")": '', "=": '', "==": '', "<": '', ">": '', "<=": '', ">=": '', "!=": '', "-": 'Expr ;', "+": 'Expr ;', "*": '', "/": ''
    },
    "ForStmt": {
        "identifier": '', "number": '', "int": '', "float": '', "if": '', "else": '', "for": 'for ( Expr ; OptExpr ; OptExpr ) Stmt', "while": '', ",": '', ".": '', ";": '', "{": '', "}": '',
         "(": '', ")": '', "=": '', "==": '', "<": '', ">": '', "<=": '', ">=": '', "!=": '', "-": '', "+": '', "*": '', "/": ''
    },
    "OptExpr": {
        "identifier": '', "number": '', "int": '', "float": '', "if": '', "else": '', "for": '', "while": '', ",": '', ".": '', ";": '', "{": '', "}": '',
         "(": '', ")": '', "=": '', "==": '', "<": '', ">": '', "<=": '', ">=": '', "!=": '', "-": '', "+": '', "*": '', "/": ''
    },
    "WhileStmt": {
        "identifier": '', "number": '', "int": '', "float": '', "if": '', "else": '', "for": '', "while": 'while ( Expr ) Stmt', ",": '', ".": '', ";": '', "{": '', "}": '',
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
        "identifier": '', "number": '', "int": '', "float": '', "if": '', "else": '', "for": '', "while": '', ",": '', ".": '', ";": '', "{": '{ StmtList }', "}": '',
         "(": '', ")": '', "=": '', "==": '', "<": '', ">": '', "<=": '', ">=": '', "!=": '', "-": '', "+": '', "*": '', "/": ''
    },
    "StmtList": {
        "identifier": 'Stmt', "number": 'Stmt', "int": 'Stmt', "float": 'Stmt', "if": 'Stmt', "else": '', "for": 'Stmt', "while": 'Stmt', ",": '', ".": '', ";": 'Stmt', "{": 'Stmt', "}": 'Stmt',
         "(": '', ")": '', "=": '', "==": '', "<": '', ">": '', "<=": '', ">=": '', "!=": '', "-": '', "+": '', "*": '', "/": ''
    },
    "Expr": {
        "identifier": 'identifier = Expr', "number": 'Rvalue', "int": '', "float": '', "if": '', "else": '', "for": '', "while": '', ",": '', ".": '', ";": '', "{": '', "}": '',
         "(": 'Rvalue', ")": '', "=": '', "==": '', "<": '', ">": '', "<=": '', ">=": '', "!=": '', "-": 'Rvalue', "+": 'Rvalue', "*": '', "/": ''
    },
    "Rvalue": {
        "identifier": 'Mag Compare Rvalue', "number": 'Mag Compare Rvalue', "int": '', "float": '', "if": '', "else": '', "for": '', "while": '', ",": '', ".": '', ";": '', "{": '', "}": '',
         "(": 'Mag Compare Rvalue', ")": '', "=": '', "==": '', "<": '', ">": '', "<=": '', ">=": '', "!=": '', "-": 'Mag Compare Rvalue', "+": 'Mag Compare Rvalue', "*": '', "/": ''
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
empilhar(saida, topo(pilha))
print("Pilha inicial:", pilha)

token_index = 0
token_atual = tokens[token_index]

while token_atual[1] != '$':
    print("Token atual: ", token_atual[1])

    if not terminal(topo(pilha)): 
        print("Topo da pilha:", topo(pilha))
        regra_atual = regras_struct[topo(pilha)][token_atual[1]]

        if regra_atual != '':
            print("Regra atual:", regra_atual)

            if not terminal(regra_atual):
                empilhar(saida, regra_atual)
                empilhar(regras, regra_atual)
            pilha.pop()

            vector_regra_atual = regra_atual.split()
            for r in reversed(vector_regra_atual):
                empilhar(pilha, r)
            print("Pilha atualizada:", pilha)
        
        else:
            print("Erro! Token", token_atual[1], "inválido! Regra vazia!")
            break
    else:
        if topo(pilha) == token_atual[1]:
            pilha.pop()

            if token_atual[1] not in topo(regras):
                empilhar(saida, token_atual[1])

            print("It's a Match!! Token", token_atual[1], "removed")
            token_index += 1
            token_atual = tokens[token_index]
            print("Next token will be:", token_atual, "\n")
            if token_atual == []:
                print("Erro! Token", token_atual, "vazio!")
                break
        
        else:
            print("Erro! Token", token_atual[1], "inválido!")
            break

print("\nSaída:")
for item in saida:
    print(item)