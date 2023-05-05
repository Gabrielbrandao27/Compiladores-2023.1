# Um parser que recebe a lista de tokens e tipos e retorna a árvore sintática
pilha = []

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
    if item in tokens_struct:
        return True
    
tokens = [['(', '('], [')', ')'], ['{', '{'], ['}', '}'], [',', ','], ['.', '.'], [';', ';'], 
         ['=', '='], ['==', '=='], ['<', '<'], ['>', '>'], ['<=', '<='], ['>=', '>='], 
         ['!=', '!='], ['+', '+'], ['-', '-'], ['*', '*'], ['/', '/'], ['1234', 'int'], 
         ['12.34', 'float'], ['for', 'for'], ['while', 'while'], ['if', 'if'], 
         ['else', 'else'], ['var1', 'identifier'], ['123', 'number'], '$']

simbolos = {
    "Function" : "0",
    "ArgList" : "1",
    "Arg" : "2",
    "Declaration" : "3",
    "Type" : "4",
    "IdentList" : "5",
    "Stmt" : "6",
    "ForStmt" : "7",
    "OptExpr" : "8",
    "whileStmt" : "9",
    "IfStmt" : "10",
    "ElsePart" : "11",
    "CompoundStmt" : "12",
    "StmtList" : "13",
    "Expr" : "14",
    "Rvalue" : "15",
    "Compare" : "16",
    "Mag" : "17",
    "Term" : "18",
    "Factor" : "19"
}

tokens_struct = {
    'identifier': 0,
    'number': 1,
    'int': 2,
    'float': 3,
    'if': 4,
    'else': 5,
    'for': 6,
    'while': 7,
    ',': 8,
    '.': 9,
    ';': 10,
    '{': 11,
    '}': 12,
    '(': 13,
    ')': 14,
    '=': 15,
    '==': 16,
    '<': 17,
    '>': 18,
    '<=': 19,
    '>=': 20,
    '!=': 21,
    '-': 22,
    '+': 23,
    '*': 24,
    '/': 25,
}

lista_regras = [[None] * len(tokens_struct) for i in range(len(simbolos))]

for i in range(len(simbolos)):
    for j in range(len(tokens_struct)):
        lista_regras[i][j] = "ok"

#print(lista_regras)


iterator = iter(simbolos.keys())
primeira_chave = next(iterator)


empilhar(pilha, '$')
empilhar(pilha, primeira_chave)

regra = ''

for index, token in enumerate(tokens):
    token_atual = token
    if index < len(tokens)-1:
      prox_token = tokens[index+1]
    else:
        prox_token = None


    while topo(pilha) != '$' and prox_token != '$':
        
        i = int(simbolos.get(topo(pilha)))
        j = int(tokens_struct.get(token_atual[1]))
        print("i: ", i, "j: ", j)
        regra = lista_regras[i][j]
        pilha.pop()
        print("Regra: ", regra)
        
for r in reversed(regra):
    empilhar(pilha, r)
    print(pilha)