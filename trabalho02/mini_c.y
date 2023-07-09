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

context_type * find(context_type * root, char * variable, char * context){
  context_type * cs = root;
  while(cs->filled){
    if(strcmp(cs->variable, variable) == 0 && strcmp(cs->context, context) == 0) break;
    printf("searching variable: %s of type %i and context %s value: %s\n", cs->variable, cs->type, cs->context, variable);
    cs = cs->next;
  }

  return cs;
}

context_type * root;
context_type * actual;
char context[50];

%}

%locations
%error-verbose
%token IDENTIFIER NUMBER_INT NUMBER_FLOAT CHARACTER INT FLOAT CHAR FOR WHILE IF ELSE
%token PLUS MINUS TIMES DIVIDE ASSIGN LT GT LE GE EQ NE
%token LPAREN RPAREN LBRACE RBRACE SEMICOLON COMMA PERIOD
%union {
    char *str;
    int integer_value;
    float float_value;
    int type;
}

%right ELSE
%expect 1

%%

Function
    : Function_Declaration ArgList RPAREN CompoundStmt { printf("REDUCED FUNCTION\n" ); }
    | Function_Declaration ArgList RPAREN CompoundStmt Function { printf("REDUCED FUNCTION \n" );}
    ;

Function_Declaration
  : Type IDENTIFIER LPAREN 
  { 
    actual = append(actual, $<integer_value>1 , $<str>2, "global"); 
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
      printf("arg %d %s %i \n", $<integer_value>1 , $<str>2, actual->filled );  
      actual = append(actual, $<integer_value>1 , $<str>2, context); 
    }
    ;

Declaration
    : Type IdentList SEMICOLON 
    {
      char * token = strtok($<str>2, ",");

      while( token != NULL ) {
          actual = append(actual, $<integer_value>1 , token, context);
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
    { 
      context_type * s = find(root, $<str>1, context); 
      if(!s->filled) { yyerror(&@1, "undeclared variable");  break;};
      printf("types %d %d \n", s->type, $<type>3); 
      if(s->type == $<type>3) {$<type>$ = $<type>3;} else {yyerror("type error");break;}  
    }
    | Rvalue
    ;

Rvalue
    : Rvalue Compare Mag { printf("types %d %d \n", $<type>1, $<type>3); if($<type>1 == $<type>3) {$<type>$ = $<type>3;} else {yyerror("type error");break;}  }
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
    : Mag PLUS Term { if($<type>1 == $<type>3) {$<type>$ = $<type>3;} else {yyerror("type error");break;}  }
    | Mag MINUS Term { if($<type>1 == $<type>3) {$<type>$ = $<type>3;} else {yyerror("type error");break;}  }
    | Term
    ;

Term
    : Term TIMES Factor {if($<type>1 == $<type>3) {$<type>$ = $<type>3;} else {yyerror("type error");break;}  }
    | Term DIVIDE Factor {if($<type>1 == $<type>3) {$<type>$ = $<type>3;} else {yyerror("type error");break;}  }
    | Factor 
    ;

Factor
    : LPAREN Expr RPAREN
    | MINUS Factor { $<type>$ = $<type>2; }
    | PLUS Factor { $<type>$ = $<type>2; }
    | IDENTIFIER 
    { 
      context_type * s = find(root, $<str>1, context);
      if(!s->filled) {yyerror(&@1,"variable not declared "); break;};
      printf("factor identifier: %s \n", s->variable); 
      $<type>$ = s->type; 
    }
    | NUMBER_INT { $<type>$ = INT; }
    | NUMBER_FLOAT { $<type>$ = FLOAT; }
    | CHARACTER { $<type>$ = CHAR; }
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

  printf("ended %d\n");

  return 0;

}



yyerror(YYLTYPE *bloc, char *s)
{
  printf("%s %s Line %d:c%d to %d:c%d",s, stderr, 
                        bloc->first_line, bloc->first_column,
                        bloc->last_line, bloc->last_column);
} 