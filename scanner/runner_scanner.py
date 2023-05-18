import pickle
import copy
import sys


f = open("scanner/input_code.txt", "r")
input = f.read()

f = open("scanner/result.bin", "rb")
regex = pickle.load(f)


final_states = regex['final_states']
automatas = regex['automatas']
inline_token = regex['inline_tokens']
separator_token = [' ', '\n']
buffers = [''] * len(automatas)
next_states = [0] * len(automatas)
actual_automatas = copy.deepcopy(automatas)
tokens = []


text = input + " "

def return_token_name(state, result_final_states):
    if state in result_final_states['final_states']:
        return result_final_states['token_name']
        
    return False


def run_automata(state_trasition_table, next_state, buffer, letter):
    #print('state_transition_table: ', state_trasition_table)
    #print('next_state: ',next_state)
    #print('buffer: ',buffer)
    actual_state = state_trasition_table[next_state]
    next_state = actual_state[letter]
    buffer += letter
    #print('next_state 1: ',next_state)
    # if(next_state == None):
    #     raise Exception(f'invalid token {buffer}')
    return next_state, buffer

def check_automatas_final_states(states, actual_automatas):
    for i in range(len(automatas)):
        # print('automatas: ', automatas[i])
        # print('actual_automatas: ', actual_automatas)
        if automatas[i] in actual_automatas:
            # print('automatas: ', automatas[i])
            if states[i] in final_states[automatas[i][1]]:
                return automatas[i][1], i
    
    raise Exception('invalid final state')
        

def run_automata_inline_token(letter):
    buffers = [''] * len(automatas)
    next_states = [0] * len(automatas)
    actual_automatas = []
    for inline in inline_token:
        i = inline[1]
        try:
            print('inline letter :', letter)
            actual_automatas.append(automatas[i])
            n_s, b = run_automata(automatas[i][0], next_states[i], buffers[i], letter)
            print('inline success')
            next_states[i] = n_s
            buffers[i] = b
        except Exception as e:
            print('inline error ', e)
    
    return check_automatas_final_states(next_states, actual_automatas)

def check_array_has_only_null(arr):
    not_null_array = [x for x in arr if x is not None]

    return not len(not_null_array)

def check_array_has_only_falsy(arr):
    not_null_array = [x for x in arr if x ]

    return not len(not_null_array)

for letter in text:
    # token_in_buffer_name = return_token_name(n_s, final_states[i])

    if letter in separator_token:
        if check_array_has_only_falsy(next_states):
            continue
        token_name, index = check_automatas_final_states(next_states, actual_automatas)

        tokens.append([buffers[index], token_name])

        buffers = [''] * len(automatas)
        next_states = [0] * len(automatas)
        actual_automatas = copy.deepcopy(automatas)

        continue
    for i in range(len(automatas)):
        # print(automatas[i])
        if(automatas[i] in actual_automatas):
            try:
                n_s, b = run_automata(automatas[i][0], next_states[i], buffers[i], letter)
                next_states[i] = n_s
                buffers[i] = b
            except Exception as e:
                actual_automatas[i] = None
    if check_array_has_only_null(actual_automatas):
        print('buffers ', buffers)
        print('next_states ', next_states)
        print('has only null')

        token_name, index = check_automatas_final_states(next_states, automatas)
        tokens.append([buffers[index], token_name])

        inline_token_name, index = run_automata_inline_token(letter)
        tokens.append([letter, inline_token_name])

        buffers = [''] * len(automatas)
        next_states = [0] * len(automatas)
        actual_automatas = copy.deepcopy(automatas)
        print(tokens)
        continue



print(tokens)


with open('scanner/result.text', 'w') as f:
    file_text = map(lambda x: ' '.join([x[0].strip(), x[1].strip()]).replace('\n', '').strip(), tokens)
    file_text = '\n'.join(file_text)
    f.write(file_text)

