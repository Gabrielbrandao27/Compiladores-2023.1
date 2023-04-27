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
