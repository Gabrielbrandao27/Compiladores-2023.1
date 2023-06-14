%{

%}


%%

%token IDENTIFIER NUMBER INT FLOAT FOR WHILE IF ELSE
%token PLUS MINUS TIMES DIVIDE ASSIGN LT GT LE GE EQ NE
%token LPAREN RPAREN LBRACE RBRACE SEMICOLON COMMA PERIOD

%%

%start Function

%%

Function
    :Type IDENTIFIER LPAREN ArgList RPAREN CompoundStmt
    ;

ArgList
    :Arg ArgList2
    ;

ArgList2
    : COMMA Arg ArgList2
    | ε
    ;

Arg
    :Type IDENTIFIER
    ;

Declaration
    :Type IdentList SEMICOLON
    ;

Type
    : INT
    | FLOAT
    ;

IdentList
    :IDENTIFIER IdentList2
    ;

IdentList2
    : COMMA IdentList
    | ε
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
    : FOR LPAREN Expr SEMICOLON OptExpr SEMICOLON OptExpr RPAREN Stmt
    ;

OptExpr
    : Expr
    | ε
    ;

WhileStmt
    : WHILE LPAREN Expr RPAREN Stmt
    ;

IfStmt
    : IF LPAREN Expr RPAREN Stmt ElsePart
    ;

ElsePart
    : ELSE Stmt
    | ε
    ;

CompoundStmt
    : LBRACE StmtList RBRACE
    ;

StmtList
    : Stmt StmtList2
    ;

StmtList2
    : StmtList
    | ε
    ;

Expr
    : IDENTIFIER ASSIGN Expr
    | Rvalue
    ;

Rvalue
    : Mag Rvalue2
    ;

Rvalue2
    : Compare Rvalue
    | ε
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
    : Term Mag2
    ;

Mag2
    : PLUS Term Mag2
    | MINUS Term Mag2
    | ε
    ;

Term
    : Factor Term2
    ;

Term2
    : TIMES Factor Term2
    | DIVIDE Factor Term2
    | ε
    ;

Factor
    : LPAREN Expr RPAREN
    | MINUS Factor
    | PLUS Factor
    | IDENTIFIER
    | NUMBER
    ;

%%

%%
int main(float var1){
    float var2;
}