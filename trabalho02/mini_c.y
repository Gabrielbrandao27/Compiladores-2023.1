%{
#include "ptypes.h"
#include <stdio.h>
#include <stdlib.h>
#include "mini_c.tab.h"
#include <string.h>
#include <stdarg.h>

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
    // printf("searching variable: %s of type %i and context %s value: %s\n", cs->variable, cs->type, cs->context, variable);
    cs = cs->next;
  }

  return cs;
}

void join(char * s1, char * s2){
  if ((strcmp(s2, "}") == 0) || (strcmp(s1, "{") == 0) || (strcmp(s1, ";") == 0))
  {
    strcat(s1, "\n");
    strcat(s1, s2);
  }else{
    strcat(s1, " ");
    strcat(s1, s2);
  }
}
 
int label_counter = 0;
context_type * root;
context_type * actual;
char context[50];

%}

%error-verbose
%token <metadata> IDENTIFIER NUMBER_INT NUMBER_FLOAT CHARACTER INT FLOAT CHAR FOR WHILE IF ELSE
%token <metadata> PLUS MINUS TIMES DIVIDE ASSIGN LT GT LE GE EQ NE
%token <metadata> LPAREN RPAREN LBRACE RBRACE SEMICOLON COMMA PERIOD
%union {
    token_metadata metadata;
};



%right ELSE

%type<metadata> Arg Type IdentList Expr Rvalue Mag Term Factor CompoundStmt StmtList Stmt Compare
%type<metadata> IfStmt Function_Declaration Declaration ForStmt WhileStmt ArgList OptExpr Function InitialRule

%expect 1

%%

InitialRule
  : Function { printf("\033[1;32m %s \033[1;0m", $$.code);};

Function
    : Function_Declaration ArgList RPAREN CompoundStmt { join($$.code, $2.code); join($$.code, $3.code); join($$.code, $4.code);}
    | Function_Declaration ArgList RPAREN CompoundStmt Function { join($$.code, $2.code); join($$.code, $3.code); join($$.code, $4.code); join($$.code, $5.code);
    }
    ;

Function_Declaration
  : Type IDENTIFIER LPAREN 
  { 
    actual = append(actual, $1.type , $2.code, "global"); 
    strcpy(context, $2.code); 
    join($$.code, $2.code); join($$.code, $3.code); 
  }
  ;

ArgList
    : Arg 
    | ArgList COMMA Arg {
      join($$.code, $2.code); join($$.code, $3.code); 
    }
    ;

Arg
    : Type IDENTIFIER 
    { 
      actual = append(actual, ($1).type , ($2).code, context); 
      join($$.code, $2.code);
    }
    ;

Declaration
    : Type IdentList SEMICOLON 
    {
      join($$.code, $2.code); join($$.code, $3.code); 
    
      char * token = strtok($2.code, ",");
      while( token != NULL ) {
          actual = append(actual, $1.type, token, context);
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
    : IDENTIFIER
    | IDENTIFIER COMMA IdentList 
    { 
      strcat($$.code, $2.code); strcat($$.code, $3.code); 
      //printf("ident list %s|", $$.code);
    }
    ;

Stmt
    : ForStmt 
    | WhileStmt
    | Expr SEMICOLON {join($$.code, $2.code);}
    | IfStmt
    | CompoundStmt
    | Declaration
    | SEMICOLON
    ;

ForStmt
    : FOR LPAREN Expr RPAREN Stmt {
      // char label_str[15];
      // sprintf(label_str, "LABEL %d", label_counter++);
      // $$.code = strdup("if");

      join($$.code, $2.code); join($$.code, $3.code); join($$.code, $4.code); 
      join($$.code, $5.code);
    }
    | FOR LPAREN Expr SEMICOLON OptExpr RPAREN Stmt {
      // char label_str[15];
      // sprintf(label_str, "LABEL %d", label_counter++);
      // join($$.code, "\n");
      // join($$.code, label_str);
      // $$.code = strdup("if");
      join($$.code, $2.code); join($$.code, $3.code); join($$.code, $4.code); join($$.code, $5.code); join($$.code, $6.code); 
      join($$.code, $7.code); 
    }
    | FOR LPAREN Expr SEMICOLON OptExpr SEMICOLON OptExpr RPAREN Stmt{
      // char label_str[15];
      // sprintf(label_str, "LABEL %d", label_counter++);
      // $$.code = strdup("if");
      join($$.code, $2.code); join($$.code, $3.code); join($$.code, $4.code); join($$.code, $5.code); join($$.code, $6.code); 
      join($$.code, $7.code); join($$.code, $8.code); 
      join($$.code, $9.code); 
    }
    ;

OptExpr
    : Expr
    ;

WhileStmt
    : WHILE LPAREN Expr RPAREN Stmt {
      join($$.code, $2.code); join($$.code, $3.code); join($$.code, $4.code); join($$.code, $5.code);
    }
    ;

IfStmt
    : IF LPAREN Expr RPAREN Stmt{
      join($$.code, $2.code); join($$.code, $3.code); join($$.code, $4.code); join($$.code, $5.code);
    }
    | IF LPAREN Expr RPAREN Stmt ELSE Stmt {
      join($$.code, $2.code); join($$.code, $3.code); join($$.code, $4.code); join($$.code, $5.code); join($$.code, $6.code); 
      join($$.code, $7.code); 
    }
    ;

CompoundStmt
    : LBRACE StmtList RBRACE { join($$.code, $2.code); join($$.code, $3.code); }
    ;

StmtList
    : Stmt
    | StmtList Stmt {join($$.code, $2.code);}
    ;

Expr
    : IDENTIFIER ASSIGN Expr 
    { 
      context_type * s = find(root, $1.code, context); 
      if(!s->filled) { yyerror($1, "undeclared variable");  break;};
      if(s->type == $3.type) {$$.type = $3.type;} else {yyerror($3, "type error");break;}  
      join($$.code, $2.code); join($$.code, $3.code); 
    }
    | Rvalue
    ;

Rvalue
    : Rvalue Compare Mag { if($1.type == $3.type) {$$.type = $3.type;} else { yyerror($3, "type error");break;}  
    join($$.code, $2.code); join($$.code, $3.code); 
    }
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
    : Mag PLUS Term { if($1.type == $3.type) {$$.type = $3.type;} else {yyerror($3, "type error");break;} 
    join($$.code, $2.code); join($$.code, $3.code); 
    }
    | Mag MINUS Term { if($1.type == $3.type) {$$.type = $3.type;} else {yyerror($3, "type error");break;} 
    join($$.code, $2.code); join($$.code, $3.code);  
    }
    | Term
    ;

Term
    : Term TIMES Factor { if($1.type == $3.type) {$$.type = $3.type;} else {yyerror($3, "type error");break;} 
    join($$.code, $2.code); join($$.code, $3.code); 
    }
    | Term DIVIDE Factor { if($1.type == $3.type) {$$.type = $3.type;} else {yyerror($3, "type error");break;}   
    join($$.code, $2.code); join($$.code, $3.code); 
    }
    | Factor
    ;
Factor
    : LPAREN Expr RPAREN {join($$.code, $2.code); join($$.code, $3.code); }
    | MINUS Factor { $$.type = $2.type; join($$.code, $2.code);  }
    | PLUS Factor { $$.type = $2.type; join($$.code, $2.code); 
      }
    | IDENTIFIER 
    { 
      context_type * s = find(root, $1.code, context);
      if(!s->filled) {yyerror($1, "variable not declared "); break;};
      $$.type = s->type;
    }
    | NUMBER_INT { $$.type = INT;}
    | NUMBER_FLOAT { $$.type = FLOAT; }
    | CHARACTER { $$.type = CHAR; }
    ;

%%

int main(int argc, char **argv)
{
  root = (context_type*) malloc(sizeof(context_type));
  root->filled = 0;
  actual = root;
  printf("\033[1;32m RESULT CODE: \033[1;0m \n");
  yyparse();
  return 0;
}



int yyerror(token_metadata t, char *s)
{
  printf("\033[1;31m %s on Line %d \033[1;0m \n", s, t.line);
} 