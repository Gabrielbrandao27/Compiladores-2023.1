pilha = []
saida = []
regras = []

context_counter = 0

def empilhar(pilha, item):
    return pilha.append(item)

def topo(pilha):
    return pilha[-1]

def terminal(item):
    for i in regras_struct:
        if item in regras_struct[i]:
            return True
        
def backtracking(regra_atual, token_atual, pilha, saida):

    producoes = regra_atual.split(' | ')
    print("Producoes: ", producoes)
    
    for producao in producoes:

        print("Producao: ", producao)
        if producao == 'ε':
            print("Regra ε desempilha o topo")
            pilha.pop()
            return True
        
        elif producao in tokens_struct.values():
            pilha.pop()
            print("Pilha atualizada: ", pilha)

            if token_atual[1] not in topo(regras):
                empilhar(saida, token_atual[1])

            print("It's a Match!! Token", token_atual[1], "removed")

            return True

        
        elif producao in simbolos.values():

            producao = regras_struct[regra_atual][token_atual]
            vector_regra_atual = producao.split()

            for r in reversed(vector_regra_atual):
                empilhar(pilha, r)

            print("Pilha atualizada:", pilha)
            producao = topo(pilha)

            if backtracking(producao, token_atual, pilha, saida):
                return True
        
        else:
            pilha.pop()
            vector_regra_atual = producao.split()

            for r in reversed(vector_regra_atual):
                empilhar(pilha, r)

            print("Pilha atualizada:", pilha)
            producao = topo(pilha)

            if backtracking(producao, token_atual, pilha, saida):
                return True
        


input = open("scanner/result.text", "r")
tokens_line = input.read().split('\n')
tokens = []
for token_line in tokens_line:
    tokens.append(token_line.split())

fim_delim = ['$', '$']
tokens.append(fim_delim)

print("Tokens: ", tokens)

simbolos = {
    0 : "Function", 
    1 : "ArgList",
    2 : "ArgList2",
    3 : "Arg", 
    4 : "Declaration", 
    5 : "Type", 
    6 : "IdentList",
    7 : "IdentList2",
    8 : "Stmt", 
    9 : "ForStmt", 
    10 : "OptExpr", 
    11 : "whileStmt", 
    12 : "IfStmt", 
    13 : "ElsePart", 
    14 : "CompoundStmt", 
    15 : "StmtList",
    16 : "StmtList2",
    17 : "Expr", 
    18 : "Rvalue",
    19 : "Rvalue2",
    20 : "Compare", 
    21 : "Mag", 
    22 : "Mag2",
    23 : "Term", 
    24 : "Term2",
    25 : "Factor"
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


context_list = ["global"]

tabela_simbolo = {} #\ 
def function_rule(tokens):
    global context_list
    tabela_simbolo[tokens[1][0]] = {
        'tipo': tokens[0][1],
        'contexto': context_list[-1]
    }

    context_list.append(tokens[1][0])

def stmt_rule(tokens):
    global context_list
    context_list.pop()


regras_func = {
    "Function": function_rule,
    "StmtList": stmt_rule
}


regras_struct = {
    "Function": {
        "identifier": '', "number": '', "int": 'Type identifier ( ArgList ) CompoundStmt', "float": 'Type identifier ( ArgList ) CompoundStmt', "if": '', "else": '', "for": '', "while": '', ",": '', ".": '', ";": '', "{": '', "}": '',
         "(": '', ")": '', "=": '', "==": '', "<": '', ">": '', "<=": '', ">=": '', "!=": '', "-": '', "+": '', "*": '', "/": ''
    },
    "ArgList": {
        "identifier": '', "number": '', "int": 'Arg ArgList2', "float": 'Arg ArgList2', "if": '', "else": '', "for": '', "while": '', ",": '', ".": '', ";": '', "{": '', "}": '',
         "(": '', ")": '', "=": '', "==": '', "<": '', ">": '', "<=": '', ">=": '', "!=": '', "-": '', "+": '', "*": '', "/": ''
    },
    "ArgList2": {
        "identifier": '', "number": '', "int": '', "float": '', "if": '', "else": '', "for": '', "while": '', ",": ', Arg ArgList2', ".": '', ";": '', "{": '', "}": '',
         "(": '', ")": 'ε', "=": '', "==": '', "<": '', ">": '', "<=": '', ">=": '', "!=": '', "-": '', "+": '', "*": '', "/": ''
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
        "identifier": 'identifier IdentList2', "number": '', "int": '', "float": '', "if": '', "else": '', "for": '', "while": '', ",": '', ".": '', ";": '', "{": '', "}": '',
         "(": '', ")": '', "=": '', "==": '', "<": '', ">": '', "<=": '', ">=": '', "!=": '', "-": '', "+": '', "*": '', "/": ''
    },
    "IdentList2": {
        "identifier": '', "number": '', "int": '', "float": '', "if": '', "else": '', "for": '', "while": '', ",": ', IdentList', ".": '', ";": 'ε', "{": '', "}": '',
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
        "identifier": 'Expr', "number": 'Expr', "int": '', "float": '', "if": '', "else": '', "for": '', "while": '', ",": '', ".": '', ";": 'ε', "{": '', "}": '',
         "(": 'Expr', ")": 'ε', "=": '', "==": '', "<": '', ">": '', "<=": '', ">=": '', "!=": '', "-": 'Expr', "+": 'Expr', "*": '', "/": ''
    },
    "WhileStmt": {
        "identifier": '', "number": '', "int": '', "float": '', "if": '', "else": '', "for": '', "while": 'while ( Expr ) Stmt', ",": '', ".": '', ";": '', "{": '', "}": '',
         "(": '', ")": '', "=": '', "==": '', "<": '', ">": '', "<=": '', ">=": '', "!=": '', "-": '', "+": '', "*": '', "/": ''
    },
    "IfStmt": {
        "identifier": '', "number": '', "int": '', "float": '', "if": 'if ( Expr ) Stmt ElsePart', "else": '', "for": '', "while": '', ",": '', ".": '', ";": '', "{": '', "}": '',
         "(": '', ")": '', "=": '', "==": '', "<": '', ">": '', "<=": '', ">=": '', "!=": '', "-": '', "+": '', "*": '', "/": ''
    },
    "ElsePart": {
        "identifier": 'ε', "number": '', "int": 'ε', "float": 'ε', "if": 'ε', "else": 'else Stmt | ε', "for": 'ε', "while": 'ε', ",": '', ".": '', ";": 'ε', "{": 'ε', "}": 'ε',
         "(": '', ")": '', "=": '', "==": '', "<": '', ">": '', "<=": '', ">=": '', "!=": '', "-": '', "+": '', "*": '', "/": ''
    },
    "CompoundStmt": {
        "identifier": '', "number": '', "int": '', "float": '', "if": '', "else": '', "for": '', "while": '', ",": '', ".": '', ";": '', "{": '{ StmtList }', "}": '',
         "(": '', ")": '', "=": '', "==": '', "<": '', ">": '', "<=": '', ">=": '', "!=": '', "-": '', "+": '', "*": '', "/": ''
    },
    "StmtList": {
        "identifier": 'Stmt StmtList2', "number": 'Stmt StmtList2', "int": 'Stmt StmtList2', "float": 'Stmt StmtList2', "if": 'Stmt StmtList2', "else": '', "for": 'Stmt StmtList2', "while": 'Stmt StmtList2', ",": '', ".": '', ";": 'Stmt StmtList2', "{": 'Stmt StmtList2', "}": '',
         "(": '', ")": '', "=": '', "==": '', "<": '', ">": '', "<=": '', ">=": '', "!=": '', "-": 'Stmt StmtList2', "+": 'Stmt StmtList2', "*": '', "/": ''
    },
    "StmtList2": {
        "identifier": 'StmtList', "number": 'StmtList', "int": 'StmtList', "float": 'StmtList', "if": 'StmtList', "else": '', "for": 'StmtList', "while": 'StmtList', ",": '', ".": '', ";": 'StmtList', "{": 'StmtList', "}": 'ε',
         "(": 'StmtList', ")": '', "=": '', "==": '', "<": '', ">": '', "<=": '', ">=": '', "!=": '', "-": 'StmtList', "+": 'StmtList', "*": '', "/": ''
    },
    "Expr": {
        "identifier": 'identifier = Expr | Rvalue', "number": 'Rvalue', "int": '', "float": '', "if": '', "else": '', "for": '', "while": '', ",": '', ".": '', ";": '', "{": '', "}": '',
         "(": 'Rvalue', ")": '', "=": '', "==": '', "<": '', ">": '', "<=": '', ">=": '', "!=": '', "-": 'Rvalue', "+": 'Rvalue', "*": '', "/": ''
    },
    "Rvalue": {
        "identifier": 'Mag Rvalue2', "number": 'Mag Rvalue2', "int": '', "float": '', "if": '', "else": '', "for": '', "while": '', ",": '', ".": '', ";": '', "{": '', "}": '',
         "(": 'Mag Rvalue2', ")": '', "=": '', "==": '', "<": '', ">": '', "<=": '', ">=": '', "!=": '', "-": 'Mag Rvalue2', "+": 'Mag Rvalue2', "*": '', "/": ''
    },
    "Rvalue2": {
        "identifier": '', "number": '', "int": '', "float": '', "if": '', "else": '', "for": '', "while": '', ",": '', ".": '', ";": 'ε', "{": '', "}": '',
         "(": '', ")": 'ε', "=": '', "==": 'Compare Rvalue', "<": 'Compare Rvalue', ">": 'Compare Rvalue', "<=": 'Compare Rvalue', ">=": 'Compare Rvalue', "!=": 'Compare Rvalue', "-": '', "+": '', "*": '', "/": ''
    },
    "Compare": {
        "identifier": '', "number": '', "int": '', "float": '', "if": '', "else": '', "for": '', "while": '', ",": '', ".": '', ";": '', "{": '', "}": '',
         "(": '', ")": '', "=": '', "==": '==', "<": '<', ">": '>', "<=": '<=', ">=": '>=', "!=": '!=', "-": '', "+": '', "*": '', "/": ''
    },
    "Mag": {
        "identifier": 'Term Mag2', "number": 'Term Mag2', "int": '', "float": '', "if": '', "else": '', "for": '', "while": '', ",": '', ".": '', ";": '', "{": '', "}": '',
         "(": 'Term Mag2', ")": '', "=": '', "==": '', "<": '', ">": '', "<=": '', ">=": '', "!=": '', "-": 'Term Mag2', "+": 'Term Mag2', "*": '', "/": ''
    },
    "Mag2": {
        "identifier": '', "number": '', "int": '', "float": '', "if": '', "else": '', "for": '', "while": '', ",": '', ".": '', ";": 'ε', "{": '', "}": '',
         "(": '', ")": 'ε', "=": '', "==": '', "<": '', ">": '', "<=": '', ">=": '', "!=": '', "-": '- Term Mag2', "+": '+ Term Mag2', "*": '', "/": ''
    },
    "Term": {
        "identifier": 'Factor Term2', "number": 'Factor Term2', "int": '', "float": '', "if": '', "else": '', "for": '', "while": '', ",": '', ".": '', ";": '', "{": '', "}": '',
         "(": 'Factor Term2', ")": '', "=": '', "==": '', "<": '', ">": '', "<=": '', ">=": '', "!=": '', "-": 'Factor Term2', "+": 'Factor Term2', "*": '', "/": ''
    },
    "Term2": {
        "identifier": '', "number": '', "int": '', "float": '', "if": '', "else": '', "for": '', "while": '', ",": '', ".": '', ";": 'ε', "{": '', "}": '',
         "(": '', ")": 'ε', "=": '', "==": '', "<": '', ">": '', "<=": '', ">=": '', "!=": '', "-": '', "+": '', "*": '* Factor Term2', "/": '/ Factor Term2'
    },
    "Factor": {
        "identifier": 'identifier', "number": 'number', "int": '', "float": '', "if": '', "else": '', "for": '', "while": '', ",": '', ".": '', ";": '', "{": '', "}": '',
         "(": '( Expr )', ")": '', "=": '', "==": '', "<": '', ">": '', "<=": '', ">=": '', "!=": '', "-": '- Factor', "+": '+ Factor', "*": '', "/": ''
    }
}

follow_simb = {
   "Function" : '$',
   "ArgList" : ')',
   "ArgList2" : ')',
   "Arg" : ', | )',
   "Declaration" : 'else | identifier | int | float | if | for | while | ; | { | }',
   "Type" : 'identifier',
   "IdentList" : ';',
   "IdentList2" : ';',
   "Stmt" : 'else | identifier | int | float | if | for | while | ; | { | }',
   "ForStmt" : 'else | identifier | int | float | if | for | while | ; | { | }',
   "OptExpr" : '; | )',
   "whileStmt" : 'else | identifier | int | float | if | for | while | ; | { | }',
   "IfStmt" : 'else | identifier | int | float | if | for | while | ; | { | }',
   "ElsePart" : 'else | identifier | int | float | if | for | while | ; | { | }',
   "CompoundStmt" : '} | $',
   "StmtList" : '}',
   "StmtList2" : '}',
   "Expr" : '; | ) | }',
   "Rvalue" : '; | )',
   "Rvalue2" : '; | )',
   "Compare" : '',
   "Mag" : '; | )',
   "Mag2" : '; | )',
   "Term" : '+ | - | ; | )',
   "Term2" : '+ | - | ; | )',
   "Factor" : '* | / | + | - | ; | )' 
}

first_simb = {
    "Function" : 'int | float',
    "ArgList" : 'int | float',
    "ArgList2" : ', | ε',
    "Arg" : 'int | float',
    "Declaration" : 'int | float',
    "Type" : 'int | float',
    "IdentList" : 'identifier',
    "IdentList2" : ', | ε',
    "Stmt" : 'identifier | number | int | float | if | for | while | ; | { | ( | - | +',
    "ForStmt" : 'for',
    "OptExpr" : 'identifier | number | ( | - | + | ε',
    "whileStmt" : 'while',
    "IfStmt" : 'if',
    "ElsePart" : 'else | ε',
    "CompoundStmt" : '{',
    "StmtList" : 'identifier | number | int | float | if | for | while | ; | { | ( | - | +',
    "StmtList2" : 'identifier | number | int | float | if | for | while | ; | { | ( | - | + | ε',
    "Expr" : 'identifier | number | ( | - | +',
    "Rvalue" : 'identifier | number | ( | - | +', 
    "Rvalue2" : '== | < | > | <= | >= | != | ε',
    "Compare" : '== | < | > | <= | >= | !=',
    "Mag" : 'identifier | number | ( | - | +',
    "Mag2" : '+ | - | ε',
    "Term" : 'identifier | number | ( | - | +',
    "Term2" : '* | / | ε',
    "Factor" : 'identifier | number | ( | - | +'
}   

empilhar(pilha, '$')
empilhar(pilha, simbolos[0])
empilhar(saida, f'{topo(pilha)}->{regras_struct[simbolos[0]][tokens[0][1]]}')
print("Pilha inicial:", pilha)

token_index = 0
token_atual = tokens[token_index]

while token_atual[1] != '$':
    print("Token atual: ", token_atual[1])
    

    if not terminal(topo(pilha)):

        print("Topo da pilha:", topo(pilha))
        empilhar(regras, topo(pilha))
        regra_atual = regras_struct[topo(pilha)][token_atual[1]]
        f = regras_func.get(topo(pilha))
        if f: f((tokens[token_index:]))
        print("Regra atual: ", regra_atual)

        if regra_atual != '':

            if regra_atual == 'ε':
                pilha.pop()
                print("Regra ε desempilha o topo")

            elif '|' in regra_atual:
                backtracking(regra_atual, token_atual, pilha, saida)
                token_index += 1
                token_atual = tokens[token_index]
                print("Next token will be:", token_atual[1], "\n")

                if token_atual == []:
                    print("Erro! Token", token_atual, "vazio!")
                    break
            
            else:
                print("Regra atual:", regra_atual)

                if not terminal(regra_atual):
                    if '->' in topo(saida):
                        aux = topo(saida).split('->')
                        if not terminal(topo(aux)):
                            empilhar(saida, f'{topo(aux)}->{regra_atual}')
                        else:
                            for key1, inner_dict in regras_struct.items():
                                if inner_dict.get(token_atual[1]) == regra_atual:
                                    pai = key1
                            empilhar(saida, f'{pai}->{regra_atual}')
                    empilhar(regras, regra_atual)
                    
                pilha.pop()

                vector_regra_atual = regra_atual.split()

                for r in reversed(vector_regra_atual):
                    empilhar(pilha, r)

                print("Pilha atualizada:", pilha)

        else:
            print("Erro! Token", token_atual[1], "inválido! Regra vazia!")

            if token_atual[1] in follow_simb[topo(pilha)]:
                print("Desempilhando", topo(pilha))
                pilha.pop()

            else:
                print("Avançando a entrada de tokens procurando um token válido")
                
                while (token_atual[1] not in first_simb[topo(pilha)] and token_atual[1] not in follow_simb[topo(pilha)]):
                    token_index += 1
                    token_atual = tokens[token_index]
            
    else:
        if topo(pilha) == token_atual[1]:
            pilha.pop()

            if token_atual[1] not in topo(regras) and token_atual[1] in regras_struct[topo(regras)][token_atual[1]]:
                empilhar(saida, f'{topo(regras)}->{token_atual[1]}')

            print("It's a Match!! Token", token_atual[1], "removed")
            token_index += 1
            token_atual = tokens[token_index]
            print("Next token will be:", token_atual[1], "\n")

            if token_atual == []:
                print("Erro! Token", token_atual, "vazio!")
                break
        
        else:
            print("Erro! Token", token_atual[1], "inválido!")
            break

print(tabela_simbolo)
print(tokens)
# print("\nSaída:")

# for item in saida:
#     print(item)