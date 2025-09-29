parser grammar CParser;
options { tokenVocab=CLexer; }

start : statement+ EOF ; 
statement : block | TERM_0 TERM_1 expr TERM_2 statement ( TERM_3 statement )? | TERM_4 TERM_1 expr TERM_2 statement | TERM_5 statement TERM_4 TERM_1 expr TERM_2 TERM_6 | declaration | expr TERM_6 | TERM_6 ; 
block : TERM_7 statement* TERM_8 ; 
declaration : TERM_9 ID TERM_10 expr TERM_6 | TERM_9 ID TERM_6 ; 
expr : expr TERM_10 expr | expr TERM_11 expr | expr TERM_12 expr | expr TERM_13 expr | expr TERM_14 expr | expr TERM_15 expr | expr TERM_16 expr | expr TERM_17 expr | TERM_1 expr TERM_2 | ID | INT ; 