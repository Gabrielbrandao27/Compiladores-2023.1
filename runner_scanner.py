import pickle
import sys


f = open("result.bin", "rb")
regex = pickle.load(f)


final_states = regex['final_states']
state_trasition_table = regex['state_transition_table']
next_state = 0
inline_token = regex['inline_tokens']
separator_token = [' ', '\n']
buffer = ''

tokens = []
text = sys.argv[1] + " "

def return_token_name(state):
    for token in final_states:
        if state in token['final_states']:
            return token['token_name']
        
    return False

for letter in text:
    actual_index = next_state
    actual_state = state_trasition_table[next_state]
    next_state = actual_state.get(letter)
    buffer += letter
    if(next_state == None):
        token_in_buffer_name = return_token_name(actual_index)
        token_name = return_token_name(state_trasition_table[0].get(letter))
        print(token_name)
        if token_name in inline_token:
            if token_name:
                if len(buffer) > 0: tokens.append([buffer, token_in_buffer_name])
                buffer = letter
                next_state = state_trasition_table[0].get(letter)
                continue
        if letter in separator_token:
            if len(buffer) > 0 and token_name: tokens.append([buffer, token_name])
            buffer = ''
            next_state = 0
            continue

        raise Exception(f'no transition for next_state: {actual_index} {actual_state} and letter: {letter}')

print(tokens)

