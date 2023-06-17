mini_c: mini_c.l mini_c.y
		bison -d mini_c.y
		flex mini_c.l
		gcc -o $@ mini_c.tab.c lex.yy.c -ll

mini_c mac: mini_c.l mini_c.y
		bison -d mini_c.y -v
		flex mini_c.l
		gcc-12 -o output.o mini_c.tab.c lex.yy.c -ll
		./output.o < exemplo.c
