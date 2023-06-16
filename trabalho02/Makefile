mini_c: mini_c.l mini_c.y
		bison -d mini_c.y
		flex mini_c.l
		gcc -o $@ mini_c.tab.c lex.yy.c -lfl