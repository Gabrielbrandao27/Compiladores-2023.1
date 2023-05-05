# Compiladores-2023.1
Repositório para trabalho da matéria Compiladores

Step 1- Ver a BNF da linguagem e identificar os tokens<br>
Step 2- Fazer as Expressões Regulares para cada token<br>
Step 3- Fazer o Gerador de Scanner que usa de entrada a lista de Expressões Regulares
  e gera de saída uma tabela representando o autômato<br>
Step 4- Fazer o Scanner que recebe a tabela do gerador de Scanner e a saída do Scanner será uma lista de (token, tipo)<br>
  e fazer o Parser Top-bottom<br>
Step 5- Para fazer o Parser Top-bottom precisa remover as recursões à esquerda da BNF
  e identificar os First(x) e Follow(x) de cada token e montar a tabela de Look Ahead<br>
Step 6- Fazer o Parser Top-bottom tomando como entrada a lista de (token, tipo)
  e gerar como saída uma árvore sintática<br>
Step 7- Para fazer este parser, vai pegar o primeiro token da saída do scanner e<br>
vai analisar qual seu tipo.<br>
Ao mesmo tempo vai empilhar a primeira variável da BNF na pilha<br>
Então vai dar match com o tipo do token com a variável na BNF e olhar a tabela e ver a regra<br>
Vai desempilhar a variável atual e vai empilhar a regra da direita pra esquerda<br>
Esta regra é feita de forma A -> alpha, onde A é o símbolo variável e alpha é o que tem<br>
a direita do símbolo.<br>
A parada é ter duas estruturas, uma contendo os tokens e outra contendo os símbolos variáveis<br>
e relacionar cada um à um número. A tabela de regras será uma matriz[símbolos] x [tokens]<br>


<h1> A primeira entrega consiste em um gerador de scanners + um parser top-down para a Linguagem Mini-C (um subconjunto da linguagem C</h1>
Sua gramática pode ser encontrada em:<br>
https://github.com/TangoEnSkai/mini-c-compiler-c/blob/master/mini_c.gr<br>
e a gramática completa de C pode ser encontrada em:<br>
https://cs.wmich.edu/~gupta/teaching/cs4850/sumII06/The%20syntax%20of%20C%20in%20Backus-Naur%20form.htm ).<br><br>

<h3>Sobre o gerador de scanners:</h3> sua entrada deve ser um conjunto de expressões regulares identificadas pelo tipo de token denotado com alguma possível anotação. A saída deverá ser um scanner para os tokens especificados na entrada.

<h3>Sobre o parser:</h3> sua entrada deverá ser uma lista de tokens gerada pelo scanner correspondente à linguagem Mini-C e sua saída deverá ser uma árvore sintática para o programa dado como entrada ao scanner, em caso de aceitação do programa, ou uma lista de erros, em caso de não-aceitação.

Os entregáveis são:
- Código fonte
- Makefile e/ou intruções de compilação e execução
- Arquivos de exemplos
- Relatório descrevendo a atuação de cada membro, em caso de trabalho feito em dupla (não serão aceitas entregas feitas por mais do que dois componentes)
