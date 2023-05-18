# Gerador de scanner com entrada = expressão regular
# e saída = tabela autômato
import numpy as np
import string
import pickle

f = open("scanner/input_regex.txt", "r")
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
is_operand = lambda x: x in special_operators # função anônima que toma x como param e 
# se x for um special_operator retorna True
is_escape = lambda x: x.startswith("\\") # função anônima que toma x como param e 

OPEN_PARENTHESES_DELIMETER = '('
CLOSE_PARENTHESES_DELIMETER = ')'
OPEN_BRACKET_DELIMETER = '['
CLOSE_BRACKET_DELIMETER = ']'

# state_transition_table = [{}] # every index is a state. And state_transition_table[0] is the 0 state. 
# state_transition_table[0]["a"] is the first transition rule of state 0 with a exact match of "a"
rules_applied_history = [] #[{ rule: "if", resulting_states: [2] }]
#each state can have 

def tokenize_regex(input):
    tokens = []
    buffer = ''
    open_parentheses_delimeter_count = 0
    open_bracket_delimeter_count = 0

    for i in range(len(input)):
        if len(buffer) > 0 and is_escape(buffer[-1]):
            buffer += input[i]
            continue

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

def exec_group_rule(rule, actual_states, state_transition_table):
    target_rules = group_rules[rule]
    
    target_states = set()
    for state in actual_states:
        state_transition_table.append({})
        new_state_index = len(state_transition_table)-1
        for rule in target_rules:
            if state_transition_table[state].get(rule) is None:
                state_transition_table[state][rule] = new_state_index
                target_states.add(new_state_index)
    return list(target_states)

def exec_strict_rule(rule, actual_states, state_transition_table):
    target_rules = rule

    target_states = actual_states
    for rule in target_rules:
        mid_states = []
        if is_escape(rule):
            continue

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


def exec_operand_rule(rule, actual_states, rule_history, state_transition_table):
    if(rule == "*"):
        actual_states = exec_repetition_rule(actual_states, rule_history, state_transition_table)
    elif (rule == "+"):
        actual_states = exec_add_rule(actual_states, rule_history)
    elif (rule == "?"):
        actual_states = exec_conditional_rule(actual_states, rule_history)
    
    return actual_states

def exec_add_rule(_, rule_history):
    return rule_history['states']

def exec_conditional_rule(actual_states, rule_history):
    return actual_states + rule_history['states']

def exec_repetition_rule(actual_states, rule_history, state_transition_table):
    for state in rule_history['states']:
        for cur_state in actual_states:
            print(cur_state)
            if state_transition_table[cur_state].get('ε') is None:
                state_transition_table[cur_state]['ε'] = state

    return actual_states + rule_history['states']

def recursive(token, actuals, state_transition_table):
    tokens = tokenize_regex(token)

    actual_states = actuals
    rules_applied_history = [] #[{ rule: "if", resulting_states: [2] }]
    for t in tokens:
        history_object = { 'rule': t, 'states': actual_states}

        if is_escape(t):
            actual_states = exec_strict_rule(t, actual_states, state_transition_table)
        elif t.startswith(OPEN_PARENTHESES_DELIMETER):
            actual_states, _ = recursive(t[1:-1], actual_states, state_transition_table)
        elif t in group_rules:
            actual_states = exec_group_rule(t, actual_states, state_transition_table)
        elif is_operand(t):
            actual_states = exec_operand_rule(t, actual_states, rules_applied_history[-1], state_transition_table)
        else:
            actual_states = exec_strict_rule(t, actual_states, state_transition_table)

        if len(rules_applied_history) > 1 and rules_applied_history[-1]['rule'] == '+' and not is_escape(t):
            actual_states = actual_states + rules_applied_history[-1]['states']

        rules_applied_history.append(history_object)
    return actual_states, state_transition_table


def minimize(state_transition_table):
    actual_state = state_transition_table[0]
    transitions = actual_state.keys()

    visited_states = [0]

    for transition in transitions:
        depth_minimize(state_transition_table,visited_states,  0, actual_state[transition])

def depth_minimize(state_transition_table,visited_states, last_state, state, to_copy = None):
    actual_state = state_transition_table[state]
    epsilon_transition = actual_state.get('ε')
    transitions = actual_state.keys()
    if state not in visited_states:
        visited_states.append(state)
        if epsilon_transition != None or to_copy:
            copy_key_obj = to_copy or state_transition_table[epsilon_transition]
            for key in copy_key_obj.keys():
                if actual_state.get(key) is None:
                    actual_state[key] = copy_key_obj[key]
            if epsilon_transition != None: del actual_state['ε']
            to_copy = state_transition_table[last_state]
        for transition in transitions:
            depth_minimize(state_transition_table,visited_states,  state, actual_state[transition], to_copy)


def get_conflict_dictionary(dict1, dict2):
    conflicting_key = []
    for key in dict1.keys():
        if dict2.get(key) is not None:
            conflicting_key.append(key)
    return conflicting_key

def safe_get (l, idx, default=None):
  try:
    return l[idx]
  except IndexError:
    return default

result_final_states = {}
inline_tokens = []

automatas = []

for i in range(len(input)):
    f_states, state_transition_table = recursive(input[i][0], [0], [{}])


    minimize(state_transition_table)

    #print(input[i][0], ' ', state_transition_table)
    automatas.append([state_transition_table, input[i][1]])

    if input[i][2] == '1':
        inline_tokens.append([input[i][1], i])


    result_final_states[input[i][1]] = f_states


result = {
    'automatas': automatas,
    'final_states': result_final_states,
    'inline_tokens': inline_tokens
}
print(result)

with open('scanner/result.bin', 'wb') as f:
    pickle.dump(result, f)
