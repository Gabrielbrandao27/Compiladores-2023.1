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