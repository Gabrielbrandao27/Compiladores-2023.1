import pickle
import sys


f = open("scanner/input_code.txt", "r")
input = f.read()

f = open("scanner/result.bin", "rb")
regex = pickle.load(f)


final_states = regex['final_states']
state_trasition_table = regex['state_transition_table']
next_state = 0
inline_token = regex['inline_tokens']
separator_token = [' ', '\n']
buffer = ''

tokens = []
text = input + " "

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
        if token_name in inline_token:
            if token_name:
                if len(buffer) > 0 and token_in_buffer_name: tokens.append([buffer[0:-1], token_in_buffer_name])
                buffer = letter
                next_state = state_trasition_table[0].get(letter)
                continue
        token_in_buffer_name = return_token_name(actual_index)
        if letter in separator_token and token_in_buffer_name:
            if len(buffer) > 0 and token_in_buffer_name: tokens.append([buffer, token_in_buffer_name])
            buffer = ''
            next_state = 0
            continue

        
        raise Exception(f'invalid token {buffer}')


with open('scanner/result.text', 'w') as f:
    file_text = map(lambda x: ' '.join([x[0].strip(), x[1].strip()]).replace('\n', '').strip(), tokens)
    file_text = '\n'.join(file_text)
    print(file_text)
    f.write(file_text)

