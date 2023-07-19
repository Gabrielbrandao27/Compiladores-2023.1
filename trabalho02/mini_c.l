L       [A-z]
D       [0-9]
C       '([^'\\]|\\.)*'         

%{
# include "ptypes.h"
# include "mini_c.tab.h"


token_metadata * NewMetadata(int line, char * code, int type){
    token_metadata * m = (token_metadata *) malloc(sizeof(token_metadata));

    m->line = line;
    m->code = strdup(code);
    m->type = type;

    return m;
}

%}
%option yylineno
%%

"int"                             { yylval.metadata = *(NewMetadata(yylineno, "int", INT)); return INT; }
"float"                           { yylval.metadata = *(NewMetadata(yylineno, "float", FLOAT)); return FLOAT; }
"char"                            { yylval.metadata = *(NewMetadata(yylineno, "char", CHAR)); return CHAR; }
"for"                             { yylval.metadata = *(NewMetadata(yylineno, "for", FOR)); return FOR; }
"while"                           { yylval.metadata = *(NewMetadata(yylineno, "while", WHILE)); return WHILE; }
"if"                              { yylval.metadata = *(NewMetadata(yylineno, "if", IF)); return IF; }
"else"                            { yylval.metadata = *(NewMetadata(yylineno, "else", ELSE)); return ELSE; }
"+"                               { yylval.metadata = *(NewMetadata(yylineno, "+", PLUS)); return PLUS; }
"-"                               { yylval.metadata = *(NewMetadata(yylineno, "-", MINUS)); return MINUS; }
"*"                               { yylval.metadata = *(NewMetadata(yylineno, "*", TIMES)); return TIMES; }
"/"                               { yylval.metadata = *(NewMetadata(yylineno, "/", DIVIDE)); return DIVIDE; }
"="                               { yylval.metadata = *(NewMetadata(yylineno, "=", ASSIGN)); return ASSIGN; }
"<"                               { yylval.metadata = *(NewMetadata(yylineno, "<", LT)); return LT; }
">"                               { yylval.metadata = *(NewMetadata(yylineno, ">", GT)); return GT; }
"<="                              { yylval.metadata = *(NewMetadata(yylineno, "<=", LE)); return LE; }
">="                              { yylval.metadata = *(NewMetadata(yylineno, ">=", GE)); return GE; }
"=="                              { yylval.metadata = *(NewMetadata(yylineno, "==", EQ)); return EQ; }
"!="                              { yylval.metadata = *(NewMetadata(yylineno, "!=", NE)); return NE; }
"("                               { yylval.metadata = *(NewMetadata(yylineno, "(", LPAREN)); return LPAREN; }
")"                               { yylval.metadata = *(NewMetadata(yylineno, ")", RPAREN)); return RPAREN; }
"{"                               { yylval.metadata = *(NewMetadata(yylineno, "{", LBRACE)); return LBRACE; }
"}"                               { yylval.metadata = *(NewMetadata(yylineno, "}", RBRACE)); return RBRACE; }
";"                               { yylval.metadata = *(NewMetadata(yylineno, ";", SEMICOLON)); return SEMICOLON; }
","                               { yylval.metadata = *(NewMetadata(yylineno, ",", COMMA)); return COMMA; }
"."                               { yylval.metadata = *(NewMetadata(yylineno, ".", PERIOD)); return PERIOD; }
{L}({L}|{D})*                     { yylval.metadata = *(NewMetadata(yylineno, yytext, IDENTIFIER)); return IDENTIFIER; }
{D}({D})*                         { yylval.metadata = *(NewMetadata(yylineno, yytext, NUMBER_INT)); return NUMBER_INT; }
{D}({D})*("."{D}({D})*)           { yylval.metadata = *(NewMetadata(yylineno, yytext, NUMBER_FLOAT)); return NUMBER_FLOAT; }
{C}                               { yylval.metadata = *(NewMetadata(yylineno, yytext, CHARACTER)); return CHARACTER; }
\n                                { }
[ \t]                             { /* ignore whitespace */ }

%%
