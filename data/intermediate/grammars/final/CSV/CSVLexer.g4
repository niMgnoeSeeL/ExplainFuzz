lexer grammar CSVLexer;

TERMINAL0 : ',' ;
TERMINAL1 : '\r' ;
TERMINAL2 : '\n' ;

TEXT : ~ [,\n\r"]+ ;
STRING : '"' ( '""' | ~ '"' )* '"' ;