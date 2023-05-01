# Gerador de scanner com entrada = expressão regular
# e saída = tabela autômato
import numpy as np
import string


group_rules = {
    '[a-z]': np.array(list(string.ascii_lowercase)),
    '[A-z]': np.array(list(string.ascii_lowercase+string.ascii_uppercase)),
    '[0-9]': np.array(list(string.digits)),
}

input = "if(a)?"
special_operators = '*+?'
is_operand = lambda x: x in special_operators

OPEN_PARENTHESES_DELIMETER = '('
CLOSE_PARENTHESES_DELIMETER = ')'
OPEN_BRACKET_DELIMETER = '['
CLOSE_BRACKET_DELIMETER = ']'

state_transition_table = [{}] # every index is a state, state_transition_table[0] is the 0 state. state_transition_table[0]["a"] is the first transition rule of state 0 with a exact match of "a"
#each state can have 

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

def exec_group_rule(rule, actual_states):
    target_rules = group_rules[rule]

    target_states = []
    for state in actual_states:
        for rule in target_rules:
            if state_transition_table[state].get(rule) is None:
                state_transition_table.append({})
                new_state_index = len(state_transition_table)-1
                state_transition_table[state][rule] = new_state_index
                target_states.append(new_state_index)
            else:
                target_states.append(state_transition_table[state][rule])
    
    return target_states

def exec_strict_rule(rule, actual_states):
    target_rules = rule

    target_states = actual_states
    for rule in target_rules:
        mid_states = []
        for state in target_states:
            if state_transition_table[state].get(rule) is None:
                state_transition_table.append({})
                new_state_index = len(state_transition_table)-1
                state_transition_table[state][rule] = new_state_index
                mid_states.append(new_state_index)
            else:
                mid_states.append(state_transition_table[state][rule])
        target_states = mid_states

    return target_states


def exec_operand_rule(rule, actual_states):
    if(rule == "*"):
        pass
    elif (rule == "+"):
        pass
    elif (rule == "?"):
        pass
        # exec_conditional_rule(rule, actual_states)
    else:
        return actual_states


# def exec_conditional_rule(rule, actual_states):



def recursive(token, actuals):
    tokens = tokenize_regex(token)

    actual_states = actuals
    for t in tokens:
        print(t)
        if t.startswith(OPEN_PARENTHESES_DELIMETER):
            recursive(t[1:-1], actual_states)
        elif t in group_rules:
            print('group rules')
            actual_states = exec_group_rule(t, actual_states)
        elif is_operand(t):
            print('operand rule')
            exec_operand_rule(t, actual_states)
        else:
            actual_states = exec_strict_rule(t, actual_states)
            print('strict rule')

    return actual_states



final_states = recursive(input, [0])
print(final_states)
print(state_transition_table)