parser grammar JSONParser;
options { tokenVocab=JSONLexer; }

json : value EOF ; 
obj : TERM_0 pair ( TERM_1 pair )* TERM_2 | TERM_0 TERM_2 ; 
pair : STRING TERM_3 value ; 
arr : TERM_4 value ( TERM_1 value )* TERM_5 | TERM_4 TERM_5 ; 
value : STRING | NUMBER | obj | arr | TERM_6 | TERM_7 | TERM_8 ; 