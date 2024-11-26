grammar multiplica;

// Lexer rules
NUMBER  : [0-9]+ ;
ID      : [a-zA-Z]+ ;
WS      : [ \t\r\n]+ -> skip ;
LPAREN  : '(' ;
RPAREN  : ')' ;
COLON   : ':' ;
COMMA   : ',' ;
DEF     : 'Def' ;
RETURN  : 'Return' ;
EQ      : '=' ;
MULT    : '*' ;
MINUS   : '-' ;
PRINT   : 'print' ;
NEWLINE : '\n' ;

// Parser rules
program : (functionDef | main)+ ;

functionDef : DEF ID LPAREN params RPAREN COLON body ;

params      : ID (COMMA ID)* ;

body        : RETURN expr ;

main        : PRINT LPAREN ID LPAREN NUMBER COMMA NUMBER RPAREN RPAREN ;

expr        : expr MULT expr
            | expr MINUS expr
            | NUMBER
            | ID ;  // Para manejar las variables y funciones
