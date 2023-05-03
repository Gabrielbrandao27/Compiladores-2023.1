# Um parser que recebe a lista de tokens e tipos e retorna a árvore sintática

tokens = [['(', '('], [')', ')'], ['{', '{'], ['}', '}'], [',', ','], ['.', '.'], [';', ';'], 
         ['=', '='], ['==', '=='], ['<', '<'], ['>', '>'], ['<=', '<='], ['>=', '>='], 
         ['!=', '!='], ['+', '+'], ['-', '-'], ['*', '*'], ['/', '/'], ['1234', 'int'], 
         ['12.34', 'float'], ['for', 'for'], ['while', 'while'], ['if', 'if'], 
         ['else', 'else'], ['var1', 'identifier'], ['123', 'number']]

pilha = []

for token in tokens:
    pilha.append[token[0]]