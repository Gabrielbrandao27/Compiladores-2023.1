%{

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct context_type {
    char * variable;
    const char * context;
    int is_function;
    int type;
    struct context_type * next;
    int filled;
};

typedef struct context_type context_type;

context_type * append(context_type * actual, int type, char * variable, char * context){
    actual->type = type;
    actual->filled = 1;
    actual->variable = variable;
    actual->context = malloc(sizeof(char) * 50);
    strcpy(actual->context, context);
    actual->next = malloc(sizeof(context_type));
    actual->next->filled = 0;
    return actual->next;
}

context_type * root;
context_type * actual;

char context[50];


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
    : Function_Declaration ArgList RPAREN CompoundStmt { printf("REDUCED FUNCTION\n" );}
    | Function_Declaration ArgList RPAREN CompoundStmt Function { printf("REDUCED FUNCTION \n" );}
    ;

Function_Declaration
  : Type IDENTIFIER LPAREN 
  { 
    actual = append(actual, $<i>1 , $<str>2, "global"); 
    strcpy(context, $<str>2); 
    printf("function context: %s \n", context); 
  }
  ;

ArgList
    : Arg 
    | ArgList COMMA Arg
    ;

Arg
    : Type IDENTIFIER 
    { 
      printf("arg %d %s %i \n", $<i>1 , $<str>2, actual->filled );  
      actual = append(actual, $<i>1 , $<str>2, context); 
    }
    ;

Declaration
    : Type IdentList SEMICOLON 
    {
      char * token = strtok($<str>2, ",");

      while( token != NULL ) {
          actual = append(actual, $<i>1 , token, context);
          token = strtok(NULL, ",");
      }
    }
    ;

Type
    : INT
    | FLOAT
    | CHAR
    ;

IdentList
    : IDENTIFIER COMMA IdentList 
    { 
      printf("Ident List %s %s \n", $<str>$, $<str>3);  
      strcat($<str>$, ","); 
      strcat($<str>$, $<str>3); 
    }
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
  printf("before parse \n");
  root = (context_type*) malloc(sizeof(context_type));
  root->filled = 0;
  actual = root;

  yyparse();

  printf("parse ended\n");

  context_type * cs = root;
  while(cs->filled){
    printf("variable: %s of type %i and context %s \n", cs->variable, cs->type, cs->context);
    cs = cs->next;
  }

  printf("ended\n");

  return 0;

}



yyerror(char *s)
{
  printf( "error: %s %s \n", s, stderr);
}