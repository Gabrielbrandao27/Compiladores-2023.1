# Gerador de scanner com entrada = expressão regular
# e saída = tabela autômato
import numpy as np
import string
import pickle

f = open("regex_input.txt", "r")
lines = f.read().split("\n")

input = []
for line in lines:
    input.append(line.split(" "))

group_rules = {
    '[a-z]': np.array(list(string.ascii_lowercase)),
    '[A-z]': np.array(list(string.ascii_lowercase+string.ascii_uppercase)),
    '[0-9]': np.array(list(string.digits)),
}
special_operators = '*+?'
is_operand = lambda x: x in special_operators

OPEN_PARENTHESES_DELIMETER = '('
CLOSE_PARENTHESES_DELIMETER = ')'
OPEN_BRACKET_DELIMETER = '['
CLOSE_BRACKET_DELIMETER = ']'

state_transition_table = [{}] # every index is a state, state_transition_table[0] is the 0 state. state_transition_table[0]["a"] is the first transition rule of state 0 with a exact match of "a"
rules_applied_history = [] #[{ rule: "if", resulting_states: [2] }]
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


def exec_operand_rule(rule, actual_states, rule_history):
    if(rule == "*"):
        actual_states = exec_repetition_rule(actual_states, rule_history)
    elif (rule == "+"):
        pass
    elif (rule == "?"):
        actual_states = exec_conditional_rule(actual_states, rule_history)
    
    return actual_states


def exec_conditional_rule(actual_states, rule_history):
    return actual_states + rule_history['states']

def exec_repetition_rule(actual_states, rule_history):
    rule_to_copy = rule_history['states']
    for state in actual_states:
        state_transition_table[state] = state_transition_table[rule_to_copy[0]]
    return actual_states + rule_history['states']


def recursive(token, actuals):
    tokens = tokenize_regex(token)

    actual_states = actuals
    rules_applied_history = [] #[{ rule: "if", resulting_states: [2] }]
    for t in tokens:
        history_object = { 'rule': t, 'states': actual_states}

        if t.startswith(OPEN_PARENTHESES_DELIMETER):
            actual_states = recursive(t[1:-1], actual_states)
        elif t in group_rules:
            print('group rules')
            actual_states = exec_group_rule(t, actual_states)
        elif is_operand(t):
            print('operand rule')
            actual_states = exec_operand_rule(t, actual_states, rules_applied_history[-1])
        else:
            print('strict rule')
            actual_states = exec_strict_rule(t, actual_states)

        rules_applied_history.append(history_object)
    return actual_states



result_final_states = []
inline_tokens = []

for regex in input:
    f_states = recursive(regex[0], [0])

    if regex[2] == '1':
        inline_tokens.append(regex[1])

    r = {
        'token_name': regex[1],
        'final_states': f_states
    }
    result_final_states.append(r)

result = {
    'state_transition_table': state_transition_table,
    'final_states': result_final_states,
    'inline_tokens': inline_tokens
}

print(result['state_transition_table'][0])
with open('result.bin', 'wb') as f:
    pickle.dump(result, f)
