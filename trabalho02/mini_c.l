L       [A-z]
D       [0-9]

%{
        #include <stdio.h>
        #include <string.h>
        enum yytokentype {
                IDENTIFIER = 99,
                NUMBER = 1,
                INT = 2,
                FLOAT = 3,
                FOR = 4,
                WHILE = 5,
                IF = 6,
                ELSE = 7,
                PLUS = 8,
                MINUS = 9,
                TIMES = 10,
                DIVIDE = 11,
                ASSIGN = 12,
                LT = 13,
                GT = 14,
                LE = 15,
                GE = 16,
                EQ = 17,
                NE = 18,
                LPAREN = 19,
                RPAREN = 20,
                LBRACE = 21,
                RBRACE = 22,
                SEMICOLON = 23,
                COMMA = 24,
                PERIOD = 25,
        };

        int yylval;
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
{D}({D})*("."{D}({D})*)?          { yylval = atoi(yytext); return NUMBER; }
\n                                { /* ignore break line */ }
[ \t]                             { /* ignore whitespace */ }

%%

void main (int argc, char **argv)
{
        int tok;
        while (tok = yylex())
                printf("%d\n", tok);
}
