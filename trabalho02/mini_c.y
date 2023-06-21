%{
    #include <stdio.h>
%}

%token IDENTIFIER NUMBER CHARACTER INT FLOAT CHAR FOR WHILE IF ELSE
%token PLUS MINUS TIMES DIVIDE ASSIGN LT GT LE GE EQ NE
%token LPAREN RPAREN LBRACE RBRACE SEMICOLON COMMA PERIOD
%union {
    char *str;
    int i;
    float f;
}

%right ELSE

%%

Function
    : Type IDENTIFIER LPAREN ArgList RPAREN CompoundStmt { printf("1: %d", $<i>1); } 
    | Type IDENTIFIER LPAREN ArgList RPAREN CompoundStmt Function /*{ printf("2: %d, %d, %d, %d, %d, %d\n", $1, $2, $3, $4, $5, $6); }*/
    ;

ArgList
    : Arg 
    | ArgList COMMA Arg
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
    | NUMBER
    | CHARACTER
    ;

%%

void main(int argc, char **argv)
{
  yyparse();
  printf("parsed");
}

yyerror(char *s)
{
  fprintf(stderr, "error: %s\n", s);
}