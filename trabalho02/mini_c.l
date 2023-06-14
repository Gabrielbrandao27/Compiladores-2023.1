%{

void count();
//int yylineno = 0;
#include <stdio.h>
#include <string.h>
#include "Python.h"
#define YYSTYPE void *
#include "tmp.tab.h"
extern void *py_parser;
extern void (*py_input)(PyObject *parser, char *buf, int *result, int max_size);
#define returntoken(tok) /*printf("%d=%s\n", tok, yytext);*/ yylval = PyUnicode_FromString(strdup(yytext)); return (tok);
#define YY_INPUT(buf,result,max_size) { (*py_input)(py_parser, buf, &result, max_size); }

%}

%%

"identifier"        { count(); returntoken(IDENTIFIER)}
"number"            { count(); returntoken(NUMBER)}
"int"               { count(); returntoken(INT)}
"float"             { count(); returntoken(FLOAT)}
"for"               { count(); returntoken(FOR)}
"while"             { count(); returntoken(WHILE)}
"if"                { count(); returntoken(IF)}
"else"              { count(); returntoken(ELSE)}
"+"                 { count(); returntoken(PLUS)}
"-"                 { count(); returntoken(MINUS)}
"*"                 { count(); returntoken(TIMES)}
"/"                 { count(); returntoken(DIVIDE)}
"="                 { count(); returntoken(ASSIGN)}
"<"                 { count(); returntoken(LT)}
">"                 { count(); returntoken(GT)}
"<="                { count(); returntoken(LE)}
">="                { count(); returntoken(GE)}
"=="                { count(); returntoken(EQ)}
"!="                { count(); returntoken(NE)}
"("                 { count(); returntoken(LPAREN)}
")"                 { count(); returntoken(RPAREN)}
"{"                 { count(); returntoken(LBRACE)}
"}"                 { count(); returntoken(RBRACE)}
";"                 { count(); returntoken(SEMICOLON)}
","                 { count(); returntoken(COMMA)}
"."                 { count(); returntoken(PERIOD)}

%%

yywrap()
{
        return(1);
}

int column = 0;

void count()
{
        int i;

        for (i = 0; yytext[i] != '\0'; i++)
                if (yytext[i] == '\n')
                        column = 0;
                else if (yytext[i] == '\t')
                        column += 8 - (column % 8);
                else
                        column++;

        /*ECHO*/;
}
