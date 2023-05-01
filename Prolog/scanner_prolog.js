const fs = require('fs');


rules = {
    'Az': (str) => {
        return str.toLowerCase() != str.toUpperCase();
    },
    '0-9': (str) => {
        return !isNaN(parseInt(str));
    },
    '(': (str) => {
        return str === '(';
    },
    ')': (str) => {
        return str === ')';
    },
    '+-': (str) => {
        return str === '+' || str === '-';
    },
    '+': (str) => {
        return str === '+';
    },
    '-': (str) => {
        return str === '-';
    },
    'e': (str) => {
        return str === 'e';
    },
    '.': (str) => {
        return str === '.';
    },
    'quotation_marks': (str) => {
        return str === '\"' || str === '\'';
    },
}

input = process.argv[2] + ' '
tokens = []
inline_token = ['(', ')', '.']
initial = 0
states = [0, 1, 2]
final_states = {
    '1': 'identifier',
    '2': 'numeral',
    '3+': 'plus',
    '3-': 'minus',
    '7': 'open_parenthesis',
    '8': 'close_parenthesis',
    '9': 'point',
    '12': 'string',
}
state_transition = {
    '0': [
        { state: '1', rule: 'Az' },
        { state: '2', rule: '0-9' },
        { state: '3+', rule: '+' },
        { state: '3-', rule: '-' },
        { state: '7', rule: '(' },
        { state: '8', rule: ')' },
        { state: '9', rule: '.' },
        { state: '10', rule: 'quotation_marks' }
    ],
    '1': [
        { state: '1', rule: 'Az' },
        { state: '1', rule: '0-9' }
    ],
    '2': [
        { state: '2', rule: '0-9' },
        { state: '5', rule: 'e' },
        { state: '4', rule: '.' },
    ],
    '3+': [
        { state: '2', rule: '0-9' }
    ],
    '3-': [
        { state: '2', rule: '0-9' }
    ],
    '4': [
        { state: '2', rule: '0-9' },
    ],
    '5': [
        { state: '6', rule: '+-' },
    ],
    '6': [
        { state: '2', rule: '0-9' },
    ],
    '7': [
    ],
    '8': [
    ],
    '9': [
    ],
    '10': [
        { state: '11', rule: 'Az' },
        { state: '11', rule: '0-9' },
    ],
    '11': [
        { state: '11', rule: 'Az' },
        { state: '11', rule: '0-9' },
        { state: '12', rule: 'quotation_marks' },
    ],
    '12': [
    ],
}
actual_state = initial
buffer = ''

function getTransition(actual_state, state_transition, input) {
    list_transitions = state_transition[actual_state].map(transition => (rules[transition.rule] && rules[transition.rule](input) && transition['state']))
    list_transitions = list_transitions.filter(t => t !== false)

    if (list_transitions.length > 0) {
        return list_transitions[0]
    }

    return null
}

for (var i = 0; i < input.length; i++) {


    transition = getTransition(actual_state, state_transition, input[i])
    if (transition !== null) {
        actual_state = transition
        buffer += input[i]
    }
    else {
        if (inline_token.includes(input[i])) {
            if (final_states[actual_state]) {
                if (buffer.length > 0) tokens.push([buffer, final_states[actual_state]])
                buffer = input[i]
                actual_state = getTransition(initial, state_transition, input[i])
                continue
            }
        }

        if (input[i] === ' ') {
            if (buffer.length > 0) tokens.push([buffer, final_states[actual_state]])
            buffer = []
            actual_state = initial
            continue
        }
        throw Error('not applicable transition for state: ' + actual_state + 'input[i]: ' + input[i])
    }
}

output = tokens.map(t => t.join(' ')).join('\n')

console.log(output)
fs.writeFileSync("result.txt", output)