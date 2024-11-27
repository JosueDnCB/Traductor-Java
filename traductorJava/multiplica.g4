grammar multiplica;

// Lexer rules
DEF     : 'def' ;
RETURN  : 'return' ;
PRINT   : 'print' ;
ID      : [a-zA-Z]+ ;
NUMBER  : [0-9]+ ;
WS      : [ \t\r\n]+ -> skip ;
LPAREN  : '(' ;
RPAREN  : ')' ;
COLON   : ':' ;
COMMA   : ',' ;
EQ      : '=' ;
MULT    : '*' ;
MINUS   : '-' ;
NEWLINE : '\n' ;

// Parser rules
program : functionDef* main+ ;


functionDef : DEF ID LPAREN params RPAREN COLON body ;

params      : ID (COMMA ID)* ;

body        : RETURN expr ;

main        : PRINT LPAREN ID LPAREN NUMBER COMMA NUMBER RPAREN RPAREN ;


expr        : expr MULT expr
            | expr MINUS expr
            | NUMBER
            | ID ; 
