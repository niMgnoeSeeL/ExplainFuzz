lexer grammar RESTLexer;

TERM_0 : '.. _' ;
TERM_1 : ':' ;
TERM_2 : '_' ;
TERM_3 : '. ' ;
TERM_4 : '=' ;
TERM_5 : '-' ;

PARAGRAPH_CHAR : [0-9a-zA-Z!"#$%&'()+,-./:;<=>?@[\]^~ \t\n\r\f] ;
PARAGRAPH_CHAR_NOSPACE : [0-9a-zA-Z!"#$%&'()+,-./:;<=>?@[\]^~] ;
PRESEP : [ \t,;()] ;
POSTSEP : [ \t,.;()] ;
ID : [a-z] ;
DIGIT_NONZERO : [1-9] ;
DIGIT : [0-9] ;
NOBR_CHAR : [0-9a-zA-Z!"#$%&'()*+,-./:;<=>?@[\]^~ \f] ;
TITLE_FIRST_CHAR : [0-9a-zA-Z!"#$%&'(),./:;<>?@[\]^~] ;
NEWLINE : '\n' ;