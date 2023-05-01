# Gerador de scanner com entrada = expressão regular
# e saída = tabela autômato
import numpy as np
import string


group_rules = {
    '[a-z]': np.array(list(string.ascii_lowercase)),
    '[A-z]': np.array(list(string.ascii_lowercase+string.ascii_uppercase)),
    '[0-9]': np.array(list(string.digits)),
}

input = "([0-9])*112(([a-z]123)*)?"
input.startswith
special_operators = '*+?'

OPEN_PARENTHESES_DELIMETER = '('
CLOSE_PARENTHESES_DELIMETER = ')'
OPEN_BRACKET_DELIMETER = '['
CLOSE_BRACKET_DELIMETER = ']'


def tokenize_regex(input):
    tokens = []
    buffer = ''
    open_parentheses_delimeter_count = 0
    open_bracket_delimeter_count = 0

    for i in range(len(input)):
        if f'{OPEN_PARENTHESES_DELIMETER}{CLOSE_PARENTHESES_DELIMETER}'.find(input[i]) != -1:
            if input[i] == OPEN_PARENTHESES_DELIMETER:
                if open_parentheses_delimeter_count == 0 and buffer != '':
                    tokens.append(buffer)
                    buffer = ''
                open_parentheses_delimeter_count+= 1
                buffer += input[i]
                continue
            if input[i] == CLOSE_PARENTHESES_DELIMETER:
                open_parentheses_delimeter_count-= 1
                buffer += input[i]
                if open_parentheses_delimeter_count == 0 and buffer != '':
                    tokens.append(buffer)
                    buffer = ''
                continue      
            # tokens.append(input[i])
            # buffer = ''
            continue
        
        
        
        if f'{OPEN_BRACKET_DELIMETER}{CLOSE_BRACKET_DELIMETER}'.find(input[i]) != -1 and open_parentheses_delimeter_count == 0:
            if input[i] == OPEN_BRACKET_DELIMETER:
                if open_bracket_delimeter_count == 0 and buffer != '':
                    tokens.append(buffer)
                    buffer = ''
                open_bracket_delimeter_count+= 1
                buffer += input[i]
                continue
            if input[i] == CLOSE_BRACKET_DELIMETER:
                open_bracket_delimeter_count-= 1
                if open_bracket_delimeter_count == 0 and buffer != '':
                    buffer += input[i]
                    tokens.append(buffer)
                    buffer = ''
                    continue
        
        if special_operators.find(input[i]) != -1 and open_parentheses_delimeter_count == 0:
            tokens.append(input[i])
            buffer = ''
            continue
        
        
        buffer += input[i]
    if buffer != '':
        tokens.append(buffer)

    return tokens


def recursive(token):
    tokens = tokenize_regex(token)

    for t in tokens:
        print(t)
        if t.startswith(OPEN_PARENTHESES_DELIMETER):
            recursive(t[1:-1])



print(input)
recursive(input)
