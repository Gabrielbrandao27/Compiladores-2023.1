%{
    #include <stdio.h>
%}

%error-verbose
%token IDENTIFIER NUMBER CHARACTER INT FLOAT CHAR FOR WHILE IF ELSE
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
    : Type IDENTIFIER LPAREN ArgList RPAREN CompoundStmt { printf("1: %s \n", $<str>2); } 
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

struct context_type {
    char * variable_name_and_context;
    int type;
};

typedef struct context_type context_type;

context_type * table[50];

void main(int argc, char **argv)
{

    for (int i = 0; i < 50; i++){
      table[i] = NULL;
    };

  if(table[0] == NULL){
    printf("is null %p", table[0]);
    table[0] = malloc(sizeof(context_type) * 5);
    table[0][0].type = 12;
    table[0][0].variable_name_and_context = "123";
    printf(" \nis not null %s \n", table[0][0].variable_name_and_context);
  };
  yyparse();
  printf("parsed \n");
}

yyerror(char *s)
{
  printf( "error: %s %s \n", s, stderr);
}