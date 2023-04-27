# Compiladores-2023.1
Repositório para trabalho da matéria Compiladores

Step 1- Ver a BNF da linguagem e identificar os tokens<br>
Step 2- Fazer as Expressões Regulares para cada token<br>
Step 3- Fazer o Gerador de Scanner que usa de entrada a lista de Expressões Regulares
  e gera de saída uma tabela representando o autômato e também o próprio Scanner<br>
Step 4- Obter a Saída do Scanner, que será uma lista de (token, tipo) e fazer o Parser Top-bottom<br>
Step 5- Para fazer o Parser Top-bottom precisa remover as recursões à esquerda da BNF
  e identificar os First(x) e Follow(x) de cada token<br>
Step 6- Fazer o Parser Top-bottom tomando como entrada a lista de (token, tipo)
  e gerar como saída uma árvore<br>

<h1> A primeira entrega consiste em um gerador de scanners + um parser top-down para a Linguagem Mini-C (um subconjunto da linguagem C</h1>
Sua gramática pode ser encontrada em:<br>
https://github.com/TangoEnSkai/mini-c-compiler-c/blob/master/mini_c.gr<br>
e a gramática completa de C pode ser encontrada em:<br>
https://cs.wmich.edu/~gupta/teaching/cs4850/sumII06/The%20syntax%20of%20C%20in%20Backus-Naur%20form.htm ).<br><br>

Sobre o gerador de scanners: sua entrada deve ser um conjunto de expressões regulares identificadas pelo tipo de token denotado com alguma possível anotação. A saída deverá ser um scanner para os tokens especificados na entrada.

Sobre o parser: sua entrada deverá ser uma lista de tokens gerada pelo scanner correspondente à linguagem Mini-C e sua saída deverá ser uma árvore sintática para o programa dado como entrada ao scanner, em caso de aceitação do programa, ou uma lista de erros, em caso de não-aceitação.

Os entregáveis são:
- Código fonte
- Makefile e/ou intruções de compilação e execução
- Arquivos de exemplos
- Relatório descrevendo a atuação de cada membro, em caso de trabalho feito em dupla (não serão aceitas entregas feitas por mais do que dois componentes)
