lexer grammar CSVLexer;

TERM_0 : ',' ;
TERM_1 : '\r' ;
TERM_2 : '\n' ;

TEXT : ~ [,\n\r"]+ ;
STRING : '"' ( '""' | ~ '"' )* '"' ;