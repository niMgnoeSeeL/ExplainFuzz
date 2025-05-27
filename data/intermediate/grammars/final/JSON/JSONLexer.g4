lexer grammar JSONLexer;

TERM_0 : '{' ;
TERM_1 : ',' ;
TERM_2 : '}' ;
TERM_3 : ':' ;
TERM_4 : '[' ;
TERM_5 : ']' ;
TERM_6 : 'true' ;
TERM_7 : 'false' ;
TERM_8 : 'null' ;

STRING : '"' ( ESC | SAFECODEPOINT )* '"' ;
fragment ESC : '\\' ( ["\\/bfnrt] | UNICODE ) ;
fragment UNICODE : 'u' HEX HEX HEX HEX ;
fragment HEX : [0-9a-fA-F] ;
fragment SAFECODEPOINT : ~ ["\\\u0000-\u001F] ;
NUMBER : '-'? INT ( '.' [0-9]+ )? EXP? ;
fragment INT : '0' | [1-9] [0-9]* ;
fragment EXP : [Ee] [+-]? [0-9]+ ;
WS : [ \t\n\r]+ -> skip ;