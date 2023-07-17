L       [A-z]
D       [0-9]
C       '([^'\\]|\\.)*'         

%{
# include "mini_c.tab.h"

int linha = 1;
%}
%%
"int"                             { yylval.linha = linha; yylval.code = "int";  yylval.integer_value = INT; return INT; }
"float"                           { yylval.linha = linha; linha; yylval.code = "float";  yylval.integer_value = FLOAT; return FLOAT; }
"char"                            { yylval.linha = linha; linha; yylval.code = "char";  yylval.integer_value = CHAR; return CHAR; }
"for"                             { yylval.linha = linha; linha; yylval.code = "for";  yylval.integer_value = FOR; return FOR; }
"while"                           { yylval.linha = linha; linha; yylval.code = "while";  yylval.integer_value = WHILE; return WHILE; }
"if"                              { yylval.linha = linha; linha; yylval.code = "if";  yylval.integer_value = IF; return IF; }
"else"                            { yylval.linha = linha; linha; yylval.code = "else";  yylval.integer_value = ELSE; return ELSE; }
"+"                               { yylval.linha = linha; linha; yylval.code = "+";  yylval.integer_value = PLUS; return PLUS; }
"-"                               { yylval.linha = linha; linha; yylval.code = "-";  yylval.integer_value = MINUS; return MINUS; }
"*"                               { yylval.linha = linha; linha; yylval.code = "*";  yylval.integer_value = TIMES; return TIMES; }
"/"                               { yylval.linha = linha; linha; yylval.code = "/";  yylval.integer_value = DIVIDE; return DIVIDE; }
"="                               { yylval.linha = linha; linha; yylval.code = "=";  yylval.integer_value = ASSIGN; return ASSIGN; }
"<"                               { yylval.linha = linha; linha; yylval.code = "<";  yylval.integer_value = LT; return LT; }
">"                               { yylval.linha = linha; linha; yylval.code = ">";  yylval.integer_value = GT; return GT; }
"<="                              { yylval.linha = linha; linha; yylval.code = "<=";  yylval.integer_value = LE; return LE; }
">="                              { yylval.linha = linha; linha; yylval.code = ">=";  yylval.integer_value = GE; return GE; }
"=="                              { yylval.linha = linha; linha; yylval.code = "==";  yylval.integer_value = EQ; return EQ; }
"!="                              { yylval.linha = linha; linha; yylval.code = "!=";  yylval.integer_value = NE; return NE; }
"("                               { yylval.linha = linha; linha; yylval.code = "(";  yylval.integer_value = LPAREN; return LPAREN; }
")"                               { yylval.linha = linha; linha; yylval.code = ")";  yylval.integer_value = RPAREN; return RPAREN; }
"{"                               { yylval.linha = linha; linha; yylval.code = "{";  yylval.integer_value = LBRACE; return LBRACE; }
"}"                               { yylval.linha = linha; linha; yylval.code = "}";  yylval.integer_value = RBRACE; return RBRACE; }
";"                               { yylval.linha = linha; linha; yylval.code = ";";  yylval.integer_value = SEMICOLON; return SEMICOLON; }
","                               { yylval.linha = linha; linha; yylval.code = ",";  yylval.integer_value = COMMA; return COMMA; }
"."                               { yylval.linha = linha; linha; yylval.code = ".";  yylval.integer_value = PERIOD; return PERIOD; }
{L}({L}|{D})*                     { yylval.linha = linha; yylval.code = strdup(yytext); yylval.str = strdup(yytext); return IDENTIFIER; }
{D}({D})*                         { yylval.linha = linha; yylval.code = strdup(yytext); yylval.float_value = atoi(yytext); return NUMBER_INT; }
{D}({D})*("."{D}({D})*)           { yylval.linha = linha; yylval.code = strdup(yytext); yylval.float_value = atoi(yytext); return NUMBER_FLOAT; }
{C}                               { yylval.linha = linha; yylval.code = strdup(yytext); yylval.str = yytext; return CHARACTER; }
\n                                {  }
[ \t]                             { /* ignore whitespace */ }

%%
