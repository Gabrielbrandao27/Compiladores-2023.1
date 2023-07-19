mini_c: mini_c.l mini_c.y
		bison -d mini_c.y
		flex mini_c.l
		cc -o $@ mini_c.tab.c lex.yy.c -lfl


mini_c_geracao_codigo:
		bison -d mini_c.y -v
		flex mini_c.l
		gcc-12 -o output.o mini_c.tab.c lex.yy.c -ll
		./output.o < exemplo-geracao-codigo.txt

mini_c_exemplo_erro:
		bison -d mini_c.y -v
		flex mini_c.l
		gcc-12 -o output.o mini_c.tab.c lex.yy.c -ll
		./output.o < exemplo-tratamento-erro.txt
