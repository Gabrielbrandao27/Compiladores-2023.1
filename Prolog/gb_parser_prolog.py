with open("gb_output_scanner_prolog.txt", "r") as f:
    file_content = f.read()
tokens = eval(file_content)
pilha = []

def vazia(pilha):
    return pilha == []

def empilhar(pilha, item):
    return pilha.append(item)

def remover(pilha, item):
    return pilha.pop(item)

def topo(pilha):
    return pilha[-1]

def tamanho(pilha):
    return len(pilha)

def posicao(pilha, item):
    indice = len(pilha) - 1 - pilha[::-1].index(item)
    return indice

