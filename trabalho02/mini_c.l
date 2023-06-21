L       [A-z]
D       [0-9]
C       '([^'\\]|\\.)*'         

%{
# include "mini_c.tab.h"
%}

%%
.i
"int"                             { yylval.i = INT; return INT; }
"float"                           { yylval.i = FLOAT; return FLOAT; }
"char"                            { yylval.i = CHAR; return CHAR; }
"for"                             { yylval.i = FOR; return FOR; }
"while"                           { yylval.i = WHILE; return WHILE; }
"if"                              { yylval.i = IF; return IF; }
"else"                            { yylval.i = ELSE; return ELSE; }
"+"                               { yylval.i = PLUS; return PLUS; }
"-"                               { yylval.i = MINUS; return MINUS; }
"*"                               { yylval.i = TIMES; return TIMES; }
"/"                               { yylval.i = DIVIDE; return DIVIDE; }
"="                               { yylval.i = ASSIGN; return ASSIGN; }
"<"                               { yylval.i = LT; return LT; }
">"                               { yylval.i = GT; return GT; }
"<="                              { yylval.i = LE; return LE; }
">="                              { yylval.i = GE; return GE; }
"=="                              { yylval.i = EQ; return EQ; }
"!="                              { yylval.i = NE; return NE; }
"("                               { yylval.i = LPAREN; return LPAREN; }
")"                               { yylval.i = RPAREN; return RPAREN; }
"{"                               { yylval.i = LBRACE; return LBRACE; }
"}"                               { yylval.i = RBRACE; return RBRACE; }
";"                               { yylval.i = SEMICOLON; return SEMICOLON; }
","                               { yylval.i = COMMA; return COMMA; }
"."                               { yylval.i = PERIOD; return PERIOD; }
{L}({L}|{D})*                     { yylval.str = strdup(yytext); return IDENTIFIER; }
{D}({D})*("."{D}({D})*)?          { yylval.f = atoi(yytext); return NUMBER; }
{C}                               { yylval.str = atoi(yytext); return CHARACTER; }
\n                                { /* ignore break line */ }
[ \t]                             { /* ignore whitespace */ }

%%
