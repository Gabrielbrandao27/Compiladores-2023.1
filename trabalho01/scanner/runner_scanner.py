import pickle
import copy
import sys
from utils import check_array_has_only_falsy, check_array_has_only_null

def run_automata(state_trasition_table, next_state, buffer, letter):
    actual_state = state_trasition_table[next_state]
    next_state = actual_state[letter]
    buffer += letter
    return next_state, buffer

def check_automatas_final_states(states, actual_automatas):
    for i in range(len(automatas)):
        if automatas[i] in actual_automatas:
            if states[i] in final_states[automatas[i][1]]:
                return automatas[i][1], i
    
    raise Exception(f'invalid token on line {count_line+1} at {count_char}')
        

def run_automata_inline_token(letter):
    buffers = [''] * len(automatas)
    next_states = [0] * len(automatas)
    actual_automatas = []
    for inline in inline_token:
        i = inline[1]
        try:
            actual_automatas.append(automatas[i])
            n_s, b = run_automata(automatas[i][0], next_states[i], buffers[i], letter)
            next_states[i] = n_s
            buffers[i] = b
        except Exception as e:
            pass
    return check_automatas_final_states(next_states, actual_automatas)

def is_inline_token_name(token_name):
    l = [x for x in inline_token if x[0] == token_name]

    return len(l) == 1

def run_automatas(actual_automatas, letter):
    for i in range(len(automatas)):
        if(automatas[i] in actual_automatas):
            try:
                n_s, b = run_automata(automatas[i][0], next_states[i], buffers[i], letter)
                next_states[i] = n_s
                buffers[i] = b
            except Exception as e:
                actual_automatas[i] = None

def is_separator_token(letter):
    if letter == '\n':
        global count_line
        global count_char
        count_line += 1
        count_char = 0

    return letter in separator_token

# main
f_input_code = open("scanner/input_code.txt", "r")
input = f_input_code.read()
f_input_automata = open("scanner/result.bin", "rb")
regex = pickle.load(f_input_automata)


final_states = regex['final_states']
automatas = regex['automatas']
inline_token = regex['inline_tokens']
separator_token = [' ', '\n']
buffers = [''] * len(automatas)
next_states = [0] * len(automatas)
actual_automatas = copy.deepcopy(automatas)
tokens = []
text = input + " "

count_char = 0
count_line = 0


for letter in text:
    count_char += 1
    if is_separator_token(letter):
        if check_array_has_only_falsy(next_states):
            continue
        token_name, index = check_automatas_final_states(next_states, actual_automatas)

        tokens.append([buffers[index], token_name])

        buffers = [''] * len(automatas)
        next_states = [0] * len(automatas)
        actual_automatas = copy.deepcopy(automatas)
        continue

    run_automatas(actual_automatas, letter)

    if check_array_has_only_null(actual_automatas):
        token_name, index = check_automatas_final_states(next_states, automatas)
        tokens.append([buffers[index], token_name])

        buffers = [''] * len(automatas)
        next_states = [0] * len(automatas)
        actual_automatas = copy.deepcopy(automatas)

        run_automatas(actual_automatas, letter)
        continue



with open('scanner/result.text', 'w') as f:
    file_text = map(lambda x: ' '.join([x[0].strip(), x[1].strip()]).replace('\n', '').strip(), tokens)
    file_text = '\n'.join(file_text)
    f.write(file_text)

