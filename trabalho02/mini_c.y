%{

%}

%token IDENTIFIER NUMBER INT FLOAT FOR WHILE IF ELSE
%token PLUS MINUS TIMES DIVIDE ASSIGN LT GT LE GE EQ NE
%token LPAREN RPAREN LBRACE RBRACE SEMICOLON COMMA PERIOD

%start Function

%%

Function
    : Type IDENTIFIER LPAREN ArgList RPAREN CompoundStmt
    ;

ArgList
    : Arg 
    | ArgList, Arg
    ;

Arg
    : Type IDENTIFIER
    ;

Declaration
    : Type IdentList SEMICOLON
    ;

Type
    : INT
    | FLOAT
    ;

IdentList
    : IDENTIFIER , IdentList
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

ElsePart
    : ELSE Stmt
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
    | NUMBER
    ;

%%
#include <stdio.h>

extern char yytext[];
extern int column;

yyerror(s)
char *s;
{
	fflush(stdout);
	printf("\n%*s\n%*s\n", column, "^", column, s);
}