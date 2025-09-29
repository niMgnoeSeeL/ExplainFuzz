lexer grammar CLexer;

TERM_0 : 'if' ;
TERM_1 : '(' ;
TERM_2 : ')' ;
TERM_3 : 'else' ;
TERM_4 : 'while' ;
TERM_5 : 'do' ;
TERM_6 : ';' ;
TERM_7 : '{' ;
TERM_8 : '}' ;
TERM_9 : 'int' ;
TERM_10 : '=' ;
TERM_11 : '==' ;
TERM_12 : '<' ;
TERM_13 : '+' ;
TERM_14 : '-' ;
TERM_15 : '*' ;
TERM_16 : '&&' ;
TERM_17 : '||' ;

ID : [a-z] ;
INT : [0-9]+ ;
WS : [ \t\r\n]+ -> skip ;