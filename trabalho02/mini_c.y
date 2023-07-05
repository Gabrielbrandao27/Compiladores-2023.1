%{

#include <stdio.h>
#include <stdlib.h>

struct context_type {
    char * variable;
    char * context;
    int type;
    struct context_type * next;
};

typedef struct context_type context_type;

context_type * append(context_type * actual, int type, char * variable, char * context){
    printf("is null %p", actual);
    if(actual == NULL){
        printf("is null %p", actual);

        actual = malloc(sizeof(context_type));
        actual->type = type;
        actual->variable = variable;
        actual->context = context;
        printf(" \nis not null %s \n", actual->variable);
        return actual;
    } else {
        actual->next = malloc(sizeof(context_type));
        actual->next->type = type;
        actual->next->variable = variable;
        actual->next->context = context;
        return actual->next;
    };
}

context_type * root = NULL;
context_type * actual = NULL;

%}

%error-verbose
%token IDENTIFIER NUMBER_INT NUMBER_FLOAT CHARACTER INT FLOAT CHAR FOR WHILE IF ELSE
%token PLUS MINUS TIMES DIVIDE ASSIGN LT GT LE GE EQ NE
%token LPAREN RPAREN LBRACE RBRACE SEMICOLON COMMA PERIOD
%union {
    char *str;
    int i;
    float f;
}

%right ELSE
%expect 1

%%

Function
    : Type IDENTIFIER LPAREN ArgList RPAREN CompoundStmt { printf("function: %d %s \n", $<i>1, $<str>2);  actual = append(actual, $<i>1 , $<str>2, "global"); } 
    | Type IDENTIFIER LPAREN ArgList RPAREN CompoundStmt Function
    ;

ArgList
    : Arg 
    | ArgList COMMA Arg
    ;

Arg
    : Type IDENTIFIER  { printf("arg: %s \n", $<str>2); } 
    ;

Declaration
    : Type IdentList SEMICOLON
    ;

Type
    : INT
    | FLOAT
    | CHAR
    ;

IdentList
    : IDENTIFIER COMMA IdentList
    | IDENTIFIER
    ;

Stmt
    : ForStmt 
    | WhileStmt
    | Expr SEMICOLON
    | IfStmt
    | CompoundStmt
    | Declaration
    | SEMICOLON
    ;

ForStmt
    : FOR LPAREN Expr RPAREN Stmt
    | FOR LPAREN Expr SEMICOLON OptExpr RPAREN Stmt
    | FOR LPAREN Expr SEMICOLON OptExpr SEMICOLON OptExpr RPAREN Stmt
    ;

OptExpr
    : Expr
    ;

WhileStmt
    : WHILE LPAREN Expr RPAREN Stmt
    ;

IfStmt
    : IF LPAREN Expr RPAREN Stmt
    | IF LPAREN Expr RPAREN Stmt ELSE Stmt
    ;

CompoundStmt
    : LBRACE StmtList RBRACE
    ;

StmtList
    : Stmt
    | StmtList Stmt
    ;

Expr
    : IDENTIFIER ASSIGN Expr
    | Rvalue
    ;

Rvalue
    : Rvalue Compare Mag
    | Mag
    ;

Compare
    : EQ 
    | LT
    | GT
    | LE
    | GE
    | NE
    ;

Mag
    : Mag PLUS Term
    | Mag MINUS Term
    | Term
    ;

Term
    : Term TIMES Factor
    | Term DIVIDE Factor
    | Factor
    ;

Factor
    : LPAREN Expr RPAREN
    | MINUS Factor
    | PLUS Factor
    | IDENTIFIER
    | NUMBER_INT
    | NUMBER_FLOAT
    | CHARACTER
    ;

%%

void main(int argc, char **argv)
{
  yyparse();
  printf("\n actual: %s", actual->variable);
}



yyerror(char *s)
{
  printf( "error: %s %s \n", s, stderr);
}