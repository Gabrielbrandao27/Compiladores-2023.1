L       [A-z]
D       [0-9]

%{
# include "mini_c.tab.h"
%}

%%

"int"                             { return INT; }
"float"                           { return FLOAT; }
"for"                             { return FOR; }
"while"                           { return WHILE; }
"if"                              { return IF; }
"else"                            { return ELSE; }
"+"                               { return PLUS; }
"-"                               { return MINUS; }
"*"                               { return TIMES; }
"/"                               { return DIVIDE; }
"="                               { return ASSIGN; }
"<"                               { return LT; }
">"                               { return GT; }
"<="                              { return LE; }
">="                              { return GE; }
"=="                              { return EQ; }
"!="                              { return NE; }
"("                               { return LPAREN; }
")"                               { return RPAREN; }
"{"                               { return LBRACE; }
"}"                               { return RBRACE; }
";"                               { return SEMICOLON; }
","                               { return COMMA; }
"."                               { return PERIOD; }
{L}({L}|{D})*                     { return IDENTIFIER; }
{D}({D})*("."{D}({D})*)?          { return NUMBER; }
\n                                { /* ignore break line */ }
[ \t]                             { /* ignore whitespace */ }

%%
